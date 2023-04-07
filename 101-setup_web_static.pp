# Redo the task #0 but by using Puppet:
exec { 'sudo apt -y update' : }
-> package { 'nginx':
  ensure => installed,
}
$directories = split('/data/web_static_releases/test', '/')
each($directories) |$directory| {
  if ! defined(File[$directory]) {
    file { $directory:
      ensure => directory
    }
  }
}
-> file { '/data/web_static/shared':
  ensure => 'directory'
}
-> file { '/data/web_static/releases/test/index.html':
  ensure  => 'present',
  content => "<h1>Welcome to Holberton</h1>"
}
-> file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test'
}
-> exec { 'chown -R ubuntu:ubuntu /data/':
  path => '/usr/bin/:/usr/local/bin/:/bin/'
}

$directories = split('/var/www/html', '/')
each($directories) |$directory| {
  if ! defined(File[$directory]) {
    file { $directory:
      ensure => directory
    }
  }
}
-> file { '/var/www/html/index.html':
  ensure  => 'present',
  content => "<h1>Welcome to Holberton</h1>"
}
exec { 'nginx_conf':
  environment => ['data=\ \tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n'],
  command     => 'sed -i "39i $data" /etc/nginx/sites-enabled/default',
  path        => '/usr/bin:/usr/sbin:/bin:/usr/local/bin'
}
-> service { 'nginx':
  ensure => running,
}
