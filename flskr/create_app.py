from flask import Flask, redirect, url_for

def create_app():
    app = Flask(__name__)
    @app.route("/")
    def to_app():
        return redirect(url_for("app.ponto_app"))
    return app