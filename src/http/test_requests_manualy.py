from requests_client import fetch_page


urls = [
    "https://remotive.com/remote-jobs/data/data-labeling-specialists-2090903",

    "https://remotive.com/remote-jobs/all-others/vice-president-technology-digital-strategy-2091104",

    "https://remotive.com/remote-jobs/information-technology/tier-iii-service-desk-engineer-2091045",
]


for url in urls:

    print("=" * 60)
    print("URL:", url)

    result = fetch_page(url)

    print("Status:", result["status"])
    print("Status Code:", result["status_code"])
    print("Error:", result.get("error", ""))