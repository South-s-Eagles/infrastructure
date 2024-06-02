variable "AWS_REGION" {
  description = "Região da AWS"
  type        = string
  default     = "us-east-1"
}

variable "AWS_ACCESS_KEY_ID" {
  type = string
}

variable "AWS_SECRET_ACCESS_KEY" {
  type = string
}

variable "AWS_SESSION_TOKEN" {
  type = string
}

/* #----------- Variaveis da intancia ---------------# */
# variable "ami_id" {
#   description = "ID da AMI"
#   type        = string
#   default     = "ami-0f9fc25dd2506cf6d" # Amazon linux 
# }

# variable "instance_type" {
#   description = "Tipo da instância EC2"
#   type        = string
#   default     = "t2.micro" # Padrão de graça
# }

# variable "key_pair_name" {
#   description = "Nome do par de chaves para acesso SSH"
#   type        = string
#   default     = "home-ec2-sptech"
# }


/* #----------- Variaveis de rede ---------------# */
# variable "vpc_cidr" {
#   description = "CIDR block da VPC"
#   type        = string
#   nullable    = false
# }
#
# variable "public_subnet_cidr" {
#   description = "CIDR block da subnet publica"
#   type        = string
#   nullable    = false
# }
#
# variable "private_subnet_cidr" {
#   description = "CIDR block da subnet privada"
#   type        = string
#   nullable    = false
# }
#
# variable "public_subnet_zone" {
#   description = "Availability zone da subnet publica"
#   type        = string
#   nullable    = false
# }
#
# variable "private_subnet_zone" {
#   description = "Availability zone for the private subnet"
#   type        = string
#   nullable    = false
# }

/* #--------------- Envs de segurança --------------#*/
# variable "stack_name" {
#   description = "Nome do stack"
#   type        = string
# }

