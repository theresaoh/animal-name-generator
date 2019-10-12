from flask import Flask, render_template, jsonify

names = ['Nap Time All-Star', "Phil", "Theresa"]

app = Flask(__name__,
    static_folder = "./dist/static",
    template_folder = "./dist"
    )

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

@app.route('/names', methods=['GET'])
def serve_all_names():
    return jsonify({"results": names})

if __name__ == "__main__":
    app.run(debug = True)