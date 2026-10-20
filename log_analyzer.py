"""Analyze synthetic Windows logon events exported as CSV."""
import argparse
import csv
from collections import Counter
from pathlib import Path

VALID_IDS = {"4624", "4625"}


def analyze(path: Path) -> Counter:
    counts = Counter()
    with path.open(newline="", encoding="utf-8-sig") as stream:
        reader = csv.DictReader(stream)
        if not reader.fieldnames or "EventID" not in reader.fieldnames:
            raise ValueError("CSV must include an EventID column")
        for row in reader:
            event_id = (row.get("EventID") or "").strip()
            if event_id in VALID_IDS:
                counts[event_id] += 1
    return counts


def main() -> None:
    parser = argparse.ArgumentParser(description="Summarize Windows logon event IDs from a CSV file")
    parser.add_argument("file", nargs="?", default="sample_events.csv", help="CSV input file")
    parser.add_argument("--threshold", type=int, default=3, help="Failed-logon alert threshold (default: 3)")
    args = parser.parse_args()
    if args.threshold < 1:
        parser.error("--threshold must be at least 1")
    try:
        counts = analyze(Path(args.file))
    except (OSError, ValueError, csv.Error) as error:
        parser.exit(1, f"Error: {error}\n")
    print("Windows Security Log Analysis")
    print("-----------------------------")
    print(f"Successful logons (4624): {counts['4624']}")
    print(f"Failed logons (4625): {counts['4625']}")
    if counts["4625"] >= args.threshold:
        print("Alert: Failed logon count reached the configured threshold.")
    else:
        print("Failed logon count below configured threshold.")
    print("Note: This is a simple count, not evidence of an attack.")


if __name__ == "__main__":
    main()
