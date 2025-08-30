# scanner.py

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_forms(url):
    """Extracts all HTML forms from a given URL."""
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup.find_all('form')
    except requests.exceptions.RequestException as e:
        print(f"[-] Could not connect to {url}. Error: {e}")
        return []

def submit_form(form, url, value):
    """Submits a form with a given value."""
    action = form.get('action')
    post_url = urljoin(url, action)
    method = form.get('method', 'get').lower()

    inputs_list = form.find_all(['input', 'textarea'])
    data = {}
    for input_tag in inputs_list:
        input_name = input_tag.get('name')
        input_type = input_tag.get('type', 'text')
        if input_name:
            if input_type == 'text':
                data[input_name] = value
            
    try:
        if method == 'post':
            return requests.post(post_url, data=data, timeout=5)
        else:
            return requests.get(post_url, params=data, timeout=5)
    except requests.exceptions.RequestException as e:
        print(f"[-] Form submission failed. Error: {e}")
        return None

def scan_sql_injection(url):
    """Scans a URL for SQL Injection vulnerabilities."""
    print(f"\n[+] Scanning {url} for SQL Injection...")
    forms = get_forms(url)
    if not forms:
        print("[i] No forms found on the page.")
        return

    sql_injection_payload = "'"
    vulnerability_fingerprint = "VULNERABILITY DETECTED"

    for form in forms:
        response = submit_form(form, url, sql_injection_payload)

        # New check: Look for our custom fingerprint in the page text
        if response and vulnerability_fingerprint in response.text:
            print(f"[!!] SQL Injection vulnerability discovered in a form on {url}")
            print("[*] Form Details:")
            print(form)
            return True

    print("[i] No SQL Injection vulnerabilities found.")
    return False

if __name__ == "__main__":
    target_url = "http://127.0.0.1:5000"
    scan_sql_injection(target_url)