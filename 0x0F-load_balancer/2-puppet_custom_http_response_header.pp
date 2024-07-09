# Puppet script to automate the creation of a custom HTTP header response.
# The custom HTTP header should be named X-Served-By.
# The value of the custom HTTP header should be the hostname of the server running Nginx.

# Ensure package list is updated
exec { 'update':
  command => '/usr/bin/apt-get update',
}

# Ensure Nginx is installed
package { 'nginx':
  ensure => present,
  require => Exec['update'],
}

# Add custom HTTP header to Nginx configuration
file_line { 'http_header':
  path  => '/etc/nginx/nginx.conf',
  line  => "http {\n\tadd_header X-Served-By \"${hostname}\";",
  match => 'http {',
  require => Package['nginx'],
}

# Ensure Nginx service is started
exec { 'start_nginx':
  command => '/usr/sbin/service nginx start',
  subscribe => File_line['http_header'],
}
