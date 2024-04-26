from flskr import create_app
from flskr.views.core_view import app_bp

app = create_app()
app.register_blueprint(app_bp)

if __name__ == "__main__":
    app.run(debug=True)

