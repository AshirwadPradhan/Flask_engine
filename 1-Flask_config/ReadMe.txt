
A Web Server Gateway Interface (WSGI) server implements the web server side of the WSGI interface for running Python web applications. 

WSGI Server/	----------------  [[Callable Object]] WSGI Application/
	Gateway ----------------				Framework
[[ interface for web    ]]				[[ Flask Application ]]
[[ servers, like apache ]]
[[ gunicorn etc.	]]

**app = Flask(__name__)
So this is the callable object which is called by WSGI server to the Flask app/framework.
WSGI gateway is used becoz native servers dont know how to run the python apps hence in order to make it run we need it. It is just a widely accepted standard
for python web apps to run on the server.[ Earlier mod_python was used].

Why use WSGI server?
--> WSGI gives you flexibility
	Application developers can swap out web stack components for others. For example, a developer can switch from Green Unicorn to uWSGI without modifying the application or framework that implements WSGI. 

--> WSGI servers promote scaling.
	Serving thousands of requests for dynamic content at once is the domain of WSGI servers, not frameworks. WSGI servers handle processing requests from the web server and deciding how to communicate those requests to an application framework's process.


**app.config['DEBUG'] = True
This is the config attribute of the flask object. making debug=True helps in reloading the webpage whenever any code changes are detected and also provides
very helpful Werkzeug debugger when something goes wrong.
There are different ways to handle config file
1--> we can create our own config file myconfig.cfg and fetch using this command
	app.config.from_pyfile('myconfig.cfg')
2--> from object,
	app.config.from_object('myapplication.default_settings') 
3--> from env var,
	app.config.from_envvar('PATH_TO_CONFIG_FILE')

We can also use class based settings for config file. As the apps grow larger, it is very helpful for housekeeping purposes. Using inheritance,
		class BaseConfig(object):    
			'Base config class'    
			SECRET_KEY = 'A random secret key'    
			DEBUG = True    
			TESTING = False    
			NEW_CONFIG_VARIABLE = 'my value'
		class ProductionConfig(BaseConfig):    
			'Production specific config'    
			DEBUG = False    
			SECRET_KEY = open('/path/to/secret/file').read()
		class StagingConfig(BaseConfig):    
			'Staging specific config'    
			DEBUG = True
		class DevelopmentConfig(BaseConfig):    
			'Development environment specific config'    
			DEBUG = True    
			TESTING = True    
			SECRET_KEY = 'Another random secret key'

# This is how we can use it
app.config.from_object('configuration.DevelopmentConfig')


**Organization of static files
my_app/
	-app.py
	-config.py
	-__init__.py
	-static/
		-css/
		-js/
		-images/
			-logo.png
And then we can use static files as shown,
1--> <img src='/static/images/logo.png'>

2--> app = Flask(__name__, static_folder='/path/to/static/folder')

3--> app = Flask(__name__, static_url_path='/differentstatic',    					static_folder='/path/to/static/folder' )
     <img src='/differentstatic/logo.png'>

4--> In Jinja we can use as follows,
	app = Flask(__name__, static_url_path='/differentstatic',    					static_folder='/path/to/static/folder')
	<img src='{{ url_for('static', filename="logo.png") }}'> 


**Composition of views and models[ Advanced Flask configuration ]
flask_app/
	-run.py
	-my_app/
		-__init__.py
		-hello/
			-__init__.py
			-models.py
			-views.py

1-->run.py
	from my_app import app 
	app.run(debug=True)

2-->my_app/__init__.py
	from flask import Flask 
	app = Flask(__name__)
	
	import my_app.hello.views

3-->my_app/hello/__init__.py
	# This will be empty

4-->my_app/hello/models.py
	# This has a non-persistent key-value store
	MESSAGES = {    'default': 'Hello to the World of Flask!', }

5-->my_app/hello/views.py
	from my_app import app 
	from my_app.hello.models import MESSAGES

	@app.route('/') 
	@app.route('/hello') 
	def hello_world():
		return MESSAGES['default']

	@app.route('/show/<key>') 
	def get_message(key):    
		return MESSAGES.get(key) or "%s not found!" % key

	@app.route('/add/<key>/<message>') 
	def add_or_update_message(key, message):    
		MESSAGES[key] = message    
		return "%s Added/Updated" % key

Then run the file 'python run.py'
[ The above code is not production ready ]


**Modular apps with blueprint
--Skipped for now---
It is same as organizing files given above but in a little different way.










