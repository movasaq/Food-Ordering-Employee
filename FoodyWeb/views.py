from FoodyWeb import web
from flask import send_from_directory, url_for, current_app, redirect

from FoodyConfig.config import STATUS, Media


@web.route("/Serve/<path:path>")
def Serve(path):
    """
    Serve Static files for development Mode (Only When APP_DEBUG=True)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Only In Debug Mode Serving Files for development Purposes
    """
    if STATUS:
        return send_from_directory(Media, path)  # flask serve
    else:
        return f"This File Only Can be Served Via Nginx WebServer,,, <A href='{current_app.config.get('DOMAIN')+path}'>{current_app.config.get('DOMAIN')+path}</A>", 400



@web.route("/")
def index_view():
    """
    Just redirect to user login page
    You can replace this with a nice and simple landing page for you company

        return render_template('path/to/landing page.html')
    """
    return redirect(url_for('auth.login'))
