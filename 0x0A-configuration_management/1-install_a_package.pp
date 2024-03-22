# This script installs flask from pip3 verseion
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
