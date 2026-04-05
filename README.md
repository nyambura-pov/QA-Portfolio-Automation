# QA Engineering Portfolio: Manual & Automation Testing

## Overview

This repository showcases my hands-on work in Software Quality Assurance, including manual test strategies, end-to-end API validation, and Python-based UI automation. 

The focus of this portfolio is structured test design, clear defect reporting, and building highly maintainable, scalable test scripts.



## Tech Stack

* **Languages:** Python (PyTest), JavaScript
* **Automation:** Selenium WebDriver
* **API Testing:** Postman, Postman CLI, FastAPI
* **Project Tracking:** Jira (Simulated Agile workflow)
* **Web Frameworks:** Streamlit



## Repository Structure

### 1. API Testing & Automation (Postman)

**Featured Project: E-Commerce E2E Order Lifecycle**
An automated, end-to-end API testing suite simulating a complete user checkout workflow utilizing the DummyJSON API. 

* **Stateful Testing & Dynamic Variables:** Captured authentication tokens and generated database IDs to pass dynamically into subsequent PUT and DELETE requests, eliminating hardcoded test data.
* **Business Logic Validation:** Engineered JavaScript assertions (using Chai) to verify mathematical calculations (e.g., Price * Quantity = Total) and JSON schema integrity.
* **Automated Teardown:** Implemented DELETE requests at the end of the test lifecycle to prevent database pollution and maintain isolated test environments.
* **The E2E Journey Tested:** 1. POST: Authenticate User (Bearer Token)
  2. GET: Search Products (Query Params)
  3. POST: Create Cart & Add Items
  4. PUT: Update Cart Quantities (State Change)
  5. DELETE: Teardown / Remove Cart

### 2. UI Automation (Selenium + Python)

* **test.py**
* Demonstrates foundational UI testing principles:
  * Web element locators (ID, CSS Selector, XPath)
  * Synchronization using Implicit and Explicit waits
  * Assertions for UI validation and state verification
  * Basic Page Object Model (POM) architectural structure



## Featured Project: InSight Cataract Detection (QA Focus)

**InSight** is an AI-based cataract detection system built using Python and FastAPI. During its development, I focused on validating input integrity, model output consistency, and overall system reliability.

### QA Contributions

* **Manual Testing Documentation:** Developed comprehensive Test Plans and 50+ Test Cases covering Smoke, Functional, and Regression testing.
* **Boundary Value Analysis (BVA):** Applied rigorous constraints to validate image uploads, including file size limits, supported formats, and resolution thresholds.
* **Black-Box Testing:** Evaluated prediction consistency using 100+ sample image datasets.
* **Defect Lifecycle Management:** Logged structured, reproducible bug reports detailing steps to reproduce, expected vs. actual results, and severity/priority assessments. Tracked through a simulated Jira workflow.

**Jira Simulation Example:** https://faithnjugunacse.atlassian.net/browse/KAN-4
