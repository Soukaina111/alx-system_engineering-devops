# This script install Flask version 2.1.0 usiing pip 3

exec { 'install_flask':
  command => '/usr/bin/pip3 install flask==2.1.0',
}
