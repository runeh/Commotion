from os.path import dirname, join

import bottle

from views import *

bottle.TEMPLATE_PATH.append(join(dirname(__file__), "templates"))

def main():
	bottle.debug(True)
	bottle.run(host='localhost', port=8080, reloader=True)


