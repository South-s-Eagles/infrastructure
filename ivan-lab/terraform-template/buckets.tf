resource "aws_s3_bucket" "raw-souths-eagle-xx" {
  bucket = "raw-souths-eagle-ivan"

  tags = {
    Project = var.project_name
  }
}

resource "aws_s3_bucket" "trusted-souths-eagle-xx" {
  bucket = "trusted-souths-eagle-ivan"

  tags = {
    Project = var.project_name
  }
}

resource "aws_s3_bucket" "client-souths-eagle-xx" {
  bucket = "client-souths-eagle-ivan"

  tags = {
    Project = var.project_name
  }
}

resource "aws_s3_bucket" "pipeline-airflow-souths-eagle-xx" {
  bucket = "pipeline-airflow-souths-eagle-ivan"

  tags = {
    Project = var.project_name
  }
}

resource "aws_s3_bucket" "infra-resources-souths-eagle-xx" {
  bucket = "infra-resources-souths-eagle-ivan"

  tags = {
    Project = var.project_name
  }
}

resource "aws_s3_bucket" "laudo_medico_client" {
  bucket = "infra-resources-souths-eagle-ivan"

  tags = {
    Project = var.project_name
  }
}

/*##--------- Buckets Permission --------*/
resource "aws_lambda_permission" "lambda-trusted-s3-permission" {
  statement_id  = "AllowS3Invoke"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.trusted_etl_lambda.function_name
  principal     = "s3.amazonaws.com"
  source_arn    = aws_s3_bucket.trusted.arn
}


/*##--------- Buckets notification ---------*/
resource "aws_s3_bucket_notification" "bucket_trusted_notification" {
  bucket = aws_s3_bucket.trusted.id

  lambda_function {
    lambda_function_arn = aws_lambda_function.trusted_etl_lambda.arn
    events              = ["s3:ObjectCreated:*"]
  }

  depends_on = [aws_lambda_permission.lambda-trusted-s3-permission]
}
