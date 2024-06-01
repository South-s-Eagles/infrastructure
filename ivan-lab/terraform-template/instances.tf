# resource "aws_instance" "spark_instance" {
#   ami           = var.ami_id
#   instance_type = var.instance_type
#   subnet_id     = aws_subnet.public.id
#   key_name      = var.key_pair_name
#   vpc_security_group_ids = [
#     aws_security_group.http_sg.id,
#     aws_security_group.ssh_sg.id
#   ]
#   depends_on = [
#     aws_route_table_association.public_subnet_association,
#     aws_security_group.http_sg,
#     aws_security_group.ssh_sg
#   ]
#   user_data = <<-EOF
#     #!/bin/bash
#     amazon-linux-extras install java-openjdk11 -y
#     curl -O https://dlcdn.apache.org/spark/spark-3.5.1/spark-3.5.1-bin-hadoop3.tgz
#     tar xzf spark-3.5.1-bin-hadoop3.tgz -C /usr/local --owner root --group root --no-same-owner
#     rm -rf spark-3.5.1-bin-hadoop3.tgz
#     mv /usr/local/spark-3.5.1-bin-hadoop3 /usr/local/spark
#     pip3 install pyspark --no-cache-dir
#     pip3 install jupyterlab --no-cache-dir
#     touch /lib/systemd/system/jupyter.service
#     echo "[Unit]" >> /lib/systemd/system/jupyter.service
#     echo "Description=Jupyter Notebook" >> /lib/systemd/system/jupyter.service
#     echo "[Service]" >> /lib/systemd/system/jupyter.service
#     echo "Type=simple" >> /lib/systemd/system/jupyter.service
#     echo "ExecStart=/opt/jupyter/script/start.sh" >> /lib/systemd/system/jupyter.service
#     echo "Restart=always" >> /lib/systemd/system/jupyter.service
#     echo "RestartSec=10" >> /lib/systemd/system/jupyter.service
#     echo "[Install]" >> /lib/systemd/system/jupyter.service
#     echo "WantedBy=multi-user.target" >> /lib/systemd/system/jupyter.service
#     mkdir /opt/jupyter
#     mkdir /opt/jupyter/notebook
#     mkdir /opt/jupyter/script
#     touch /opt/jupyter/script/start.sh
#     echo '#!/bin/bash' >> /opt/jupyter/script/start.sh
#     echo '/usr/bin/python3 -m notebook --NotebookApp.notebook_dir=/opt/jupyter/notebook --NotebookApp.password=$(/usr/bin/python3 -c "from notebook.auth import passwd; print(passwd(\"urubu100\"))")  --allow-root --ip 0.0.0.0 --port 80' >> /opt/jupyter/script/start.sh
#     chmod +x /opt/jupyter/script/start.sh
#     systemctl daemon-reload
#     systemctl start jupyter
#     systemctl enable jupyter
#   EOF

#   tags = {
#     Name = "Spark Instance"
#   }
# }
