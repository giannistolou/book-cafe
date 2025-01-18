# Local Development Setup

Follow these steps to set up the project for local development.

## Prerequisites

Make sure you have the following installed on your machine:
- Python (version 3.6 or higher)
- Node.js (version 12 or higher)
- Yarn package manager

## Setup

###  Create and Activate Virtual Environment

If you don't have a virtual environment set up, create one using the following commands:

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment (Windows)
venv\Scripts\activate

# Activate the virtual environment (macOS/Linux)
source venv/bin/activate
```

### Install Django Dependencies

Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

### Install JavaScript Dependencies
Install the required JavaScript packages using Yarn:

```bash
yarn install
```

### Build and Watch CSS
Build the project and start watching for CSS changes:

```bash
yarn run build
yarn run watch:css
```

### Run the Project
Start the Django development server:

```bash
python manage.py runserver
```

### Collect Static Files
In another terminal, collect the static files for the project:

```bash
python manage.py collectstatic
```

### Access the Project

Open your web browser and navigate to `http://127.0.0.1:8000` to access the project

### Additional Information 

- Make sure to activate your virtual environment before running the above commands.
- If you encounter any issues, check the logs for error messages and ensure all dependencies are installed correctly.