import asyncio
import os

from dotenv import load_dotenv
from google import genai


async def main():
    load_dotenv()
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY")).aio

    async for chunk in await client.models.generate_content_stream(
        model="gemini-3.1-flash-lite-preview",
        contents="Tell me a story in 300 words about the python programming language",
    ):
        print(chunk.text, end="")


if __name__ == "__main__":
    asyncio.run(main())
