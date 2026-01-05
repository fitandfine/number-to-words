def number_to_words(n: int) -> str:
    """
    Convert a non-negative integer into its English word representation.

    Example:
        1000001     -> "one million one"
        1000000000000 -> "one trillion"

    The function works by breaking the number into chunks of three digits
    (thousands, millions, billions, trillions), because this mirrors how
    large numbers are spoken in English.
    """

    # Zero is a special case because the main logic
    # only works for positive numbers
    if n == 0:
        return "zero"

    # Lookup tables for converting digits into words.
    # Using tuples keeps this simple, fast, and readable.
    ones = (
        "", "one", "two", "three", "four",
        "five", "six", "seven", "eight", "nine"
    )

    teens = (
        "ten", "eleven", "twelve", "thirteen", "fourteen",
        "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
    )

    tens = (
        "", "", "twenty", "thirty", "forty",
        "fifty", "sixty", "seventy", "eighty", "ninety"
    )

    # Scale names for each group of three digits.
    # This version supports numbers up to the trillions range.
    scales = (
        "",
        "thousand",
        "million",
        "billion",
        "trillion"
    )

    def process_chunk(num: int) -> str:
        """
        Convert a number less than 1000 into words.

        This helper function handles only one chunk at a time,
        keeping the main function easier to read and reason about.
        """
        words = ""

        # Handle the hundreds place (e.g., 345 -> "three hundred")
        if num >= 100:
            words += ones[num // 100] + " hundred "
            num %= 100  # Remove the hundreds portion

        # Handle numbers from 20 to 99
        if num >= 20:
            words += tens[num // 10] + " "
            num %= 10  # Remove the tens portion

        # Handle numbers from 10 to 19 (teens)
        elif num >= 10:
            # Teens are irregular in English and must be handled explicitly
            return words + teens[num - 10] + " "

        # Handle the ones place (1–9)
        if num > 0:
            words += ones[num] + " "

        return words

    # This string will accumulate the final result
    result = ""

    # Keeps track of which scale we are currently processing
    scale_index = 0

    # Process the number three digits at a time
    # Example: 1,234,567,890 -> [890] [567] [234] [1]
    while n > 0:
        chunk = n % 1000

        # Skip empty chunks to avoid phrases like "zero million"
        if chunk != 0:
            result = (
                process_chunk(chunk)
                + scales[scale_index]
                + " "
                + result
            )

        # Move to the next group of three digits
        n //= 1000
        scale_index += 1

    # Clean up any leading/trailing spaces before returning
    return result.strip()
