template "#{node[:nginx][:dir]}/sites-available/sentry.conf" do
  source 'nginx.conf.erb'
  owner 'root'
  group 'root'
  mode 00644
  notifies :reload, "service[nginx]"
end

nginx_site "sentry.conf"

nginx_site "default" do
  enable false
end


user "www-sentry" do
  comment "user account that sentry will run under"
  system true
  shell "/bin/bash"
end

group "www-server" do
  members "www-sentry"
end

directory "/www/sentry" do
  owner 'root'
  group 'www-server'
  mode "0755"
  recursive true
  action :create
end

python_virtualenv "/www/sentry" do
  owner "root"
  group "www-server"
  action :create
end

python_pip "sentry[postgres]" do
  virtualenv "/www/sentry"
end

template "/etc/sentry.conf.py" do
	source "sentry.conf.py.erb"
	owner "root"
	group "root"
	mode 00644
end


postgresql_connection_info = {:host => "localhost",
                              :port => 5432,
                              :username => 'postgres',
                              :password => 'password1'}

postgresql_database 'sentry' do
  connection postgresql_connection_info
  action :create
end

postgresql_database_user 'www-sentry' do
  connection postgresql_connection_info
  database_name 'sentry'
  host '%'
  password 'password1'
  privileges [:all]
  action [:create, :grant]
end

# On first install you may need to bootstrap users by doing:
# * /www/sentry/bin/sentry --config=/etc/sentry.conf.py createsuperuser
# * /www/sentry/bin/sentry --config=/etc/sentry.conf.py repair --owner=<username>

execute "sentry migrations" do
  command "/www/sentry/bin/sentry --config=/etc/sentry.conf.py upgrade --noinput"
end

supervisor_service "sentry-web" do
  action :enable
  autostart true
  autorestart true
  redirect_stderr true
  user "www-sentry"
  directory "/www/sentry/"
  command "/www/sentry/bin/sentry --config=/etc/sentry.conf.py start http"
end
