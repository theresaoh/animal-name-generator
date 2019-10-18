from flask import Flask, render_template
from namesAPI import names_api

app = Flask(__name__,
    static_folder = "./dist/static",
    template_folder = "./dist"
)

app.register_blueprint(names_api)

@app.route('/')
def serve_vue_app():
    """
    Serve our Vue App
    """
    return render_template('index.html')

@app.after_request
def add_header(req):
    """
    Clear Cache for hot-reloading
    """
    req.headers["Cache-Control"] = "no-cache"
    return req

if __name__ == "__main__":
    app.run(debug = True)