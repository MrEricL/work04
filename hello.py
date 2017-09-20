from flask import Flask

my_app=Flask(__name__)

@my_app.route('/')
def root():
	return "<h1> Hi </h1>"

@my_app.route('/foo')
def rootwo():
	return "<i> Hi Part 2 </i>"

@my_app.route('/goo')
def roothree():
	return "<b> Hi Part 3 </b>"

if __name__ == '__main__':
	my_app.debug = True
	my_app.run()



