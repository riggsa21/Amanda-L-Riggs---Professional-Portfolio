#!/usr/bin/env python3
"""GeoSite Intel: synthetic sample-order CSV validation demo.
Run `python process_demo_orders.py` in the folder containing sample_orders.csv.
No customer information is real. Original input is never overwritten.
"""
from pathlib import Path
from datetime import date
from collections import defaultdict
import csv

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "sample_orders.csv"
CLEAN = ROOT / "clean_orders.csv"
REVIEW = ROOT / "review_required.csv"
SUMMARY = ROOT / "customer_summary.csv"

clean, review, totals = [], [], defaultdict(float)
seen_ids = set()
with SOURCE.open(newline="", encoding="utf-8") as stream:
    reader = csv.DictReader(stream)
    for line_number, row in enumerate(reader, start=2):
        issues = []
        order_id = row["order_id"].strip()
        customer = row["customer"].strip()
        if not order_id:
            issues.append("Missing order ID")
        elif order_id in seen_ids:
            issues.append("Duplicate order ID")
        if order_id:
            seen_ids.add(order_id)
        try:
            date.fromisoformat(row["date"].strip())
        except ValueError:
            issues.append("Invalid date")
        try:
            amount = float(row["amount"].strip())
            if amount < 0:
                issues.append("Negative amount")
        except ValueError:
            amount = None
            issues.append("Invalid amount")
        if row["status"].strip().lower() not in {"pending", "shipped"}:
            issues.append("Invalid status")
        if not customer:
            issues.append("Missing customer")
        if issues:
            review.append({**row, "line_number": line_number, "issues": "; ".join(issues)})
        else:
            clean.append(row)
            totals[customer] += amount

def write_csv(path, fieldnames, entries):
    with path.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(entries)

fields = ["order_id", "customer", "date", "amount", "status"]
write_csv(CLEAN, fields, clean)
write_csv(REVIEW, fields + ["line_number", "issues"], review)
write_csv(SUMMARY, ["customer", "total_amount"], [
    {"customer": customer, "total_amount": f"{amount:.2f}"}
    for customer, amount in sorted(totals.items())
])
print(f"Input: {len(clean) + len(review)} rows | clean: {len(clean)} | review: {len(review)}")
print("Files written:", CLEAN.name, REVIEW.name, SUMMARY.name)
