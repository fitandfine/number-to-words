# Number to Words API (FastAPI)
![Tests](https://github.com/fitandfine/number-to-words/actions/workflows/tests.yml/badge.svg)


A beginner-friendly yet production-structured Python project that converts numbers into their English word representation using a REST API built with **FastAPI**.

This project is designed as a **learning-first API** to understand:
- How APIs work internally
- How FastAPI is structured
- How to write clean business logic
- How to test APIs properly
- How to document and showcase an API project on GitHub

---

##  Features

- Converts integers into English words  
  - Example: `1_000_001 → "one million one"`
- Supports numbers **up to trillions**
- Clean separation of logic and API layer
- Fully unit-tested using `pytest`
- Beginner-readable code with detailed comments

---

##  Project Motivation

I had previously **used APIs** but never built one from scratch.  
This project was created to deeply understand:
- API request/response flow
- Input validation
- Modular Python design
- Testing and automation
- Real-world FastAPI structure

This repository is intentionally written in a **clear and explainable style**, so that other learners can also benefit from it.

---

##  Project Structure

```text
number-to-words/
├── ntow/                # Core application package
│   ├── __init__.py
│   ├── logic.py        # Number-to-words conversion logic
│   └── main.py         # FastAPI application
├── tests/              # Unit tests
│   ├── __init__.py
│   └── test_logic.py
├── requirements.txt
├── README.md
```

## Tech Stack

- Python 3.12

- FastAPI

- Uvicorn

- Pytest

## Installation & Setup

1) Clone the repository
```bash
git clone https://github.com/fitandfine/number-to-words.git
cd number-to-words
```
2) Create a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```
3) Install dependencies
```bash
pip install -r requirements.txt
```

## Running the API
Start the FastAPI server:
```bash
uvicorn ntow.main:app --reload
```
API will be available at:
```bash
http://127.0.0.1:8000
# This will display the health of the API as written in the default route
```
Interactive Swagger UI:
```bash
http://127.0.0.1:8000/docs
```

## Core Logic Explanation
- Numbers are split into chunks of three digits

- Each chunk is converted independently

- Scale names (thousand, million, billion, trillion) are applied

- Zero chunks are skipped to avoid invalid phrases

This mirrors how numbers are spoken in real English.


## Continuous Integration (CI)

This repository uses GitHub Actions to automatically:

- Install dependencies

- Run unit tests on every push or pull request

This ensures code quality and prevents regressions.