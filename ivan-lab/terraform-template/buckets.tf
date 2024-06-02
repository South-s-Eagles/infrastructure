resource "aws_s3_bucket" "raw" {
  bucket = "raw-souths-eagle-ivan"

  tags = {
    Name = var.project_name
  }
}

resource "aws_s3_bucket" "trusted" {
  bucket = "trusted-souths-eagle-ivan"

  tags = {
    Name = var.project_name
  }
}

resource "aws_s3_bucket" "client" {
  bucket = "client-souths-eagle-ivan"

  tags = {
    Name = var.project_name
  }
}

resource "aws_s3_bucket" "data_pipeline" {
  bucket = "pipeline-airflow-souths-eagle-ivan"

  tags = {
    Name = var.project_name
  }
}
