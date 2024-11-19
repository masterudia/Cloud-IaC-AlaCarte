# Cloud-IaC-AlaCarte
![cloud-iac-alacarte Logo](/Cloud-IaC-AlaCarte/cloud_alacarte_logo)
**Cloud-IaC-AlaCarte** is a modular, multi-cloud Infrastructure as Code (IaC) framework that simplifies the deployment and management of cloud resources across AWS, Azure, and GCP.

## Features
- **Multi-Cloud Support**: Manage infrastructure on AWS, Azure, and GCP.
- **Modular Design**: Reusable Terraform modules for common resources.
- **Orchestration**: Python scripts for account and project setup.

## Quick Start

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/Cloud-IaC-AlaCarte.git
   cd Cloud-IaC-AlaCarte
2. **Install Dependencies and Configure the Environment**:
```
pip install boto3 azure-mgmt-subscription google-cloud-resource-manager pyyaml
```
### Install Terraform
#### Follow instructions at: https://www.terraform.io/downloads

##### Edit config.yaml with your cloud-specific settings:
###### Example:
```
environments:
  dev:
    cloud: aws
    account_name: "Dev Account"
    email: "dev@example.com"
  prod:
    cloud: azure
    subscription_name: "Prod Subscription"
    email: "prod@example.com"
```
3. **Set Up and Deploy:** 
```
##### Run the Python script to set up accounts or projects
python cloud-scripts/setup.py

# Initialize Terraform
terraform init

# Deploy the infrastructure
terraform apply
```
# Project Structure
```
Cloud-IaC-AlaCarte/
├── cloud-scripts/      # Python scripts for multi-cloud setup
├── terraform/          # Terraform modules and configurations
├── docs/               # Documentation and guides
├── .github/            # CI/CD workflows
└── README.md           # Project overview
```

# Contributing

```
# To contribute:
# 1. Fork the repository.
# 2. Create a feature branch:
git checkout -b feature/your-feature-name

# 3. Commit your changes:
git commit -m "Add your commit message"

# 4. Push to your fork:
git push origin feature/your-feature-name

# 5. Open a pull request and describe your changes.
````
