# what causes the problem was the wrong extension`phpp` instead of `php` here is how to fix it

exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
