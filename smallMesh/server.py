from flask import Flask

app = Flask(__name__)


@app.route("/")
def root():
	msg = '''Welcome to my server.
This is a P2P server that works using threads\n\n'''
	return msg
    

if __name__ == '__main__':
	app.run('0.0.0.0',5000)
