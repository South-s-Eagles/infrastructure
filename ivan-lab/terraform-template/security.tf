# resource "aws_security_group" "http_sg" {
#   name        = "${var.stack_name}-http-sg"
#   description = "Allow HTTP traffic"
#   vpc_id      =  aws_vpc.main.id

#   ingress {
#     from_port   = 80
#     to_port     = 80
#     protocol    = "tcp"
#     cidr_blocks = ["0.0.0.0/0"]
#   }

#   egress {
#     from_port   = 0
#     to_port     = 0
#     protocol    = "-1"
#     cidr_blocks = ["0.0.0.0/0"]
#   }

#   tags = {
#     Name = "${var.stack_name}-http-sg"
#   }
# }

# resource "aws_security_group" "ssh_sg" {
#   name        = "${var.stack_name}-ssh-sg"
#   description = "Allow SSH traffic"
#   vpc_id      = aws_vpc.main.id

#   ingress {
#     from_port   = 22
#     to_port     = 22
#     protocol    = "tcp"
#     cidr_blocks = ["0.0.0.0/0"]
#   }

#   egress {
#     from_port   = 0
#     to_port     = 0
#     protocol    = "-1"
#     cidr_blocks = ["0.0.0.0/0"]
#   }

#   tags = {
#     Name = "${var.stack_name}-ssh-sg"
#   }
# }
