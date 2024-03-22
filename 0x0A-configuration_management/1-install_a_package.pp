# This script install Flask version 2.1.0 using pip
exec { 'install_puppet_lint':
  command => '/usr/bin/apt-get -y install puppet-lint=2.5.0',
}
