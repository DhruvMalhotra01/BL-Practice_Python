import asyncio

from crawler import crawl_page

async def main():

    url = (
         "https://remotive.com/remote-jobs/"
        "information-technology/"
        "tier-iii-service-desk-engineer-2091045"
    )

    result  = await crawl_page(url)

    print("Result type:", type(result))

    print("\nMarkdown:")
    print(result.markdown[:1000])

    print("\nHTML available:")
    print(result.html is not None)

    print("\nLLinks:")
    print(result.links)

    print("\nMetadata:")
    print("result.metadata")

if __name__ == "__main__":
    asyncio.run(main())