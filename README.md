# group-project-team-2
[![Build Status](https://img.shields.io/circleci/build/github/insight-fellows-devops-2020b-sv/group-project-team-2?style=for-the-badge)](https://app.circleci.com/pipelines/github/insight-fellows-devops-2020b-sv/group-project-team-2?branch=master)
[![open-issues](https://img.shields.io/github/issues/insight-fellows-devops-2020b-sv/group-project-team-2?style=for-the-badge)](https://github.com/insight-fellows-devops-2020b-sv/group-project-team-2/issues)
[![open-pr](https://img.shields.io/github/issues-pr/insight-fellows-devops-2020b-sv/group-project-team-2?style=for-the-badge)](https://github.com/insight-fellows-devops-2020b-sv/group-project-team-2/pulls)

# group-project-team-2
An Insight Fellow Project by 20B DO SV

## Features

This module deploys EKS Clusters on AWS and installs a list of Helm Charts on them.

## Terraform Versions

For Terraform v0.12.26+

## Usage

```
module "this" {
    source = "github.com/insight-fellows-devops-2020b-sv/group-project-team-2"
}
```

## Instructions

You will need to configure your AWS credentials before using this project:

### Linux
Add the following in your `~/.bashrc` or `~/.zshrc` with your credentials:
```
export AWS_ACCESS_KEY_ID=YOUR_AWS_ACCESS_KEY_ID
export AWS_SECRET_ACCESS_KEY=YOUR_AWS_SECRET_ACCESS_KEY
```

### Windows
Execute the following in your terminal:
```
$ aws configure
AWS Access Key ID [None]: YOUR_AWS_ACCESS_KEY_ID
AWS Secret Access Key [None]: YOUR_AWS_SECRET_ACCESS_KEY
Default region name [None]: us-west-2
Default output format [None]: json
```

### Testing the Project

Initialize and Run Terraform Scripts
```
terraform init
terraform apply
```
Input Cluster name and AWS Region

If the output gives connection errors, input the following commands:
```
aws eks --region us-west-2 update-kubeconfig --name terrastax
terraform apply
```

In case you get any dependency errors, it could be because of the modules dependencies which is not supported by Terraform.
Simply rerun `terraform apply` to solve this issue

If you want to port forward the services and deployments to your localhost, use the following commands:
```
kubectl --namespace=monitoring port-forward svc/prometheus-operator-prometheus 9090
kubectl --namespace=monitoring port-forward deploy/prometheus-operator-grafana 3000
```

## Examples

- [defaults](https://github.com/insight-fellows-devops-2020b-sv/group-project-team-2/examples/defaults)

## Known  Issues
No issue is creating limit on this module.

<!-- BEGINNING OF PRE-COMMIT-TERRAFORM DOCS HOOK -->
## Requirements

No requirements.

## Providers

| Name | Version |
|------|---------|
| helm | n/a |

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| aws\_region | The region to deploy in | `string` | n/a | yes |
| id | The id of the resources | `string` | n/a | yes |

## Outputs

| Name | Description |
|------|-------------|
| cluster\_arn | The Amazon Resource Name (ARN) of the cluster. |
| cluster\_certificate\_authority\_data | Nested attribute containing certificate-authority-data for your cluster. This is the base64 encoded certificate data required to communicate with your cluster. |
| cluster\_endpoint | The endpoint for your EKS Kubernetes API. |
| cluster\_id | The name/id of the EKS cluster. |
| cluster\_security\_group\_id | Security group ID attached to the EKS cluster. |
| cluster\_version | The Kubernetes server version for the EKS cluster. |
| config\_map\_aws\_auth | A kubernetes configuration to authenticate to this EKS cluster. |

<!-- END OF PRE-COMMIT-TERRAFORM DOCS HOOK -->

## Authors

Module managed by [insight-fellows-devops-2020b-sv](https://github.com/insight-fellows-devops-2020b-sv)
