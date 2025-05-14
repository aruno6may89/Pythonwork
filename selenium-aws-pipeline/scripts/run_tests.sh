#!/bin/bash

# Navigate to the project directory
cd "$(dirname "$0")/../.."

# Install dependencies
pip install -r requirements.txt

# Run the tests
pytest tests/ --maxfail=1 --disable-warnings -q

# Exit with the status of the test run
exit $?