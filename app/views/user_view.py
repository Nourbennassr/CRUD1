from flask import request, jsonify
from app.models.user import User
from app import app

@app.route('/users', methods=['GET'])
def get_users():
    users = User.get_all()
    result = []
    for user in users:
        result.append({
            'username': user['username'],
            'email': user['email'],
             '_id': str(user['_id'])
            
        })
    return jsonify(result)

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    username = data['username']
    email = data['email']
    user = User(username, email)
    user.save()
    return jsonify({'message': 'User created successfully'})

@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = User.get_by_id(user_id)
    if user:
        result = {
            'username': user['username'],
            'email': user['email']
        }
        return jsonify(result)
    return jsonify({'message': 'User not found'})

@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.get_by_id(user_id)
    if user:
        data = request.get_json()
        username = data['username']
        email = data['email']
        updated_user = User(username, email)
        updated_user.update(user_id)
        return jsonify({'message': 'User updated successfully'})
    return jsonify({'message': 'User not found'})

@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.get_by_id(user_id)
    if user:
        User.delete(user_id)
        return jsonify({'message': 'User deleted successfully'})
    return jsonify({'message': 'User not found'})