from flask import request, jsonify
from .database import add_app, get_app_by_id, delete_app

def register_routes(app):
    @app.route('/add-app', methods=['POST'])
    def add_app_route():
        data = request.get_json()
        app_name = data['app_name']
        version = data['version']
        description = data['description']
        add_app(app_name, version, description)
        return jsonify({"message": "App added successfully"}), 201

    @app.route('/get-app/<int:id>', methods=['GET'])
    def get_app_route(id):
        app = get_app_by_id(id)
        if app:
            return jsonify({
                'id': app.id,
                'app_name': app.app_name,
                'version': app.version,
                'description': app.description
            }), 200
        return jsonify({"message": "App not found"}), 404

    @app.route('/delete-app/<int:id>', methods=['DELETE'])
    def delete_app_route(id):
        delete_app(id)
        return jsonify({"message": "App deleted successfully"}), 200
