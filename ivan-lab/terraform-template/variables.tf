variable "project_name" {
  description = "Nome do projeto"
  type        = string
  default     = "Souths-Eagle"
}

variable "AWS_REGION" {
  description = "Região da AWS"
  type        = string
  default     = "us-east-1"
}

variable "AWS_ACCESS_KEY_ID" {
  type     = string
  nullable = false
}

variable "AWS_SECRET_ACCESS_KEY" {
  type     = string
  nullable = false
}

variable "AWS_SESSION_TOKEN" {
  type     = string
  nullable = false
}

variable "key_pair_name" {
  description = "Nome do par de chaves para acesso SSH"
  type        = string
  default     = "souths-eagle"
}

variable "default_role_name" {
  description = "Role default para utilizar no laboratório"
  type        = string
  default     = "LabRole"
}
