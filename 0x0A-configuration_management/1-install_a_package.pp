# This script install Flask version 2.1.0 usiing pip 3

exec { 'Flask':
  command => '/usr/bin/apt-get -y install Flask -v 2.5.0',
}
