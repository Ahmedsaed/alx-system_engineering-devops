# create a file: /tmp/school

file { 'school':
  ensure  => file,
  path    => '/tmp/school',
  mode    => '0744',
  group   => 'www-data',
  owner   => 'www-data',
  content => 'I love Puppet',
}
