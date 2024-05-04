# Puppet script to create ssh config file
file_line { 'Turn off passwd auth':
	ensure	=> 'present',
	path		=> '/etc/ssh/ssh_config',
	line		=> '	PasswordAuthentication n',
}

file_line { 'Declare identify file':
	ensure	=> 'present',
	path		=> '/etc/ssh/ssh_config',
	line		=> '	IdentityFile ~/.ssh/school',
}
