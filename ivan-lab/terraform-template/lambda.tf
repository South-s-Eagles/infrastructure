# Default role para ser utilizada na criação de funções lambda
data "aws_iam_role" "lab_role" {
  name = var.default_role_name
}

resource "aws_lambda_function" "trusted_etl_lambda" {
  function_name = "ProcessTrustedEtl"
  description   = "Função lambda que faz o trigger de um evento de criação do S3 Trusted para o S3 Cliente"
  role          = data.aws_iam_role.lab_role.arn
  filename      = "../lambda/functions/trusted_trigger_etl/lambda_function.zip"
  handler       = "lambda_function.lambda_handler"
  runtime       = "python3.10"
  architectures = ["x86_64"]

  vpc_config {
    subnet_ids         = [aws_subnet.public.id, aws_subnet.private.id, aws_subnet.private_second_zone.id]
    security_group_ids = [aws_security_group.spark_server_sg.id]
  }

  environment {
    variables = {
      SPARK_ENDPOINT = aws_instance.spark_instance.private_ip
    }
  }

  tags = {
    Project = var.project_name
  }

  depends_on = [aws_security_group.spark_server_sg]
}
