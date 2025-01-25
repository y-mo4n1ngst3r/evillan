"""
Advanced Payload Encoder with CVE Support
=========================================

This package provides utilities for generating, encoding, and testing payloads 
for web application penetration testing. It supports multiple encoding methods, 
CVE payload fetching, and live testing on target endpoints.

Modules:
- cli: The entry point for the CLI.
- encoder: Contains encoding logic and advanced mixing algorithms.
- ascii: Handles ASCII art and blinking effects.
- cve_fetcher: Fetches CVE payloads from external sources.
- tester: Provides live testing functionality.
- utils: Contains utility functions (e.g., clear screen, color codes).
"""

__version__ = "1.0.0"
__author__ = "y_mo4n1ngst3r"
__license__ = "MIT"

# Convenience imports
from .encoder import encode_payloads
from .ascii import print_blinking_ascii
from .cve_fetcher import fetch_cve_payloads
from .tester import test_payloads
from .utils import clear_screen
