### Performance tests

siege_sync_proxy_slow:
	# Boots up single process using python asyncio (gevents) to process requests
	siege -c 16 -t 4s http://localhost:5000/slow | grep -v HTTP*

siege_fast:
	# Boots up single process using python asyncio (gevents) to process requests
	siege -c 16 -t 4s http://localhost:5000/fast | grep -v HTTP*
