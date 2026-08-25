import asyncio

from httpx_client import async_fetch

async def main():
    url = (
        "https://remotive.com/"
        "remote-jobs/information-technology/"
        "tier-iii-service-desk-engineer-2091045"
    )

    result = await async_fetch(url)

    print("Status:",result["status"])
    print("Status Code:",result["status_code"])
    print("Error:",result.get("error",""))

if __name__ == "__main__":
    asyncio.run(main())