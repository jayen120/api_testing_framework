# 🔍 API Testing Framework

A recruiter-ready API testing framework built with **Pytest**, **Requests**, and **JSONSchema**, integrated with **Jenkins CI/CD** for automated test execution and reporting.

---

## 🚀 Features
- ✅ Parametrized API endpoint testing with Pytest
- ✅ JSON schema validation for response consistency
- ✅ HTML & JUnit reports generated automatically
- ✅ Jenkins pipeline integration for CI/CD automation
- ✅ Clean, modular project structure with clear documentation

---

## 📂 Project Structure
api-testing-framework/
├── tests/
│ ├── test_parametrize.py # Parametrized API endpoint tests 
│ ├── test_schema_validation.py # Schema validation tests 
├── schemas/ 
│ └── user_schema.json # JSON schema for validation 
├── requirements.txt # Python dependencies 
├── Jenkinsfile # CI/CD pipeline definition 
├── README.md # Project documentation 
└── .gitignore # Ignore venv, cache, reports


---

## ⚙️ Tech Stack
- **Python 3.10+**
- **Pytest** – testing framework
- **Requests** – API calls
- **JSONSchema** – schema validation
- **Pytest-HTML** – HTML reporting
- **Jenkins** – CI/CD automation

---

## ▶️ Run Locally
Clone the repo and install dependencies:
```bash
git clone https://github.com/jayen120/api-testing-framework.git
cd api-testing-framework
pip install -r requirements.txt
