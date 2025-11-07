# 📘 CONTRIBUTING.md

## 🏫 Project: IMDB Top 50 Scraper (Team Elk)
**Team Members:**  
- **Lead:** @tayjmcdile-alt  
- **Designer:** @ausarkhan  
- **Software Engineer (SWE):** @apaiz12  
- **Tester:** @ericbutler1209  

---

## 🧭 Purpose
This document explains how to contribute to the **IMDB Top 50 Scraper** project for the XULA SDLC assignment.  
All work follows the **Software Development Life Cycle (SDLC)**, uses **Continuous Integration (CI)**, and awards credit based on **commit authorship**.

---

## 🛠️ Getting Started
1. Clone the repo and set up your environment:
   ```bash
   git clone https://github.com/nishantsahoo/IMDB_Top50_Scrape.git
   cd IMDB_Top50_Scrape
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
   
--- 

## 💻 Contributing Workflow

All contributions to this project must follow the SDLC and use GitHub effectively:

1. **Follow the SDLC:**  
   - Plan → Design → Implement → Test → Deploy → Maintain.  
   - Each team member works only on assigned issues.

2. **Branching Strategy:**  
   - Main branch: `main`  
   - Feature branches: `feature/<short-description>`  
   - Test branches: `test/<short-description>`  
   - Example:  
     ```bash
     git checkout -b feature/add-xula-driver
     ```

3. **Commits:**  
   - Write clear and descriptive commit messages:  
     ```
     [Component] Short description
     
     - What was changed
     - Why it was changed
     - Issue reference (#issue-number)
     ```  
   - Example:  
     ```
     [Scraper] Added XULA driver function

     - Created main driver to run IMDb scraper
     - Linked to Issue #4
     ```

4. **Pull Requests (PRs):**  
   - Push your branch and open a PR into `main`.  
   - Include a reference to the relevant issue(s).  
   - Ensure all tests pass before merging.

---

## 🧪 Testing Guidelines

All testing should use Python’s **unittest** framework:

1. **Tester & SWE Responsibilities:**  
   - Write **10 tests** for the *Centennial Campaign Impact Scraper* function.  
   - Write **10+ tests** for any class you implement from the UML diagram.

2. **Test File Naming:**  
   - `test_<function_or_class>.py`  
   - Place test files in a `tests/` directory.

3. **Running Tests:**  
   ```bash
   python -m unittest discover tests
   ```
---