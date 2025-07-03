#!/usr/bin/env python3

import csv
import sys
import os
import argparse

def wide_to_long(input_csv, output_csv=None):
    if output_csv is None:
        base, _ = os.path.splitext(input_csv)
        output_csv = base + "_long.csv"

    with open(input_csv, newline='') as infile, open(output_csv, 'w', newline='') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = ['domain', 'record_type', 'target']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            domain = row['domain']
            for rtype in row:
                if rtype.lower() == 'domain':
                    continue
                target = row[rtype].strip()
                if target:
                    writer.writerow({
                        'domain': domain,
                        'record_type': rtype.upper(),
                        'target': target
                    })

    print(f"✅ Converted: {input_csv} → {output_csv}")

def main():
    parser = argparse.ArgumentParser(
        description="Convert wide DNS CSV (one row per domain) to long form (one row per record)."
    )
    parser.add_argument("input_csv", help="Input wide CSV file")
    parser.add_argument("output_csv", nargs="?", help="Output long CSV file (optional)")

    args = parser.parse_args()

    wide_to_long(args.input_csv, args.output_csv)

if __name__ == "__main__":
    main()
