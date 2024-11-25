### **Zero Account Setup Steps**

1. **Create the AWS Account:**
   - Use the AWS Console to set up Account Zero.
   - For lab environments, you can use the **Gmail "+" trick** to create unique email addresses (e.g., `example+accountzero@gmail.com`).

2. **Enable Multi-Factor Authentication (MFA):**
   - Set up MFA on the root account using a virtual device like Google Authenticator or Authy for enhanced security.

3. **Enable IAM Access for AWS Budgets:**
   - Navigate to **Account Settings** in the AWS Billing Console.
   - Enable **IAM Access for AWS Budgets** to allow budget resources to be managed via IAM users or roles.

4. **Run CloudFormation for Security Setup:**
   - Deploy the CloudFormation template to configure the following:
     - **IAM Programmatic User** with no permissions.
     - **IAM Role** with AdministratorAccess and trust policies for secure assume-role operations.
     - **Budget Alert** for cost monitoring, with notifications sent to the account's email address.

5. **Store Credentials Securely:**
   - Copy and securely store the programmatic user's **Access Key ID** and **Secret Access Key** immediately after CloudFormation execution.

6. **Validate Security and Governance:**
   - Test assume-role functionality from the programmatic user to ensure the trust policy is configured correctly.
   - Verify budget alert email notifications by simulating threshold breaches.