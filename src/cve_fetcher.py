import requests

def fetch_cve_payloads():
    """Fetch payloads from PayloadsAllTheThings."""
    url = "https://raw.githubusercontent.com/swisskyrepo/PayloadsAllTheThings/master/README.md"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return [line.strip() for line in response.text.splitlines() if "payload" in line.lower()]
    except Exception as e:
        print(f"Failed to fetch payloads: {e}")
    return []
