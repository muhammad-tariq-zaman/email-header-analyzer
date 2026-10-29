# email-header-analyzer

Parse an email message file and report its From / Subject / Date plus
every `Received` hop, in header order, so a support engineer can trace
the path a message took.

## How to run

```bash
python3 main.py message.eml
```

## Example output

```text
From: alice@example.com
Subject: Test
Date: Mon, 26 Oct 2026 10:00:00 +0500
Received hops: 2
  hop 1: from mail-a.example.com by mail-b.example.com
  hop 2: from laptop.local by mail-a.example.com
```

Standard library only. No network access.
