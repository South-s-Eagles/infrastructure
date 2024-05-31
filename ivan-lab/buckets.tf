resource "aws_s3_bucket" "raw-bucket" {
  bucket = "raw-souths-eagle-ivan"
}

resource "aws_s3_bucket" "trusted-bucket" {
  bucket = "trusted-souths-eagle-ivan"
}

resource "aws_s3_bucket" "client-bucket" {
  bucket = "client-souths-eagle-ivan"
}

resource "aws_s3_bucket" "bucket4" {
  bucket = "pipeline-airflow-souths-eagle-ivan"
}