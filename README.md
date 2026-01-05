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

# Usage
```bash
GET /convert?number=565 # using query parameter
GET /convert/565 # using path parameter
```
```bash
# Example:
http://127.0.0.1/convert?number=565
http://127.0.0.1/convert/565
```

## Further Development

This project is functional and well-tested, but there are several opportunities for enhancement to make it even more robust, scalable, and production-ready:

1. **Containerization with Docker**
   - Package the API and all dependencies in a Docker container.
   - Ensures environment consistency across different machines and servers.
   - Simplifies deployment to cloud platforms or production servers.

2. **API Endpoint Testing**
   - Extend automated testing to include all endpoints using `FastAPI TestClient`.
   - Validate input, output, and error handling programmatically.
   - Integrate with GitHub Actions CI/CD for automatic testing on every push or pull request.

3. **Path Parameter Support**
   - Modify `/convert` endpoint to accept numbers as path parameters (e.g., `/convert/12345`) for a more RESTful API design.

4. **Support for Negative Numbers and Decimals**
   - Extend conversion logic to handle negative integers and fractional numbers.
   - Could add options like “currency” or “ordinal numbers” (e.g., `1st`, `2nd`).

5. **Localization / Multi-Language Support**
   - Add support for converting numbers into words in other languages.
   - Could be implemented with a language parameter (`/convert?number=123&lang=fr`).

6. **Dockerized Testing and CI/CD**
   - Run all unit and API tests inside a container to ensure the container works correctly.
   - Automate the CI/CD pipeline to build, test, and deploy Docker images.

7. **Error Logging & Monitoring**
   - Add proper error logging using tools like **Sentry** or **logging module**.
   - Monitor API usage and detect potential issues in production.

8. **Deployment**
   - Deploy the API to cloud platforms such as AWS, GCP, or Azure.
   - Add HTTPS support and domain routing for production readiness.

9. **Rate Limiting / Security**
   - Implement request throttling to prevent abuse.
   - Add API key authentication or JWT tokens for secure usage.

---
## Thank You for your time in reading this far!
Anup