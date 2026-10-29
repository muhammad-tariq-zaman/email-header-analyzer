"""Analyse email headers: list Received hops and basic fields.

Usage: python3 main.py message.eml
"""
import argparse
import re
import sys
from email import policy
from email.parser import Parser


def analyse_headers(text):
    """Return a dict of From/Subject/Date plus ordered Received hops."""
    msg = Parser(policy=policy.default).parsestr(text)
    hops = []
    for received in msg.get_all("Received", []):
        by_match = re.search(r"\bby\s+(\S+)", str(received))
        from_match = re.search(r"\bfrom\s+(\S+)", str(received))
        hops.append({
            "from": from_match.group(1) if from_match else None,
            "by": by_match.group(1) if by_match else None,
        })
    return {
        "from": str(msg["From"]) if msg["From"] else None,
        "subject": str(msg["Subject"]) if msg["Subject"] else None,
        "date": str(msg["Date"]) if msg["Date"] else None,
        "hop_count": len(hops),
        "hops": hops,
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", help="Path to an .eml / message file")
    args = parser.parse_args(argv)
    with open(args.path, encoding="utf-8") as f:
        result = analyse_headers(f.read())
    print(f"From: {result['from']}")
    print(f"Subject: {result['subject']}")
    print(f"Date: {result['date']}")
    print(f"Received hops: {result['hop_count']}")
    for i, hop in enumerate(result["hops"], 1):
        print(f"  hop {i}: from {hop['from']} by {hop['by']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
