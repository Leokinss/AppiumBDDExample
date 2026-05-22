# Mobile Automation Framework
 
> Page Object Model (POM) with Gherkin syntax via Pytest-BDD.
 
## Setup
 
```bash
py -3.14 -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```
 
## Running tests
 
```bash
pytest -s -v --platform android   # Android
pytest -s -v --platform ios       # iOS
```
 
The `--platform` flag (default: `android`) selects the mobile target for the Appium driver session.
 
## Project structure
 
| Path | Description |
|------|-------------|
| `config/capabilities.yaml` | Appium driver capabilities per platform |
| `pages/mobile/<platform>/` | Page objects per platform |
| `pages/mobile/pages.py` | Platform class registry (`PAGE_CLASSES`) |
| `tests/features/` | Gherkin feature files |
 
## Adding iOS support (TODO)
 
1. Implement page objects under `pages/mobile/ios/*.py`
2. Register the classes in `pages/mobile/pages.py` under `PAGE_CLASSES["iOS"]`
## Prerequisites
 
- Appium server running locally
- Android emulator or iOS simulator