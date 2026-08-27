import asyncio
import time

from http.requests_client import fetch_page
from http.httpx_client import async_fetch_many


URLS = [
    "https://remotive.com/remote-jobs/data/data-labeling-specialists-2090903",
    "https://remotive.com/remote-jobs/all-others/vice-president-technology-digital-strategy-2091104",
    "https://remotive.com/remote-jobs/information-technology/tier-iii-service-desk-engineer-2091045",
]


def fetch_sequential(urls: list[str]) -> list[dict]:
    """
    Fetch URLs sequentially using the synchronous requests client.
    """

    results = []

    for url in urls:
        result = fetch_page(url)
        results.append(result)

    return results


async def fetch_concurrent(urls: list[str]) -> list[dict]:
    """
    Fetch URLs concurrently using httpx and asyncio.
    """

    return await async_fetch_many(urls)


def calculate_improvement(
    sequential_time: float,
    async_time: float
) -> float:
    """
    Calculate percentage improvement of async execution.
    """

    if sequential_time == 0:
        return 0.0

    return (
        (sequential_time - async_time)
        / sequential_time
    ) * 100


async def main():

    print(f"Number of URLs: {len(URLS)}")
    print()

    # -------------------------
    # Sequential benchmark
    # -------------------------

    start = time.perf_counter()

    sequential_results = fetch_sequential(URLS)

    sequential_time = time.perf_counter() - start

    # -------------------------
    # Async benchmark
    # -------------------------

    start = time.perf_counter()

    async_results = await fetch_concurrent(URLS)

    async_time = time.perf_counter() - start

    # -------------------------
    # Calculate improvement
    # -------------------------

    improvement = calculate_improvement(
        sequential_time,
        async_time
    )

    # -------------------------
    # Print benchmark
    # -------------------------

    print(
        f"Sequential execution : "
        f"{sequential_time:.2f} seconds"
    )

    print(
        f"Async execution      : "
        f"{async_time:.2f} seconds"
    )

    print(
        f"Improvement           : "
        f"{improvement:.2f}%"
    )

    # -------------------------
    # Print result summary
    # -------------------------

    print()
    print("Sequential results:")

    for result in sequential_results:
        print(
            result["status"],
            result.get("status_code"),
            result["url"]
        )

    print()
    print("Async results:")

    for result in async_results:
        print(
            result["status"],
            result.get("status_code"),
            result["url"]
        )


if __name__ == "__main__":
    asyncio.run(main())