# Puppet configuration for SSH client settings
file_line { 'Identity file setting':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '    IdentityFile ~/.ssh/school',
}

file_line { 'Disable password login setting':
    path    => '/etc/ssh/ssh_config',
    line    => '    PasswordAuthentication no',
}
