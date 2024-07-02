# The Puppet script to install and configure nginx

package { 'nginx':
  ensure => 'present',
}

exec { 'update_and_install_nginx':
  command  => 'sudo apt-get update && sudo apt-get -y install nginx',
  provider => shell,
}

exec { 'create_hello_world_page':
  command  => 'echo "Hello World!" | sudo tee /var/www/html/index.html',
  provider => shell,
}

exec { 'configure_redirect':
  command  => 'sudo sed -i "s/listen 80 default_server;/listen 80 default_server;\\n\\tlocation \/redirect_me {\\n\\t\\treturn 301 https:\/\/orbidmedia.co.za\/;\\n\\t}/" /etc/nginx/sites-available/default',
  provider => shell,
}

exec { 'restart_nginx':
  command  => 'sudo service nginx restart',
  provider => shell,
}
