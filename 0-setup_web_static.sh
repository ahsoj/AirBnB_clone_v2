#!/usr/bin/env bash
# create recursive child folders & deploy static file

sudo apt-get -y update
if [ ! command -v nginx &> /dev/null];
then
    #sudo apt-get -y install ufw
    sudo apt-get -y install nginx
fi
sudo ufw allow "Nginx HTTP"

if [ ! -d "/data/web_static"];
then
    sudo mkdir -p /data/web_static/shared /data/web_static/releases/test
fi
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
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
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

echo "$server_config" > /etc/nginx/sites-available/default
sudo ln -sf /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default
sudo service nginx restart
