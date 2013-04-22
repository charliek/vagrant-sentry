package "iptables-persistent" do
  action :install
end

directory "/etc/iptables" do
	mode "0640"
	owner "root"
	group "root"
	action :create
end

%w{v4 v6}.each do |version|
	template "/etc/iptables/rules.#{version}" do
	  source "rules.erb"
	  mode "0644"
	  owner "root"
	  group "root"
	end
end

service "iptables-persistent" do
	action :restart
end
