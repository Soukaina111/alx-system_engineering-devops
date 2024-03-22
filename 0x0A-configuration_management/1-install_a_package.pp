# This script install Flask version 2.1.0 usiing pip 3

exec { 'install_flask':
  command => '/usr/bin/apt-get -y install flask== 2.1.0',
}
