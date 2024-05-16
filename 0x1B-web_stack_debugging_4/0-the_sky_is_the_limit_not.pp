# This script fixex the issue about the config files to have 0 failed requests
 exec { 'nginx fix':
   onlyif   => 'test -e /etc/default/nginx',
     command  => "sed -i s/'-n 15'/'-n 4096'/g /etc/default/nginx;  service nginx restart",
       provider => 'shell'
       }
