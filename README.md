# Cloud-IaC-AlaCarte
**Cloud-IaC-AlaCarte** is a modular, multi-cloud Infrastructure as Code (IaC) framework that simplifies the deployment and management of cloud resources across AWS, Azure, and GCP.

# Cloud-IaC-AlaCarte Framework Principles

The Cloud-IaC-AlaCarte framework is designed with the following principles:

1. **Modularity**: Infrastructure components are organized as reusable modules to support multi-cloud deployments.
2. **Governance**: Centralized platform-level controls ensure consistent policies and management across cloud providers.
3. **Flexibility**: A la carte modules enable teams to select and integrate only the components they need.
4. **Scalability**: Supports the addition of new workloads, environments, or cloud providers without major structural changes.

## Features
- **Multi-Cloud Support**: Manage infrastructure on AWS, Azure, and GCP.
- **Modular Design**: Reusable Terraform modules for common resources.
- **Orchestration**: Python scripts for account and project setup.

# Detailed Descriptions

## infra-modules/
Reusable modules for common infrastructure components across multiple cloud providers. Examples include compute resources (e.g., VMs, EC2), networking configurations (e.g., VPCs, subnets), and NoSQL databases.

## platform-controls/
Modules and scripts for cloud governance and foundational controls:
- **Modules**: Provide reusable configurations for managing AWS Organizations, Azure Management Groups, and GCP folders.
- **Terraform Configurations**: Define environment-specific setups for platform-level governance.

## workloads/
Contains workload-specific configurations for applications. Each application folder includes:
- **Pipelines**: CI/CD configurations for deployment.
- **IaC**: Infrastructure as Code specific to the application.
- **Code**: Application source code.
- **Tests**: Integration, load, and other workload-specific tests.

## cloud-scripts/
Utility scripts for managing platform operations, such as provisioning accounts or enforcing policies.

## Quick Start

1. **Clone the Repository**:
   ```
   git clone https://github.com/yourusername/Cloud-IaC-AlaCarte.git
   cd Cloud-IaC-AlaCarte
   ```
2. **Install Dependencies and Configure the Environment**:
`pip install boto3 azure-mgmt-subscription google-cloud-resource-manager pyyaml`
### Install Terraform
#### Follow instructions at: https://www.terraform.io/downloads

3. **Set Up and Deploy:** 

##### Run the Python script to set up accounts or projects
`python cloud-scripts/setup.py`

## Initialize Terraform
`terraform init`

## Deploy the infrastructure
`terraform apply`

# Project Structure
**Cloud-IaC-AlaCarte** is a modular, multi-cloud Infrastructure as Code (IaC) framework. It is designed to provide reusable, "a la carte" components for managing cloud infrastructure and workloads, including platform-level governance, application-specific infrastructure, and utility scripts.

## Directory Structure and Purpose
```
Cloud-IaC-AlaCarte/
├── LICENSE                      # Project license
├── README.md                    # This documentation file
├── infra-modules/               # A la carte reusable infrastructure modules
│   ├── compute/                 # Modules for multi-cloud compute resources (e.g., VMs, EC2)
│   ├── networking/              # Modules for multi-cloud networking (e.g., VPCs, subnets)
│   └── nosql-db/                # Modules for NoSQL databases
│       ├── aws/                 # AWS-specific NoSQL database implementation (e.g., DynamoDB)
│       ├── azure/               # Azure-specific NoSQL database implementation (e.g., CosmosDB)
│       └── gcp/                 # GCP-specific NoSQL database implementation (e.g., Bigtable)
├── platform-controls/           # Platform-level governance and foundational cloud controls
│   ├── cloud-scripts/           # Utility scripts for managing cloud operations
│   │   └── control-plane/       # Scripts for central governance (e.g., account provisioning)
│   ├── modules/                 # Reusable modules for governance
│   │   ├── aws-organizations/   # Manage AWS Organizations and Service Control Policies (SCPs)
│   │   ├── azure-management-groups/ # Manage Azure Management Groups and Policies
│   │   └── gcp-resource-hierarchy/  # Manage GCP folders and IAM policies
│   └── terraform/               # Environment-specific governance configurations
│       └── control-plane/       # Configurations for platform governance
├── workloads/                   # Workload-specific configurations and deployments
│   ├── app1/                    # Application 1 (example workload)
│   │   ├── pipelines/           # CI/CD pipelines for app1
│   │   ├── iac/                 # IaC configurations for app1's infrastructure
│   │   ├── code/                # Application source code for app1
│   │   └── tests/               # Workload-specific tests for app1
│   ├── app2/                    # Application 2 (example workload)
│   │   ├── pipelines/           # CI/CD pipelines for app2
│   │   ├── iac/                 # IaC configurations for app2's infrastructure
│   │   ├── code/                # Application source code for app2
│   │   └── tests/               # Workload-specific tests for app2
├── docs/                        # Documentation for the project, modules, and usage
```
# Detailed Descriptions

## infra-modules/
Reusable modules for common infrastructure components across multiple cloud providers. Examples include compute resources (e.g., VMs, EC2), networking configurations (e.g., VPCs, subnets), and NoSQL databases.

## platform-controls/
Modules and scripts for cloud governance and foundational controls:
- **Modules**: Provide reusable configurations for managing AWS Organizations, Azure Management Groups, and GCP folders.
- **Terraform Configurations**: Define environment-specific setups for platform-level governance.

## workloads/
Contains workload-specific configurations for applications. Each application folder includes:
- **Pipelines**: CI/CD configurations for deployment.
- **IaC**: Infrastructure as Code specific to the application.
- **Code**: Application source code.
- **Tests**: Integration, load, and other workload-specific tests.

## cloud-scripts/
Utility scripts for managing platform operations, such as provisioning accounts or enforcing policies.

# Contributing
## To contribute:
### 1. Fork the repository.
### 2. Create a feature branch:
`git checkout -b feature/your-feature-name`
### 3. Commit your changes:
`git commit -m "Add your commit message"`
### 4. Push to your fork:
`git push origin feature/your-feature-name`
### 5. Open a pull request and describe your changes.
