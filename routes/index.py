from flask import redirect

def get_index_routes(app):

    @app.route('/', methods=['GET'])
    def get_root_page():
        return redirect('/home')