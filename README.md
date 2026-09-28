# 📚 NoteShare – Peer-to-Peer Study Material Register

NoteShare is a dynamic, localized peer-to-peer study registry built for campus environments. It allows students to catalog, categorize, and discover reference materials, question banks, and lab manuals. The project leverages an automated DevOps pipeline to enforce strict quality gates and conditional blue-green style cloud deployments.

## 🚀 Live Environment Links
* **Live Web Application URL:** [https://noteshare-b4c2.onrender.com](https://noteshare-b4c2.onrender.com)
* **GitHub Project Repository:** [https://github.com/Ajinkya1734/noteshare](https://github.com/Ajinkya1734/noteshare)

---

## 🛠️ Technology Stack & Architecture
* **Backend Engine:** Python 3.12+ powered by the lightweight **Flask** framework.
* **Production Web Server:** **Gunicorn** (Green Unicorn) serving as the WSGI HTTP container.
* **Continuous Integration Suite:** **GitHub Actions** containerized test suiterunners.
* **Static Analysis / Linting:** **Flake8** code standards quality inspector engine.
* **Automated Unit Testing:** **Pytest** testing framework checking state modifications.
* **Cloud Hosting Space:** **Render PaaS Platform** bound strictly via API automation webhooks.

---

## 📂 Core Directory File Layout
```text
noteshare/
├── .github/
│   └── workflows/
│       └── ci-cd.yml      # CI/CD Pipeline Orchestration Code
├── templates/
│   └── index.html         # Jinja2 Dynamic Frontend Layout View
├── .gitignore             # Python Environment Allocation Filter
├── app.py                 # Core Application Web Server & Data Routing Logic
├── requirements.txt       # Unified System Dependencies File List
└── test_app.py            # Automated Validation & Quality Integration Tests
```

---

## 🏗️ Automated CI/CD Pipeline Flow Architecture

```text
  [ Code Push / Pull Request ]
               │
               ▼
   ┌───────────────────────┐
   │    GitHub Actions     │
   │   Container Spawn     │
   └───────────┬───────────┘
               │
               ▼
   ┌───────────────────────┐
   │ Dependency Extraction │ ──> Reads and installs requirements.txt
   └───────────┬───────────┘
               │
               ▼
   ┌───────────────────────┐
   │    Quality Gate 1     │ ──> Flake8 runs strict style linting check
   │     (Code Linting)    │
   └───────────┬───────────┘
               │
               ▼
   ┌───────────────────────┐
   │    Quality Gate 2     │ ──> Pytest executes 4 rigorous automated tests
   │   (Automated Tests)   │
   └───────────┬───────────┘
               │
               ▼
   ┌───────────────────────┐
   │  Conditional Deploy   │ ──> Fired ONLY if main branch push & tests pass
   │  (Render API Webhook) │
   └───────────────────────┘
```

---

## 🧪 Automated Test Cases Covered (`test_app.py`)
1. **`test_health_check_endpoint`**: Confirms that `/health` functions properly and reports status maps.
2. **`test_material_addition_updates_registry`**: Validates data creation, state modification, and server calculation logs.
3. **`test_blank_field_submission_rejected`**: Ensures quality gates throw correct `400 Bad Request` states on empty inputs.
4. **`test_registry_clear_wipes_all_data`**: Verifies administrative database reset hooks safely wipe values back to baseline zero.
