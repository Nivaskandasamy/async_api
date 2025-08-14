# Import necessary modules from FastAPI and other libraries
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import asyncio
import time

# Create a FastAPI application instance
app = FastAPI()

# Define a Pydantic model for request body if using POST,
# but for GET, query parameters are simpler.
# Leaving this here for demonstration if the user decides to switch to POST later.
# class SumRequest(BaseModel):
#     num1: float
#     num2: float

@app.get('/sum')
async def sum_numbers(num1: float, num2: float):
    """
    API endpoint to sum two numbers using FastAPI.
    Takes 'num1' and 'num2' as query parameters.
    Returns their sum as a JSON response.
    """
    try:
        # Simulate some asynchronous work (e.g., I/O operation)
        # This makes the endpoint an awaitable coroutine, suitable for asyncio tests
        await asyncio.sleep(5) # Increased delay to 5 seconds to simulate async operation

        # Calculate the sum
        result = num1 + num2

        # Log the operation for demonstration purposes
        print(f"Received: num1 = {num1}, num2 = {num2}, Calculated Sum: {result}")

        # Return the sum as a JSON response. FastAPI automatically handles JSON serialization.
        return {"sum": result}
    except Exception as e:
        # FastAPI handles validation of num1 and num2 automatically via type hints
        # so TypeError/ValueError are typically converted to 422 Unprocessable Entity
        # However, a general exception handler is still good practice for unexpected issues.
        print(f"An unexpected error occurred: {e}")
        raise HTTPException(status_code=500, detail="An internal server error occurred.")