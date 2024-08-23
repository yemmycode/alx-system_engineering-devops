# This script adjusts file limits for the holberton user, ensuring seamless login and file access.

# Set the hard file limit for the holberton user to 50,000
exec { 'set-hard-file-limit-for-holberton':
  command => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf',
  path    => ['/usr/local/bin', '/bin']
}

# Set the soft file limit for the holberton user to 50,000
exec { 'set-soft-file-limit-for-holberton':
  command => 'sed -i "/holberton soft/s/4/50000/" /etc/security/limits.conf',
  path    => ['/usr/local/bin', '/bin']
}
