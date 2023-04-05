#!/usr/bin/env bash
# create recursive child folders & deploy static file

sudo apt-get -y update
sudo apt-get -y install nginx
sudo apt-get -y install ufw

sudo ufw allow "Nginx HTTP"
sudo mkdir -p /data/web_static/shared /data/web_static/releases/test

data="
<html>
    <body>
   	<h1>Welcome To HBNB</h1>
    </body>
</html>
"
echo "$data" > /data/web_static/releases/test/index.html
sudo chown -hR ubuntu:ubuntu /data/

if [ -d "/data/web_static/current" ];
then
    sudo rm -rf /data/web_static/current
fi
sudo ln -s /data/web_static/releases/test/ /data/web_static/current
server_config="
server {
	listen 80 default_server;
	listen [::]:80 default_server;
	root /var/www/html;
	index index.html index.htm index.nginx-debian.html;
	server_name _;
	add_header X-Served-By \$hostname;
	location / {
		try_files \$uri \$uri/ =404;
	}
	location /hbnb_static/ {
		alias /data/web_static/current/;
	}
}"

echo "$server_config" > /etc/nginx/sites-enabled/default
#sudo ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default
sudo service nginx restart
