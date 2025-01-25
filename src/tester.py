import os
import requests

# Define payload categories and corresponding file paths
PAYLOAD_FILES = {
    "csrf": "payloads/csrf.txt",
    "xss": "payloads/xss.txt",
    "sqli": "payloads/sqli.txt",
    "lfi": "payloads/lfi.txt",
    "ssrf": "payloads/ssrf.txt",
}

def load_payloads(category):
    """Load payloads from the file for a specific category."""
    file_path = PAYLOAD_FILES.get(category)
    if not file_path or not os.path.exists(file_path):
        print(f"Error: Payload file for {category} not found.")
        return []
    with open(file_path, "r") as file:
        return [line.strip() for line in file.readlines() if line.strip()]

def test_payloads(target_url, test_option):
    """
    Test payloads on a target URL.
    :param target_url: The URL to test payloads against.
    :param test_option: The specific category to test (e.g., csrf, xss).
    """
    print(f"Testing {len(payloads)} payloads on {target_url}...")
    
    for payload in payloads:
        try:
            response = requests.get(target_url, params={"q": payload}, timeout=5)
            print(f"Payload: {payload} | Status: {response.status_code}")
        except Exception as e:
            print(f"Payload: {payload} | Error: {str(e)}")
