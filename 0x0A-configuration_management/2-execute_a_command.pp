#This script kill a process named "killmenow"
exec { 'kill_process':
  command => 'pkill killmenow',
  onlyif  => 'pgrep killmenow',
}
