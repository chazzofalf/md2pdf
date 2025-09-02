#!/usr/bin/env bash
# Wrapper script to activate the project's virtual environment and run md2pdf.py
# Works regardless of the current working directory from which the script is invoked.

# Resolve the directory where this script resides
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Path to the virtual environment
VENV_DIR="${SCRIPT_DIR}/.venv"

# Ensure the virtual environment exists
if [ ! -d "${VENV_DIR}" ]; then
  echo "Error: Virtual environment not found at ${VENV_DIR}"
  exit 1
fi

# Activate the virtual environment
# shellcheck disable=SC1091
source "${VENV_DIR}/bin/activate"

# Execute the Python script with any passed arguments
python "${SCRIPT_DIR}/md2pdf.py" "$@"
