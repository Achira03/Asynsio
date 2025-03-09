import asyncio
import aiohttp
import time

URLS = [
    "https://jsonplaceholder.typicode.com/todos/1",
    "https://jsonplaceholder.typicode.com/todos/2",
    "https://jsonplaceholder.typicode.com/todos/3",
    "https://jsonplaceholder.typicode.com/todos/4",
    "https://jsonplaceholder.typicode.com/todos/5",
]

async def fetch(session, url):
    start_time = time.time()
    async with session.get(url) as response:
        data = await response.json()
        elapsed_time = time.time() - start_time
        print(f"Fetched data from {url} in {elapsed_time:.2f} seconds: {data}")
        return data

async def process_data(data):
    await asyncio.sleep(1)  # Simulate data processing time
    print(f"Processed data: {data}")

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in URLS]
        results = await asyncio.gather(*tasks)
        
        process_tasks = [process_data(data) for data in results]
        await asyncio.gather(*process_tasks)

if __name__ == "__main__":
    asyncio.run(main())