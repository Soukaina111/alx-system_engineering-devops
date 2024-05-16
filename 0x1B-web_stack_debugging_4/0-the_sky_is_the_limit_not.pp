# This script fixex the issue about the config files to have 0 failed requests
exec { 'nginx ulimits fix':
  onlyif   => 'test -e /etc/default/nginx',
  command  => "sed -i 's/^#*ULIMITS/#ULIMITS/g' /etc/default/nginx; service nginx restart",
  provider => 'shell',
}
