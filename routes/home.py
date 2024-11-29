from flask import render_template

def get_home_routes(app):

    @app.route('/home', methods=['GET'])
    def get_home_page():
        return render_template('index.html')