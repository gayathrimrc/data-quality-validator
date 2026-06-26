
# 📘 **Data Quality Validator**  
A production‑ready Python‑based **Data Quality Validation Service** designed for automated CI/CD pipelines, containerized execution, and multi‑environment Kubernetes deployment.  
This project validates structured datasets (CSV) using schema rules, type checks, and row‑level business rules — ensuring data quality before ingestion into downstream systems.

---

## 🚀 Overview  
The Data Quality Validator provides:

- **Schema validation** (required columns, data types)  
- **Row‑level rule checks** (null checks, ranges, patterns)  
- **Exit‑code‑driven automation** for CI/CD  
- **Unit‑tested validation logic**  
- **Dockerized runtime**  
- **GHCR‑published container images**  
- **Kubernetes deployment across dev → qa → prod**  
- **Enterprise GitHub Actions pipeline** with approvals  

This service is ideal for **data engineering**, **ETL/ELT workflows**, **ML pipelines**, and **data governance automation**.

---

## 📁 Project Structure  
```
data-quality-validator/
│
├── main.py                 # Entry point for validation execution
├── validator.py            # Core validation logic
├── requirements.txt        # Python dependencies
├── Dockerfile              # Container build definition
├── README.md               # Documentation
│
├── k8s/                    # Kubernetes manifests
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── config-dev.yaml
│   ├── config-qa.yaml
│   └── config-prod.yaml
│
└── tests/
    └── test_validator.py   # Pytest suite
```

---

## 🧠 How It Works  
The validator loads a CSV file, checks:

- Required columns  
- Expected data types  
- Business rules (e.g., age ≥ 0, email not null)  

It returns:

- **Exit code 0** → validation passed  
- **Exit code 1** → validation failed  

This makes it perfect for **automated pipelines**.

---

## ▶️ Running Locally

### Install dependencies
```
pip install -r requirements.txt
```

### Run validation
```
python main.py <path_to_csv>
```

### Run tests
```
pytest
```

---

## 🐳 Docker Support  
The project includes a production‑ready Dockerfile.

### Build the image
```
docker build -t data-quality-validator .
```

### Run the validator inside Docker
```
docker run --rm -v $(pwd)/data.csv:/app/data.csv data-quality-validator
```

---

## 📦 Publishing to GHCR (GitHub Container Registry)  
The GitHub Actions pipeline automatically:

- Builds the Docker image  
- Tags it with the commit SHA  
- Pushes it to GHCR  

Images appear under:

```
ghcr.io/<your-org-or-user>/data-quality-validator:<sha>
```

---

## 🏗️ Enterprise CI/CD Pipeline (GitHub Actions)  
The repository includes a full enterprise pipeline:

### **Stages**
1. **Build & Test**  
2. **Data Validation Execution**  
3. **Docker Build**  
4. **Push to GHCR**  
5. **Deploy to Dev (Kubernetes)**  
6. **Promote to QA**  
7. **Manual Approval → Deploy to Prod**

### **Environments**
- `dev` → automatic  
- `qa` → automatic  
- `prod` → manual approval required  

### **Secrets Required**
| Secret | Purpose |
|--------|---------|
| `GHCR_TOKEN` | Push to GHCR |
| `KUBECONFIG_DEV` | Deploy to dev cluster |
| `KUBECONFIG_QA` | Deploy to qa cluster |
| `KUBECONFIG_PROD` | Deploy to prod cluster |

---

## ☸️ Kubernetes Deployment  
The project includes manifests for:

- Deployment  
- Service  
- Environment‑specific ConfigMaps  

### Deploy to dev
```
kubectl apply -f k8s/config-dev.yaml
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

### Deploy to qa
```
kubectl apply -f k8s/config-qa.yaml
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

### Deploy to prod
```
kubectl apply -f k8s/config-prod.yaml
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

---

## 🧪 Testing Strategy  
The project uses **pytest** for:

- Schema validation tests  
- Rule validation tests  
- Negative test cases  

Tests run automatically in CI.

---

## 🔒 Security & Governance  
This project follows enterprise best practices:

- No credentials stored in code  
- All secrets stored in GitHub Environments  
- Immutable container images (tagged with commit SHA)  
- Manual approval for production deployments  
- Config‑driven environment separation  

---

## 📈 Roadmap  
Future enhancements may include:

- Data profiling metrics  
- Great Expectations integration  
- API wrapper for real‑time validation  
- Airflow / Azure Data Factory integration  
- Slack/Teams notifications  

---
