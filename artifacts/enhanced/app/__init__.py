from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)  # Allows the front-end to communicate with the back-end
    
    # Basic configuration
    app.config['SECRET_KEY'] = 'cs499-milestone-two-secret-key'
    
    # Import and register routes
    from .routes import bp
    app.register_blueprint(bp)
    
    print("✅ Flask app created successfully! (Milestone Two Enhancement)")
    return app