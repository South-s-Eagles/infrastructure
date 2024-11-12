resource "aws_s3_bucket" "laudo" {
  bucket = "laudo-souths-eagle-xx"

  tags = {
    Project = var.project_name
  }
}

#
# resource "aws_s3_bucket" "raw" {
#   bucket = "raw-souths-eagle-xx"
#
#   tags = {
#     Project = var.project_name
#   }
#
#   lifecycle {
#     prevent_destroy = true
#   }
# }
#
# resource "aws_s3_bucket" "trusted" {
#   bucket = "trusted-souths-eagle-xx"
#
#   tags = {
#     Project = var.project_name
#   }
#
#   lifecycle {
#     prevent_destroy = true
#   }
# }
#
# resource "aws_s3_bucket" "client" {
#   bucket = "client-souths-eagle-xx"
#
#   tags = {
#     Project = var.project_name
#   }
#   lifecycle {
#     prevent_destroy = true
#   }
# }
#
# resource "aws_s3_bucket" "infra_resources_storage" {
#   bucket = "infra-resources-souths-eagle-xx"
#
#   tags = {
#     Project = var.project_name
#   }
#   lifecycle {
#     prevent_destroy = true
#   }
# }

#
# /*##--------- Buckets Permission --------*/
# resource "aws_lambda_permission" "lambda-trusted-s3-permission" {
#   statement_id  = "AllowS3Invoke"
#   action        = "lambda:InvokeFunction"
#   function_name = aws_lambda_function.trusted_etl_lambda.function_name
#   principal     = "s3.amazonaws.com"
#   source_arn    = aws_s3_bucket.trusted.arn
# }
#
#
# /*##--------- Buckets notification ---------*/
# resource "aws_s3_bucket_notification" "bucket_trusted_notification" {
#   bucket = aws_s3_bucket.trusted.id
#
#   lambda_function {
#     lambda_function_arn = aws_lambda_function.trusted_etl_lambda.arn
#     events              = ["s3:ObjectCreated:*"]
#   }
#
#   depends_on = [aws_lambda_permission.lambda-trusted-s3-permission]
# }
