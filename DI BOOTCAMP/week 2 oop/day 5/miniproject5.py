#!/usr/bin/env python3
"""
WebPageLoader - Measures webpage load times using requests and time modules.
Demonstrates OOP principles: encapsulation and abstraction.
"""

import requests
import time


class WebPageLoader:
    """
    A class to measure webpage load times using requests and time modules.
    Demonstrates OOP principles: encapsulation and abstraction.
    """

    def __init__(self, timeout=30):
        """
        Initialize the WebPageLoader with default timeout.

        Args:
            timeout (int): Maximum time to wait for response in seconds
        """
        self.timeout = timeout
        self.results = []

    def measure_load_time(self, url):
        """
        Measure how long it takes to get a complete response from a URL.

        Args:
            url (str): The webpage URL to test

        Returns:
            dict: Contains url, load_time, status_code, and success status
        """
        start_time = None
        try:
            # Record start time
            start_time = time.time()

            # Make the HTTP request with timeout
            response = requests.get(url, timeout=self.timeout)

            # Record end time after complete response received
            end_time = time.time()

            # Calculate total time
            load_time = end_time - start_time

            result = {
                'url': url,
                'load_time': round(load_time, 4),
                'status_code': response.status_code,
                'success': True,
                'content_length': len(response.content)
            }

            self.results.append(result)
            return result

        except requests.exceptions.RequestException as e:
            # Handle connection errors, timeouts, etc.
            end_time = time.time()
            load_time = end_time - start_time if start_time else 0

            result = {
                'url': url,
                'load_time': None,
                'status_code': None,
                'success': False,
                'error': str(e)
            }

            self.results.append(result)
            return result

    def test_multiple_sites(self, urls):
        """
        Test load times for multiple websites.

        Args:
            urls (list): List of URLs to test

        Returns:
            list: Results for all tested sites
        """
        print("=" * 60)
        print("WEBPAGE LOAD TIME TESTER")
        print("=" * 60)

        for url in urls:
            print(f"\nTesting: {url}")
            result = self.measure_load_time(url)

            if result['success']:
                print(f"   Status: {result['status_code']}")
                print(f"   Load Time: {result['load_time']:.4f} seconds")
                print(f"   Content Size: {result['content_length']:,} bytes")
            else:
                print(f"   Error: {result['error']}")

        return self.results

    def get_summary(self):
        """Return a summary of all tests performed."""
        if not self.results:
            return "No tests performed yet."

        successful = [r for r in self.results if r['success']]
        failed = [r for r in self.results if not r['success']]

        summary = {
            'total_tests': len(self.results),
            'successful': len(successful),
                       'failed': len(failed),
            'average_load_time': sum(r['load_time'] for r in successful) / len(successful) if successful else 0
        }

        return summary


# ============== DEMONSTRATION ==============

if __name__ == "__main__":

    # Create loader instance
    loader = WebPageLoader(timeout=30)

    # List of sites to test
    test_sites = [
        "https://www.google.com",
        "https://www.ynet.co.il",
        "https://www.imdb.com",
        "https://www.github.com",
        "https://www.stackoverflow.com",
        "https://www.wikipedia.org"
    ]

    # Run tests
    results = loader.test_multiple_sites(test_sites)

    # Print summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    summary = loader.get_summary()
    print(f"Total Tests: {summary['total_tests']}")
    print(f"Successful: {summary['successful']}")
    print(f"Failed: {summary['failed']}")
    print(f"Average Load Time: {summary['average_load_time']:.4f} seconds")

    # Detailed results table
    print("\n" + "=" * 60)
    print("DETAILED RESULTS")
    print("=" * 60)
    print(f"{'URL':<30} {'Status':<10} {'Load Time (s)':<15}")
    print("-" * 60)

    for result in results:
        url_short = result['url'].replace('https://', '')[:28]
        if result['success']:
            print(f"{url_short:<30} {result['status_code']:<10} {result['load_time']:<15.4f}")
        else:
            print(f"{url_short:<30} {'ERROR':<10} {'N/A':<15}")