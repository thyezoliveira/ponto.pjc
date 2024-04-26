from flskr import create_app
from flskr.views.core_view import test_bp

app = create_app()
app.register_blueprint(test_bp)

if __name__ == "__main__":
    app.run()

