from crawl4ai import AsyncWebCrawler

async def crawl_page(url: str):
    """
    Crawl a single webpage using Crawl4AI.
    """

    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(url)

        return result