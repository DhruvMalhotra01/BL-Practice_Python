import asyncio

from httpx_client import async_fetch_many

async def main():
    urls = [
        "https://remotive.com/remote-jobs/data/data-labeling-specialists-2090903",
        "https://remotive.com/remote-jobs/all-others/vice-president-technology-digital-strategy-2091104",
        "https://remotive.com/remote-jobs/information-technology/tier-iii-service-desk-engineer-2091045",
    ]

    results = await async_fetch_many(urls)

    for result in results:
        print("=" * 60)
        print("URL:", result["url"])
        print("Status:", result.get("status"))
        print("Status Code:", result.get("status_code"))
        print("Error:", result.get("error", ""))

if __name__ == "__main__":
    asyncio.run(main())