# evillan

A tool for create encoded payloads and test them on targets

Advanced Payload Encoder with CVE Support

A CLI tool for penetration testers and security researchers to generate advanced encoded payloads for testing web application vulnerabilities. This tool supports:

    Layered encoding using multiple methods.
    Dynamic CVE payload fetching from external sources.
    Live testing of payloads on target endpoints.

Features

    Multiple Encoding Methods:
        Supports encoding techniques like base64, url, html, rot13, reverse, unicode-escape, and more.
    Advanced Payload Mixing:
        Encodes payloads with layered encoding techniques for bypassing security filters.
    CVE Payload Fetching:
        Dynamically fetch payloads from sources like PayloadsAllTheThings.
    Live Testing:
        Send generated payloads to target URLs and analyze responses.
    User-Friendly CLI:
        Simple and flexible command-line interface.
Installation
Clone the Repository

git clone https://github.com/yourusername/advanced-payload-encoder.git
cd advanced-payload-encoder

Install Dependencies

Use pip to install the required dependencies:

pip install -r requirements.txt

Install the Tool Locally

You can install the tool as a Python package:

pip install -e .

Usage
Basic Command:

payload-encoder -i <input_file> -o <output_file> -m <methods> -d <depth>

Options
Option	Description
-i, --input	Path to the text file containing payloads (required).
-o, --output	Path to save the encoded payloads (default: encoded_payloads.txt).
-m, --methods	List of encoding methods to apply (e.g., base64, url, html).
-d, --depth	Maximum number of encoding layers (default: 3).
--fetch-cve	Fetch additional CVE payloads from external sources.
--test	Target URL to test the encoded payloads (e.g., http://example.com).

Examples:
Encode Payloads
payload-encoder -i payloads.txt -o encoded_payloads.txt -m base64 url html -d 3

This command:

    Reads payloads from payloads.txt.
    Encodes them with up to 3 layers of base64, url, and html encodings.
    Saves the output to encoded_payloads.txt.

Fetch CVE Payloads
payload-encoder --fetch-cve -i payloads.txt -o encoded_payloads.txt -m base64 url -d 2

This command:

    Fetches additional CVE payloads dynamically.
    Combines them with payloads from payloads.txt.
    Encodes them with up to 2 layers of base64 and url encodings.

Supported Encoding Methods

    base64: Encode payloads in Base64.
    url: URL-encode payloads.
    html: Escape HTML characters.
    rot13: Apply ROT13 cipher.
    reverse: Reverse the payload.
    unicode-escape: Encode payloads in Unicode escape sequences.
    ascii85: Encode payloads in Ascii85.
    zlib-base64: Compress payloads using zlib, then Base64 encode.
    sql-char: Convert payloads to SQL CHAR() format.

Features in Development

    Steganography Payloads: Hide payloads in images or files.
    WAF Evasion Techniques: Include advanced techniques to bypass web application firewalls.
    Custom Payload Templates: Allow users to define reusable payload patterns.

Contributing

Contributions are welcome! To contribute:

    Fork the repository.
    Create a new branch (git checkout -b feature/your-feature).
    Commit your changes (git commit -m "Add your feature").
    Push the branch (git push origin feature/your-feature).
    Open a pull request.

License

This project is licensed under the MIT License.

Acknowledgments

    Inspired by tools like PayloadsAllTheThings.
    Developed by y_mo4n1ngst3r






