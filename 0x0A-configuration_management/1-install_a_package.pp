# This script install Flask version 2.1.0 using pip
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip',
}
