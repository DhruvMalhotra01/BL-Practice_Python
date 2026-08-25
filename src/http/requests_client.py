import requests


def fetch_page(url: str) -> dict:
    """
    fetch a web page synchronously using requests.

    Returns:
        dict containing URL, status , status_code and content.
    """

    try:
        response = requests.get(
            url,
            timeout=10,
        )

        #Raise an exception for HTTP 4xx / 5xx
        response.raise_for_status()

        return {
            "url": url,
            "status": "success",
            "status_code": response.status_code,
            "content": response.text
        }

    except requests.exceptions.Timeout:
        return {
            "url": url,
            "status": "failed",
            "status_code": None,
            "error": "Request timed out"
        }

    except requests.exceptions.ConnectionError:
        return {
            "url": url,
            "status": "failed",
            "status_code": None,
            "error": "Connection failed"
        }

    except requests.exceptions.HTTPError as error:
        return {
            "url": url,
            "status": "failed",
            "status_code": error.response.status_code if error.response else None,
            "error": str(error)
        }

    except requests.exceptions.RequestException as error:
        return {
            "url": url,
            "status": "failed",
            "status_code": error.response.status_code if error.response else None,
            "error": str(error)
        }
