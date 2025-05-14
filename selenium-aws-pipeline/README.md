# selenium-aws-pipeline

This project automates web interactions using Selenium in Python. It includes functionality for generating random usernames, logging into a website, creating SMS templates, and verifying their creation.

## Project Structure

```
selenium-aws-pipeline
├── src
│   └── SMS_template.py          # Main script for Selenium automation
├── tests
│   └── __init__.py              # Marks the tests directory as a Python package
├── requirements.txt              # Lists Python dependencies
├── buildspec.yml                 # AWS CodeBuild configuration
├── Dockerfile                     # Docker image build instructions
├── docker-compose.yml            # Multi-container Docker application configuration
└── scripts
    └── run_tests.sh             # Script to run tests
```

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd selenium-aws-pipeline
   ```

2. **Install dependencies:**
   Ensure you have Python and pip installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the main script:**
   Execute the Selenium script using:
   ```bash
   python src/SMS_template.py
   ```

4. **Run tests:**
   To execute the tests, run the following command:
   ```bash
   bash scripts/run_tests.sh
   ```

## AWS CI/CD Pipeline

This project is configured to run in an AWS CI/CD pipeline using AWS CodeBuild. The `buildspec.yml` file defines the build process, and the `Dockerfile` is used to create a Docker image for the application.

## Usage

- The main functionality of the application is encapsulated in `src/SMS_template.py`.
- Modify the script as needed to change the behavior of the automation.
- Ensure that the necessary environment variables and configurations are set for the web application being tested.

## License

This project is licensed under the MIT License. See the LICENSE file for details.