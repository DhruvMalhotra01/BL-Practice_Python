import httpx

async def async_fetch(url: str) -> dict:# this is function is a coroutine that can perform asynchronous operations
    """
    Fetch a web page asynchronously using httpx.AsyncClient.


    Returns:
        dict containing URL, status, status_code,
        headers and content.
    """

    try:
        async with httpx.AsyncClient() as client:#create an asynchronous HTTP client
            # async with ensure that http client is properly opened and closed 

            response = await client.get(
                url,
                timeout=10
            )

            response.raise_for_status()

            return{
                "url": url,
                "status" : "success",
                "status_code" : response.status_code,
                "header" : dict(response.headers),
                "content" : response.text
            }
    except httpx.TimeoutException:
        return{
            "url" : url,
            "status" : "failed",
            "status_code" : None,
            "error" :"Request timed out"
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
        