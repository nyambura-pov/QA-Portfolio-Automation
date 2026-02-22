# QA Engineering Portfolio: Manual & Automation Testing

## Overview

This repository showcases my hands-on work in Software Quality Assurance, including manual testing, API validation and Python-based automation.

The focus of this portfolio is structured test design, clear defect reporting, and building maintainable test scripts.

---

## Tech Stack

- **Languages:** Python (PyTest)
- **Automation:** Selenium WebDriver
- **API Testing:** Postman, FastAPI
- **Project Tracking:** Jira (Bug tracking simulation)
- **Web Frameworks:** Streamlit

---

## Repository Structure

### Manual Testing Documentation

Created while testing the **InSight Cataract Detection System**.

- **Test Plan:** Scope, objectives, risks, and testing strategy
- **Test Cases:** 50+ scenarios covering Smoke, Functional, and Regression testing
- **Bug Reports:** Structured defect reports including:
  - Steps to reproduce
  - Expected vs. actual results
  - Severity and priority assessment

---

### API Testing (Postman)

- Postman collection for testing FastAPI backend endpoints
- Tests include:
  - Status code validation (200, 400, 500)
  - JSON schema validation
  - Edge case input validation
  - Basic response time checks

---

### Automation (Selenium + Python)

- `test.py`
- Demonstrates:
  - Web element locators (ID, CSS Selector, XPath)
  - Implicit and Explicit waits
  - Assertions for UI validation
  - Basic Page Object Model (POM) structure

---

## Featured Project: InSight (QA Focus)

**InSight** is an AI-based cataract detection system built using Python and FastAPI.  
During development, I focused on validating input integrity, model output consistency, and overall system reliability.

### QA Contributions

- Applied **Boundary Value Analysis (BVA)** to validate image upload constraints:
  - File size limits
  - Supported and unsupported formats
  - Resolution thresholds

- Performed **Black-Box Testing** using 100+ sample image datasets to evaluate prediction consistency.

- Logged reproducible issues and tracked them through a simulated Jira workflow.

🔗 Jira Simulation Example:  
https://faithnjugunacse.atlassian.net/browse/KAN-4
