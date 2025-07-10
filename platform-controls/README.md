
## Usage

Reference templates in workload pipelines:

```yaml
# workloads/app1/pipelines/deploy.yml
jobs:
  deploy:
    uses: ../../platform-controls/cloud-scripts/pipeline-templates/aws/terraform-deploy.yml@main
    with:
      environment: production
      region: us-west-2
```

## Available Templates

### Cloud-Specific
- `terraform-deploy.yml` - Standard Terraform deployment
- `security-scan.yml` - Security scanning
- `multi-region-deploy.yml` - Multi-region deployment
- `compliance-check.yml` - Policy validation

### Shared
- `docker-build.yml` - Container builds
- `unit-tests.yml` - Unit testing
- `integration-tests.yml` - Integration testing
- `code-quality.yml` - Code quality checks

## Parameters

Common parameters for all templates:
- `cloud-provider` - Target cloud (aws/azure/gcp)
- `environment` - Deployment environment (dev/staging/prod)
- `region` - Target region
- `terraform-version` - Terraform version to use

## Contributing

1. Add new templates to appropriate cloud directory
2. Update this README with template description
3. Test with multiple cloud providers
4. Submit for review