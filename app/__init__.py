import os
from flask import Flask, render_template, request, session, redirect
from flask_cors import CORS
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect, generate_csrf
from flask_login import LoginManager
from .models import db, User

# ✅ Blueprints
from .api.user_routes import user_routes
from .api.auth_routes import auth_routes
from .api.experience_routes import experience_routes
from .api.review_routes import review_routes
from .api.image_routes import image_routes

# ✅ Seed commands
from .seeds import seed_commands
from .config import Config

# ✅ Create Flask app
app = Flask(__name__, static_folder='../react-vite/dist', static_url_path='/')


# ✅ Login manager setup
login = LoginManager(app)
login.login_view = 'auth.unauthorized'


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


# ✅ Seed CLI command
app.cli.add_command(seed_commands)

# ✅ Load config + initialize extensions
app.config.from_object(Config)
db.init_app(app)
Migrate(app, db)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}}, supports_credentials=True)

# ✅ Register blueprints
app.register_blueprint(user_routes, url_prefix='/api/users')
app.register_blueprint(auth_routes, url_prefix='/api/auth')
app.register_blueprint(experience_routes, url_prefix='/api/experiences')
app.register_blueprint(review_routes, url_prefix='/api/reviews')
app.register_blueprint(image_routes, url_prefix='/api/images')


# ✅ Redirect HTTP → HTTPS in production
@app.before_request
def https_redirect():
    if os.environ.get('FLASK_ENV') == 'production':
        if request.headers.get('X-Forwarded-Proto') == 'http':
            url = request.url.replace('http://', 'https://', 1)
            code = 301
            return redirect(url, code=code)


# ✅ Inject CSRF token
# @app.after_request
# def inject_csrf_token(response):
#     csrf_token = generate_csrf()

#     # Detect if in production
#     is_prod = os.environ.get('FLASK_ENV') == 'production'

#     response.set_cookie(
#         'csrf_token',
#         csrf_token,
#         secure=is_prod,  # ✅ only secure in production (HTTPS)
#         samesite='Lax' if not is_prod else 'Strict',  # ✅ use Lax for dev
#         httponly=False
#     )
#     response.headers.set('X-CSRFToken', csrf_token)
#     return response
@app.after_request
def inject_csrf_token(response):
    csrf_token = generate_csrf()
    response.set_cookie(
        'csrf_token',
        csrf_token,
        secure=os.environ.get("FLASK_ENV") == "production",   # 👈 MATCHED
        samesite="None" if os.environ.get("FLASK_ENV") == "production" else "Lax",
        httponly=False
    )
    response.headers.set('X-CSRFToken', csrf_token)
    return response

# ✅ API route docs
@app.route("/api/docs")
def api_help():
    """
    Returns all API routes and their doc strings
    """
    acceptable_methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    route_list = {
        rule.rule: [[method for method in rule.methods if method in acceptable_methods],
                    app.view_functions[rule.endpoint].__doc__]
        for rule in app.url_map.iter_rules() if rule.endpoint != 'static'
    }
    return route_list


# ✅ Serve frontend React app
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def react_root(path):
    """
    This route will direct to the public directory in our
    react builds in the production environment for favicon
    or index.html requests
    """
    if path == 'favicon.ico':
        return app.send_from_directory('public', 'favicon.ico')
    return app.send_static_file('index.html')


# ✅ Catch-all for 404s (React SPA fallback)
@app.errorhandler(404)
def not_found(e):
    return app.send_static_file('index.html')
