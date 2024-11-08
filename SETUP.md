# Hackathon Project - Setup Instructions

This document contains step-by-step instructions to replicate the project setup on any system. It includes details on requirements, commands, and structure for easy initialization and use.

---

## **Requirements**

To set up and run this project, you need the following tools:

- **Python**: Version 3.8 or higher
- **pip**: Python package manager
- **make**: For automating commands (pre-installed on macOS/Linux; for Windows, use `make.bat` or WSL)
- **Sphinx**: For generating documentation
- **pytest**: For running automated tests

---

## **Project Structure**

The project structure is organized as follows:
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
├── README.md              # General project overview
└── requirements.txt       # Python dependencies
```

---

## **Setup Steps**

### **1. Clone the Repository**

Clone this repository to your local machine:
```bash
git clone <REPOSITORY_URL>
cd hackathon-project
```

### **2. Initialize the Virtual Environment**

Run the following command to set up the virtual environment and install dependencies:
```bash
make init
```
This will create a virtual environment in the `.venv` directory and install dependencies from `requirements.txt`.

### **3. Generate Documentation**

To generate the HTML documentation using Sphinx:
```bash
make docs
```
The generated HTML files will be located in `docs/build/html`. Open the main file in your browser with:
```bash
make open-docs
```

### **4. Run Tests**

Run automated tests to ensure everything works as expected:
```bash
make test
```

### **5. Run the Project**

Execute the main script to start the project:
```bash
make run
```

### **6. Cleaning Up**

- **Soft Clean**: Removes temporary files, caches, and Sphinx build artifacts:
  ```bash
  make clean
  ```

- **Hard Clean**: Removes everything, including the virtual environment:
  ```bash
  make clean-forced
  ```

---

## **Updating Dependencies**

If you install new Python packages and want to update `requirements.txt`, run:
```bash
make update-reqs
```

---

## **Notes**

- **Documentation**: Built with Sphinx, located in `docs/source/`. Regenerate it with `make docs`.
- **Tests**: Stored in the `tests/` directory and extendable for new features.
- **Virtual Environment**: Managed locally in `.venv`, ensuring project isolation.

---

## **Contact**

For issues or contributions, contact:

- **Stefano Roy Bisignano**: bisiwork01@gmail.com
- **Mirko Di Maggio**: mirko27.mdm@gmail.com
