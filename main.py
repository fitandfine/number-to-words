from fastapi import FastAPI, HTTPException, Query


app = FastAPI()

@app.get("/")
def health_check():
    # Just a simple route to see if the server is alive
    return {"status": "online", "message": "Number to Words API is running"}

@app.get("/convert")
def convert(number: int = Query(..., description="The number you want to turn into words")):
    # Basic validation: let's keep it to positive numbers for now
    if number < 0:
        raise HTTPException(status_code=400, detail="Please provide a positive integer.")
    
    # Using our logic from logic.py
    words = f"You have entered the number {number}. The conversion logic will be added here."  # Placeholder for actual conversion logic
    
    return {
        "input": number,
        "output": words
    }