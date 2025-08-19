# Calc - Math Interpreter

[![Continuous Integration](https://github.com/JeelDobariya38/Calc-Backend/actions/workflows/test-code.yml/badge.svg)](https://github.com/JeelDobariya38/Calc-Backend/actions/workflows/test-code.yml)

## Overview

Calc is a versatile math interpreter designed to assist with various mathematical calculations and homework. It offers both a command-line interface (CLI) and an HTTP API, making it suitable for diverse use cases, including local usage, professional integration, and educational purposes.

## Installation

**App Requires**: Python 3.10+ [Recommended, 3.12.x]

You can install Calc in three ways:

1. **Install Locally**
2. **Install Containerized (using Docker):** [Recommended for professional use]
3. **Install Pythonically (using pip):** _Supports only CLI app_ [Recommended for aspiring developers]

### Install Locally

**Requirements:** Python (3.10+) & Git

1. Verify Git installation.

   ```bash
   git --version
   ```

2. Clone the repository locally.

   ```bash
   git clone https://github.com/JeelDobariya38/Calc.git
   ```

3. Navigate to the cloned directory.

   ```bash
   cd Calc
   ```

4. Verify Python installation.

   ```bash
   python --version
   ```

5. Install dependencies.

   ```bash
   pip install -r requirements.txt
   ```

6. Run the REPL of Calc:

   ```bash
   python main.py
   ```

7. Optionally, run Calc from the browser.

   ```bash
   uvicorn api.app:app --port 8000
   ```

### Install Containerized (Using Docker) [for advanced users]

**Requirements:** Docker Desktop

#### For Development Use (only valid for developers)

1. Verify Git and Docker installation.

   ```bash
   git --version
   docker --version
   ```

2. Clone the repository.

   ```bash
   git clone https://github.com/JeelDobariya38/Calc.git
   ```

3. Navigate to the Calc directory.

   ```bash
   cd Calc
   ```

4. Build the Docker images. You can build either or both images according to your needs.

   - Building backend image

     ```bash
     docker build -t jeeldobariya2325/calc:latest-backend -f Dockerfile.backend .
     ```

   - Building CLI image

     ```bash
     docker build -t jeeldobariya2325/calc:latest-cli -f Dockerfile.cli .
     ```

5. Run a container from the newly built image.

   - Running the API

     ```bash
     docker run -p 8080:80 --env "HOST=0.0.0.0" --env "PORT=80" -d jeeldobariya2325/calc:latest-backend
     ```

   - Running CLI

     ```bash
     docker run -it jeeldobariya2325/calc:latest-cli
     ```

#### For Production Use (for final production usage)

1. Running the API

   ```bash
   docker run -p 8080:80 --env "HOST=0.0.0.0" --env "PORT=80" -d jeeldobariya2325/calc:latest-backend
   ```

2. Running CLI tools

   ```bash
   docker run -it jeeldobariya2325/calc:latest-cli
   ```

### Install Pythonically (Using pip) [for beginner users]

**Requirements:** Python (3.10+), pip & Git

1. Verify Python and Git installation.

   ```bash
   git --version
   python --version
   pip --version
   ```

2. Install the package from the Git repository:

   ```bash
   pip install git+https://github.com/JeelDobariya38/Calc.git
   ```

3. Run the CLI tool from the terminal:

   ```bash
   calc
   ```

## Usage

### CLI Mode

- **Local Installation:**

  ```bash
  python main.py
  ```

- **Docker:**

  ```bash
  docker run -it jeeldobariya2325/calc:latest-cli
  ```

### API Mode (Backend)

- **Local Installation:**

  ```bash
  uvicorn api.app:app --port 8000
  ```

  Access the API at `http://localhost:8000`.

- **Docker:**

  ```bash
  docker run -p 8080:80 --env "HOST=0.0.0.0" --env "PORT=80" -d jeeldobariya2325/calc:latest-backend
  ```

  Access the API at `http://localhost:8080`.

## Report Bugs

If you encounter any bugs or have any questions related to Calc, feel free to create an issue on our [GitHub repository](https://github.com/JeelDobariya38/Calc-Backend/issues).

For feature requests or contributions, you are welcome to create an issue or a pull request.

## License

This project is licensed under the [MIT License](LICENSE.txt).
