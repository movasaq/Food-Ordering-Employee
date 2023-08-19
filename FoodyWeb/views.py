from FoodyWeb import web
from flask import redirect, url_for, send_from_directory, current_app

from FoodyConfig.config import STATUS, Media
from FoodyAdmin.model import SiteSetting


@web.route("/Serve/<path:path>")
def Serve(path):
    """
    This View Server Media Content
    Base of App Debug
    if debug is one this view itself serve media otherwise
    this view let nginx serve Static files
    """
    if STATUS:
        return send_from_directory(Media, path)  # flask serve
    else:
        return redirect(current_app.config.get("DOMAIN") + f'/Media/{path}')  # nginx serve
        # return send_from_directory(Media, path) # flask serve


@web.route("/logo.png")
def serve_app_logo():
    """
    this view serve app logo
    if there is no image set for app logo
     return default logo image
    """
    if (site := SiteSetting.query.filter_by(tag="setting").first()):
        if site.Logo:
            if not STATUS:
                return redirect(current_app.config.get("DOMAIN") + f'/Media/{site.Logo}')  # nginx serve
            else:
                return send_from_directory(Media, site.Logo)

    if not STATUS:
        return redirect(current_app.config.get("DOMAIN") + "/Media/logo.png")  # nginx serve

    return send_from_directory(Media, "logo.png")


@web.route("/")
def index_view():
    """
    Just redirect to user login page
    You can replace this with a nice and simple landing page for you company

        return render_template('path/to/landing page.html')
    """
    return redirect(url_for('auth.login'))
