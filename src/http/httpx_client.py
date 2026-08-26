import asyncio
import httpx


async def async_fetch(
    url: str,
    client: httpx.AsyncClient
) -> dict:
    """
    Fetch a web page asynchronously using httpx.AsyncClient.

    Returns:
        dict containing URL, status, status_code,
        headers and content.
    """

    try:
        response = await client.get(
            url,
            timeout=10
        )

        response.raise_for_status()

        return {
            "url": url,
            "status": "success",
            "status_code": response.status_code,
            "headers": dict(response.headers),
            "content": response.text
        }

    except httpx.TimeoutException:
        return {
            "url": url,
            "status": "failed",
            "status_code": None,
            "error": "Request timed out"
        }

    except httpx.ConnectError:
        return {
            "url": url,
            "status": "failed",
            "status_code": None,
            "error": "Connection failed"
        }

    except httpx.HTTPStatusError as error:
        return {
            "url": url,
            "status": "failed",
            "status_code": error.response.status_code,
            "error": str(error)
        }

    except httpx.RequestError as error:
        return {
            "url": url,
            "status": "failed",
            "status_code": None,
            "error": str(error)
        }


async def async_fetch_many(urls: list[str]) -> list[dict]:
    """
    Fetch multiple URLs concurrently.
    """

    async with httpx.AsyncClient() as client:

        tasks = [
            async_fetch(url, client)
            for url in urls
        ]

        results = await asyncio.gather(
            *tasks,
            return_exceptions=True
        )

        final_results = []

        for url, result in zip(urls, results):

            if isinstance(result, Exception):
                final_results.append({
                    "url": url,
                    "status": "failed",
                    "status_code": None,
                    "error": str(result)
                })

            else:
                final_results.append(result)

        return final_results