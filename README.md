# async-api

A simple demonstration of asynchronous API development and concurrent client testing using FastAPI and aiohttp.

## Overview

This project provides:

- A FastAPI server exposing an endpoint `/sum` that asynchronously adds two numbers.
- A Python script to test the endpoint with multiple concurrent requests using asyncio and aiohttp, showcasing the benefits of asynchronous programming.

## Folder Structure

```
.
├── .gitignore
├── .python-version
├── concurrent_testing.py   # Script for concurrent async API testing
├── main.py                # FastAPI server with /sum endpoint
├── pyproject.toml
├── README.md
├── uv.lock
└── __pycache__/
```

## API Endpoint

- **URL:** `/sum`
- **Method:** GET
- **Query Parameters:**
  - `num1` (float): First number
  - `num2` (float): Second number
- **Response:** JSON object with the sum, e.g. `{ "sum": 3.0 }`
- **Note:** The endpoint simulates a 5-second asynchronous delay.

## Running the FastAPI Server

1. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```
    Or use the dependencies listed in [pyproject.toml](pyproject.toml).

2. Start the server:
    ```sh
    uvicorn main:app --host 127.0.0.1 --port 5000
    ```

## Concurrent Testing

To test the endpoint with 10 concurrent requests:

```sh
python concurrent_testing.py
```

- The script will send 10 simultaneous requests to `/sum`.
- Demonstrates that all requests complete in just over 5 seconds (instead of 50 seconds if run sequentially).

## Requirements

- Python 3.12+
- FastAPI
- aiohttp
- uvicorn

## License

MIT License (add your license here if needed)
