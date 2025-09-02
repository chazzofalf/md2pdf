# md2pdf

A simple utility to convert Markdown files to PDF using a Python script and a Bash wrapper that activates a virtual environment.

## Repository

[https://github.com/chazzofalf/md2pdf](https://github.com/chazzofalf/md2pdf)

## Overview

- **`md2pdf.py`** – Python script that converts a Markdown file to PDF using `markdown` and `weasyprint`.
- **`md2pdf.sh`** – Bash wrapper that activates the project's virtual environment (`.venv`) and forwards all arguments to `md2pdf.py`. It resolves the real script location, so it works correctly even when invoked via a symbolic link.
- **Virtual environment** – All required Python packages are listed in `requirements.txt`.

## Installation

```bash
# Clone the repository
git clone https://github.com/chazzofalf/md2pdf.git
cd md2pdf

# Create a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Make the wrapper executable
chmod +x md2pdf.sh
```

## Usage

```bash
# Convert a markdown file to PDF
./md2pdf.sh path/to/file.md
```

The output PDF will be saved next to the input file with the same base name and a `.pdf` extension.

### Using the wrapper through a symbolic link

```bash
# Create a symlink in another project
ln -s /full/path/to/md2pdf/md2pdf.sh ./md2pdf.sh

# Run it from the other project directory
./md2pdf.sh other_project_file.md
```

The wrapper will still locate the original virtual environment and perform the conversion.

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.
