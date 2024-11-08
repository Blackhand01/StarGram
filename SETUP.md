# Hackathon Project

This repository contains a Python-based project configured for hackathon development. It includes a virtual environment, documentation generation with Sphinx, automated testing, and a structured setup for development and documentation.

---

## **Requirements**

To replicate this configuration, you need the following tools:

- **Python**: Version 3.8 or higher
- **pip**: Python package manager
- **make**: For automating commands (pre-installed on macOS/Linux; for Windows, use `make.bat` or WSL)
- **Sphinx**: For generating documentation
- **pytest**: For running automated tests

---

## **Project Structure**

The repository is organized as follows:
```
hackathon-project/
├── .pytest_cache/         # Cache for pytest
├── .venv/                 # Virtual environment (not included in version control)
├── data/                  # Project datasets
├── docs/                  # Sphinx documentation
│   ├── build/             # Generated documentation (HTML)
│   └── source/            # Sphinx source files
├── notebooks/             # Jupyter notebooks
├── src/                   # Main source code
│   └── main.py            # Main Python script
├── tests/                 # Automated tests
│   └── test_main.py       # Example test file
├── .gitignore             # File to exclude unnecessary files/directories from version control
├── Makefile               # Automated commands
├── README.md              # This file
└── requirements.txt       # Python dependencies
```

---

## **Setup Instructions**

### **1. Clone the Repository**

Clone this repository to your local machine:
```bash
git clone <REPOSITORY_URL>
cd hackathon-project
```

### **2. Initialize the Virtual Environment**

Run the following command to set up the virtual environment:
```bash
make init
```
This will create a virtual environment in the `.venv` directory and install dependencies listed in `requirements.txt`.

### **3. Generate Documentation**

To generate the HTML documentation, use:
```bash
make docs
```
The generated HTML files will be available in `docs/build/html`. You can open the main file with:
```bash
make open-docs
```

### **4. Run Tests**

Run the automated tests with:
```bash
make test
```

### **5. Run the Project**

Run the main script of the project:
```bash
make run
```

### **6. Cleaning Up**

- **Soft Clean** (removes temporary files, caches, and Sphinx build artifacts):
  ```bash
  make clean
  ```
- **Hard Clean** (removes everything, including the virtual environment):
  ```bash
  make clean-forced
  ```

---

## **Dependencies**

Dependencies are managed in the `requirements.txt` file. To update the list of currently installed dependencies, use:
```bash
make update-reqs
```

The current required libraries include:
```
sphinx
pytest
```

---

## **Notes**

- Documentation is built using **Sphinx**. The source files are located in `docs/source/`.
- Tests are defined in the `tests/` directory and can be extended based on the project's needs.
- If you encounter any issues, ensure Python and the required tools are installed correctly.

---

## **Contributors**

- **Stefano Roy Bisignano**
- **Mirko Di Maggio**
