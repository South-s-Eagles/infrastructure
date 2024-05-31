provider "aws" {
  region = var.region
  assume_role {
    role_arn = "arn:aws:iam::712757779207:role/LabRole"
  }
}