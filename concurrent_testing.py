import asyncio
import aiohttp # Asynchronous HTTP client library
import time

async def fetch_sum(session, num1, num2):
    """
    Asynchronously fetches the sum from the FastAPI endpoint.
    """
    url = f"http://127.0.0.1:5000/sum?num1={num1}&num2={num2}"
    async with session.get(url) as response:
        # Raise an exception for bad status codes (4xx or 5xx)
        response.raise_for_status()
        data = await response.json()
        # Log which request completed and its result
        print(f"Request: num1={num1}, num2={num2} -> Response: {data['sum']}")
        return data
    

async def main():
    """
    Main function to run concurrent API calls to the FastAPI endpoint.
    """
    start_time = time.time()
    # Create an aiohttp ClientSession to manage connections efficiently
    async with aiohttp.ClientSession() as session:
        tasks = []
        # Create multiple asynchronous tasks
        print("Creating 10 concurrent requests to the FastAPI /sum endpoint...")
        for i in range(1, 11): # Sending 10 concurrent requests
            tasks.append(fetch_sum(session, i, i * 2))

        # Run all tasks concurrently and wait for them to complete
        # asyncio.gather will run them in parallel (asynchronously)
        await asyncio.gather(*tasks)

    end_time = time.time()
    print(f"\nAll 10 requests completed in {end_time - start_time:.4f} seconds.")
    print("Due to the 5-second sleep in the FastAPI endpoint, you'll notice")
    print("the total time is slightly over 5 seconds, demonstrating concurrency.")
    print("If requests were sequential, it would take ~50 seconds (10 * 5s).")

if __name__ == "__main__":
    # Ensure aiohttp is installed: pip install aiohttp
    print("Starting asyncio concurrency test against FastAPI...")
    asyncio.run(main())