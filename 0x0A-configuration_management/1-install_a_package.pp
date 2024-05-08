# Using Puppet, install flask from pip3
package { 'Install flask':
  ensure   	=> '2.1.0',
	name			=> 'flask',
  provider 	=> 'pip3',
}