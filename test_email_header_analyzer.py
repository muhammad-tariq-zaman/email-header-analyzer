import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unittest
from main import analyse_headers

SAMPLE = """From: alice@example.com
Subject: Test
Date: Mon, 26 Oct 2026 10:00:00 +0500
Received: from mail-a.example.com by mail-b.example.com
Received: from laptop.local by mail-a.example.com

Hello
"""


class TestEmailHeaders(unittest.TestCase):
    def test_fields(self):
        r = analyse_headers(SAMPLE)
        self.assertEqual(r["from"], "alice@example.com")
        self.assertEqual(r["subject"], "Test")

    def test_hop_count_and_order(self):
        r = analyse_headers(SAMPLE)
        self.assertEqual(r["hop_count"], 2)
        self.assertEqual(r["hops"][0]["from"], "mail-a.example.com")

    def test_no_received_headers(self):
        r = analyse_headers("From: a@b.com\nSubject: Hi\n\nBody\n")
        self.assertEqual(r["hop_count"], 0)


if __name__ == "__main__":
    unittest.main()
