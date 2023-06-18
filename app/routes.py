from app import app


@app.route("/<name>")
def index(name):
    return f"Hello {name}!"
