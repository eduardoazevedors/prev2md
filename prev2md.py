#!/usr/bin/env python3
"""
prev2md - Convert PDF files to Markdown using opendataloader-pdf.

Usage:
    python prev2md.py <pdf_file_or_dir> [<pdf_file_or_dir> ...] [-o OUTPUT_DIR] [--stdout]

Examples:
    python prev2md.py document.pdf
    python prev2md.py document.pdf -o output/
    python prev2md.py docs/ -o output/
    python prev2md.py document.pdf --stdout
"""

import argparse
import sys
from pathlib import Path

import opendataloader_pdf


def main():
    parser = argparse.ArgumentParser(
        prog="prev2md",
        description="Convert PDF files to Markdown using opendataloader-pdf.",
    )
    parser.add_argument(
        "input",
        nargs="+",
        help="PDF file(s) or directory containing PDFs",
    )
    parser.add_argument(
        "-o", "--output-dir",
        help="Output directory (default: same as input file directory)",
    )
    parser.add_argument(
        "--stdout",
        action="store_true",
        help="Write Markdown output to stdout instead of file",
    )
    parser.add_argument(
        "--pages",
        help='Pages to extract (e.g. "1,3,5-7")',
    )
    parser.add_argument(
        "--table-method",
        choices=["default", "cluster"],
        help="Table detection method (default: border-based, cluster: border + cluster)",
    )
    parser.add_argument(
        "-q", "--quiet",
        action="store_true",
        help="Suppress console logging output",
    )

    args = parser.parse_args()

    # Validate inputs exist
    for input_path in args.input:
        if not Path(input_path).exists():
            print(f"Error: '{input_path}' not found.", file=sys.stderr)
            sys.exit(1)

    opendataloader_pdf.convert(
        input_path=args.input if len(args.input) > 1 else args.input[0],
        output_dir=args.output_dir,
        format="markdown",
        quiet=args.quiet,
        pages=args.pages,
        table_method=args.table_method,
        to_stdout=args.stdout,
    )


if __name__ == "__main__":
    main()
