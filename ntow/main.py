from fastapi import FastAPI, HTTPException, Query
from .logic import number_to_words

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