#!/usr/bin/python
'''
A basic bottle app skeleton
'''

import bottle
from bottle import template
import os


app = application = bottle.Bottle()
bottle.TEMPLATE_PATH.insert(0, os.path.dirname(os.path.abspath(__file__)) +"/views")
bottle.TEMPLATE_PATH.insert(0, os.path.dirname(os.path.abspath(__file__)))
bottle.TEMPLATE_PATH.insert(0, '/data/Dropbox/python/web/bottlebasis/views')

@app.route('/static/<filename:path>')
def static(filename):
	'''
	Serve static files
	'''
	try:
		return bottle.static_file(filename, root='{}/static'.format(os.path.dirname(__file__)))
		#return '{}/static'.format(os.path.dirname(os.path.abspath(__file__)))
	except:
		return '{}/static'.format(os.path.dirname(os.path.abspath(__file__)))
	##return bottle.static_file(filename, root='{}/static'.format(conf.get('bottle', 'root_path')))

@app.route('/')
def show_index():
	'''
	The front "index" page
	'''
	return 'Hello'

@app.route('/page/<page_name>')
def show_page(page_name):
	'''
	Return a page that has been rendered using a template
	'''
	#return str(bottle.TEMPLATE_PATH) ##+ 
	bottle.TEMPLATE_PATH.insert(0, os.path.dirname(os.path.abspath(__file__)) +"/views")
	bottle.TEMPLATE_PATH.insert(0, os.path.dirname(os.path.abspath(__file__)))
	bottle.TEMPLATE_PATH.insert(0, '/data/Dropbox/python/web/bottlebasis/views')
	try:
		return template('page', page_name=page_name)
	except Exception, e:
		return "<p>Error: %s</p> <p>%s</p>" % (str(e), os.getcwd())

class StripPathMiddleware(object):
	'''
	Get that slash out of the request
	'''
	def __init__(self, a):
		self.a = a
	def __call__(self, e, h):
		e['PATH_INFO'] = e['PATH_INFO'].rstrip('/')
		return self.a(e, h)

if __name__ == '__main__':
	bottle.run(app=app, host='0.0.0.0', port=8080)
