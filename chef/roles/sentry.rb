name "sentry-box"
description "Setup sentry server"

default_attributes(
	:postgresql => {
		:password => {
			:postgres => "md5305b26ef6df948d22b93b625e1340c5a"
		}
	}
)

run_list [
	"recipe[python]",
	"recipe[supervisor]",
	"recipe[postgresql::server]", 
	"recipe[postgresql::client]", 
	"recipe[postgresql::ruby]", 
	"recipe[sentry]"
]
