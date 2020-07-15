#######
# EKS
#######
variable "id" {
  description = "The id of the resources"
  type        = string
}

variable "aws_region" {
  description = "The region to deploy in"
  type        = string
}

provider "aws" {
  region = var.aws_region
}