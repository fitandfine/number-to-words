from fastapi import FastAPI, HTTPException, Query
from .logic import number_to_words

app = FastAPI()

@app.get("/")
def health_check():
    # Just a simple route to see if the server is alive
    return {"status": "online", "message": "Number to Words API is running"}

# route to accept number as query parameter and return its word representation
@app.get("/convert")
def convert(number: int = Query(..., description="The number you want to turn into words")):
    # Basic validation: let's keep it to positive numbers for now
    if number < 0:
        raise HTTPException(status_code=400, detail="Please provide a positive integer.")
    
    if number > 999_999_999_999_999:
        raise HTTPException(status_code=400, detail="Number too large. Please provide a number up to 999,999,999,999,999.")
    
    # Using our logic from logic.py
    words = number_to_words(number)
    
    return {
        "input": number,
        "output": words
    }

@app.get("/convert/{number}")
def convert(number: int):
    # Basic validation: let's keep it to positive numbers for now
    if number < 0:
        raise HTTPException(status_code=400, detail="Please provide a positive integer.")
    
    if number > 999_999_999_999_999:
        raise HTTPException(status_code=400, detail="Number too large. Please provide a number up to 999,999,999,999,999.")
    
    # Using our logic from logic.py
    words = number_to_words(number)
    
    return {
        "input": number,
        "output": words
    }


@app.get("/about")
def about():
    return {
        "name": "Number to Words API",
        "version": "1.0",
        "description": "A simple API to convert numbers into their English word representations. Works for positive integers, Upto 999,999,999,999,999.",
    }