# Define a resource class for managing pip packages
class { 'pip': }

# Define a package resource for Flask
package { 'Flask':
  ensure => '2.1.0',
  provider => 'pip3',
}
