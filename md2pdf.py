#!/usr/bin/env python3
"""
md2pdf.py - Convert a Markdown file to PDF.

Usage:
    python md2pdf.py input.md [output.pdf]

If the output file is not specified, the PDF will be saved with the same
basename as the input file and a .pdf extension.
"""

import sys
import os
import pathlib
import argparse

try:
    import markdown
except ImportError:
    sys.stderr.write("Error: The 'markdown' package is required. Install with 'pip install markdown'.\n")
    sys.exit(1)

try:
    from weasyprint import HTML, CSS
except ImportError:
    sys.stderr.write("Error: The 'weasyprint' package is required. Install with 'pip install weasyprint'.\n")
    sys.exit(1)


def markdown_to_html(md_text: str) -> str:
    """
    Convert markdown text to HTML.
    """
    return markdown.markdown(
        md_text,
        extensions=[
            "extra",
            "codehilite",
            "toc",
            "tables",
            "sane_lists",
            "smarty",
        ],
    )


def html_to_pdf(html_content: str, output_path: pathlib.Path, base_url: str = None) -> None:
    """
    Render HTML content to a PDF file using WeasyPrint.
    """
    html = HTML(string=html_content, base_url=base_url)
    # Basic styling to improve PDF output
    default_css = CSS(string="""
        @page { size: A4; margin: 1in; }
        body { font-family: serif; line-height: 1.4; }
        h1, h2, h3, h4, h5, h6 { font-family: sans-serif; }
        code { background: #f5f5f5; padding: 2px 4px; border-radius: 3px; }
        pre { background: #f5f5f5; padding: 0.5em; overflow-x: auto; }
        table { border-collapse: collapse; width: 100%; }
        th, td { border: 1px solid #ddd; padding: 4px; }
        th { background: #f0f0f0; }
    """)
    html.write_pdf(target=str(output_path), stylesheets=[default_css])


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert Markdown to PDF.")
    parser.add_argument("input", type=pathlib.Path, help="Path to the input markdown file")
    parser.add_argument(
        "output",
        nargs="?",
        type=pathlib.Path,
        help="Path to the output PDF file (default: same name with .pdf)",
    )
    args = parser.parse_args()

    if not args.input.is_file():
        sys.stderr.write(f"Error: Input file '{args.input}' does not exist or is not a file.\n")
        sys.exit(1)

    output_path = args.output
    if output_path is None:
        output_path = args.input.with_suffix(".pdf")
    else:
        output_path = output_path.resolve()

    try:
        md_text = args.input.read_text(encoding="utf-8")
    except Exception as e:
        sys.stderr.write(f"Error reading '{args.input}': {e}\n")
        sys.exit(1)

    html = markdown_to_html(md_text)

    # Use the markdown file's directory as the base URL so relative resources resolve
    base_url = str(args.input.parent.resolve())

    try:
        html_to_pdf(html, output_path, base_url=base_url)
    except Exception as e:
        sys.stderr.write(f"Error generating PDF: {e}\n")
        sys.exit(1)

    print(f"PDF generated: {output_path}")


if __name__ == "__main__":
    main()

