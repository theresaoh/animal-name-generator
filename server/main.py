from app import create_app
from models import setup_database
from flask import render_template

def add_vue_routes(app):
    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def catch_all(path):
        return render_template("index.html")


    @app.after_request
    def add_header(req):
        """
        Clear Cache for hot-reloading
        """
        req.headers["Cache-Control"] = "no-cache"
        return req

if __name__ == "__main__":
    app = create_app()
    add_vue_routes(app)
    setup_database(app)
    app.run(debug = True)