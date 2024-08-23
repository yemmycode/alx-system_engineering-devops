# This script enhances the traffic capacity of an Nginx server.

# Increase the ULIMIT for the default file
exec { 'fix-for-nginx-ulimit':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => ['/usr/local/bin', '/bin'],
}

# Restart Nginx
exec { 'nginx-restart':
  command => 'nginx restart',
  path    => ['/etc/init.d'],
}
