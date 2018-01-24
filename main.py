from flask import Flask,  render_template
from flask import Blueprint
from flask import request
from flask_sse import sse
from channel import channel



app = Flask(__name__)
app.config["REDIS_URL"] = "redis://localhost"
app.register_blueprint(sse, url_prefix='/stream')
app.register_blueprint(channel, url_prefix='/channel')




@app.route("/")
def page():
    return render_template("login.html")

@app.route("/main/<username>")
def main_page(username):
	return render_template("main2.html", name=username)


@app.route("/wait/<Cid>")
def wait_page(Cid):
	return render_template("wait.html", name=Cid)



@app.route("/join/<Cid>")
def join_page(Cid):
	return render_template("join.html", name=Cid)


# @app.route('/<path:path>')
# def static_file(path):
#     return app.send_static_file(path)

# @app.route("/", methods=['POST'])
# def hello():
# 	print "Hello World!"
# 	print "req:  ", request.data
# 	sse.publish({"message": "Hello!"}, type='greeting')
# 	return "resssponsee main"

