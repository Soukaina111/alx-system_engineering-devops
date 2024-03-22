#This script kill a process named "killmenow"

exec { 'kill_process':
	command => 'pkill killmenow',
	provider => 'shell',
	onlyif  => 'pgrep killmenow',
}
