terraform {
  required_version = "~> 1.0"

  cloud {
    organization = "souths-eagle"

    workspaces {
      name = "souths-eagle-infra-gui"
    }
  }

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
}

