from bottle import route, view


@route("/")
@view("index")
def index():
    return {}

