import flask
from functools import wraps


def login_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        auth=flask.request.authorization
        if auth and auth.username == "bharath" and auth.password == "password1":
            return f(*args, **kwargs)
        return flask.make_response("Could not verify your login !" , 401 , {'WWW-Authenticate':'Basic realm="Login Required !"'})
    return decorator



app=flask.Flask(__name__)
app.config["DEBUG"]=True
app.config["TOKEN"]="Bharathkarkera"


@app.route('/',methods=["GET"])
@login_required
def root():
    return 'You are logged in!'

@app.route('/protect',methods=["GET"])
def protected():
    return ''


@app.route('/unprotected',methods=["GET"])
def unprotected():
    return ''


app.run(host="0.0.0.0")
