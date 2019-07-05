### Run proxy server in different modes

run_proxy_sync:
	# Boots up N processes where N is # workers (e.g. `-w 4` means 4 processes)
	gunicorn -w 4 -b 127.0.0.1:4000 proxy.proxy:app


### Run third party server in different modes

run_third_party_sync:
	# Boots up 4 processes which is spec'd by number of workers (e.g. `-w 4`
	#   means 4 processes)
	# Max num requests = number of workers
	gunicorn -w 4 -b 127.0.0.1:5000 third_party.third_party:app

run_third_party_asyncio:
	# Boots up single process using python asyncio (gevents) to process requests
	# Concurrency not limited by threads or processes
	gunicorn -w 1 -k gevent -b 127.0.0.1:5000 third_party.third_party:app


### Performance tests

siege_slow:
	# Boots up single process using python asyncio (gevents) to process requests
	siege -c 4 -t 4s http://localhost:5000/slow | grep -v HTTP*

siege_fast:
	# Boots up single process using python asyncio (gevents) to process requests
	siege -c 4 -t 4s http://localhost:5000/fast | grep -v HTTP*
