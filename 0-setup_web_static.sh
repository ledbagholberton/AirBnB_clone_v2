#!/usr/bin/env bash
#Creation of files and others for web static
sudo apt-get update -y
sudo apt-get install nginx -y
sudo rm -f /data/web_static/current
sudo mkdir data
sudo cd data
sudo mkdir web_static
sudo cd web_static
sudo mkdir releases shared
sudo cd releases
sudo mkdir test
sudo echo "<html>
         <head>
         </head>
         <body>
             Holberton School
         </body>
      </html>" | /data/web_static/releases/test/index.html
sudo ln -s  /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i "40i location /hbnb_static/ {\n\talias /data/web_static/current;\n\t}" /etc/nginx/sites-enable/default 
sudo service nginx restart
