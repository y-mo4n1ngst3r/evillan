import argparse
from ascii import print_blinking_ascii
from encoder import encode_payloads
from cve_fetcher import fetch_cve_payloads
from tester import test_payloads


def main():
    # Print blinking ASCII art at the start
    print_blinking_ascii()

    # Define the CLI interface
    parser = argparse.ArgumentParser(
        description="Advanced Mixed Payload Encoder with CVE Support",
        epilog="Author: y_morn1ngst3r",
    )
    parser.add_argument(
        "-i", "--input",
        type=str,
        help="Path to the text file containing payloads",
        required=True,
    )
    parser.add_argument(
        "-o", "--output",
        type=str,
        help="Path to save the encoded payloads",
        default="encoded_payloads.txt",
    )
    parser.add_argument(
        "-m", "--methods",
        type=str,
        nargs="+",
        help="Encoding methods to apply (e.g., base64, url, html)",
        required=True,
    )
    parser.add_argument(
        "-d", "--depth",
        type=int,
        help="Maximum number of encoding layers",
        default=3,
    )
    parser.add_argument(
        "-fc", "--fetch-cve",
        action="store_true",
        help="Fetch CVE payloads from external sources",
    )
    parser.add_argument(
        "-t", "--test",
        type=str,
        nargs="?",
        const="all",
        help="Test payloads on a target URL, Using -csrf, -xss, -sqli, ",
    )
    parser.add_argument(
        "-u", "--url",
        type=str,
        help="Target URL to test payloads (required for --test).",
    )
    parser.add_argument(
        "--format",
        type=str,
        choices=["txt", "json", "csv", "markdown"],
        help="Output format: txt (default), json, csv, markdown",
        default="txt",
    )
    parser.add_argument(
        "--version",
        action="version",
        version="Advanced Payload Encoder v1.0.0",
        help="Show the version of the tool.",
    )
    args = parser.parse_args()

    # Fetch payloads and encode them
    payloads = fetch_cve_payloads() if args.fetch_cve else []
    encoded_payloads = encode_payloads(
        args.input, args.methods, args.depth, payloads)
    payloads_for_testing = [payload for payload,
                            _ in encoded_payloads]  # Extract only payload

    # Save encoded payloads
    with open(args.output, "w") as file:
        for payload in encoded_payloads:
            file.write(payload + "\n")
    print(f"Encoded payloads saved to {args.output}")

    # Optionally test payloads
    if args.test:
        if not args.url:
            print("Error: --url is required when using --test.")
        else:
            test_payloads(args.url, args.test)


if __name__ == "__main__":
    main()
