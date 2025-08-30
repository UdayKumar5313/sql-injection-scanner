# SQL Injection Vulnerability Scanner

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

A custom-built, automated vulnerability scanner written in Python. This tool is designed to detect basic SQL Injection (SQLi) vulnerabilities in web application forms. It was developed as a hands-on cybersecurity portfolio project to demonstrate practical skills in offensive security tool development.

This scanner is designed to be used against its companion project, the **[Secure Blog App](https://github.com/UdayKumar5313/secure-blog-app)**, which contains both a vulnerable and a patched version of the code.

## Features
- Crawls a target URL to discover all web forms.
- Submits a classic SQLi payload (`'`) to each discovered form to trigger a database error.
- Analyzes the server's HTTP response code to identify anomalies (specifically, a `500 Internal Server Error`) that indicate a successful injection.
- Reports the vulnerable form's details upon successful detection.

## Skills Demonstrated
* **Programming:** Python
* **Libraries:** Requests (for HTTP requests), BeautifulSoup4 (for HTML parsing)
* **Cybersecurity Concepts:** OWASP Top 10, SQL Injection (SQLi), Vulnerability Scanning, Black-Box Testing
* **Tools:** Git, GitHub, Virtual Environments (venv)

## How to Use

### Prerequisites
* Python 3.7+
* Git

### Setup & Installation
1.  Clone the repository:
    ```sh
    git clone [https://github.com/UdayKumar5313/sql-injection-scanner.git](https://github.com/UdayKumar5313/sql-injection-scanner.git)
    cd sql-injection-scanner
    ```
2.  Create and activate a virtual environment:
    ```sh
    # For Windows
    python -m venv venv
    .\venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```
3.  Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```
    *(Note: You will need to create a `requirements.txt` file with the content `requests` and `beautifulsoup4`.)*

### Execution
1.  First, get the target web application ([Secure Blog App](https://github.com/UdayKumar5313/secure-blog-app)) running on `http://127.0.0.1:5000`.
2.  Run the scanner from its own terminal:
    ```sh
    python scanner.py
    ```

## Example Output
When a vulnerability is found, the scanner will produce the following output:
