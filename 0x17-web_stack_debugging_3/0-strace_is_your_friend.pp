$file_to_modify = '/var/www/html/wp-settings.php'

# Substitute "phpp" with "php" in the specified file

exec { 'substitute_line':
  command => "sed -i 's/phpp/php/g' ${file_to_modify}",
  path    => ['/bin', '/usr/bin']
}
