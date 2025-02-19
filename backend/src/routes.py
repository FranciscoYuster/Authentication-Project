from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from datetime import timedelta
from models import User, Profile

api = Blueprint("api", __name__)

@api.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    email = data.get('email')
    password = data.get('password')
    
    if not email:
        return jsonify({"fail": "Email is required"}), 400  # Mejor usar 400 (Bad Request)
     
    if not password:
        return jsonify({"error": "Password is required"}), 400

    found = User.query.filter_by(email=email).first()
    if found:
        return jsonify({"fail": "User already exists"}), 409

   

    profile = Profile()
    user = User()
    user.email = email
    user.set_password(password)
    user.profile = profile

    user.save()
    if not user:
        return jsonify({"error": "Error"})

    
    return jsonify({"success": "Thanks for register, please login"}), 200

@api.route('/login', methods=['POST'])
def login():

    email = request.json.get('email')
    password = request.json.get('password')
    
    if not email:
        return jsonify({"fail": "Email is required"}), 400  # Mejor usar 400 (Bad Request)
     
    if not password:
        return jsonify({"error": "Password is required"}), 400
    
    user = User.query.filter_by(email=email).first()

    if not user:
        return jsonify({"error": "Credentials are incorrects!"}), 401
    
    if not user.verify_password(password):
        return jsonify({"error": "Credentials are incorrects!"}), 401
    

    # expires = timedelta(min=15)
    # access_token = create_access_token(identity=str(user.id), expires_delta=expires )
    access_token = create_access_token(identity=str(user.id))


    datos = {
        "access_token": access_token,
        "user": user.serialize()
    }


    return jsonify(datos),200
    


    

@api.route('/profile', methods=['GET'])
@jwt_required()  # ruta protegida
def profile():

    id = get_jwt_identity() 
    user = User.query.get(id)

    if not user:
        return jsonify({"error": "User not found"}),401


    return jsonify({
        "status": "success!",
          "user": user.serialize()
        }),200

@api.route('/profile', methods=['PUT'])
@jwt_required()
def update_profile():
    id = get_jwt_identity() 
    user = User.query.get(id)

    if not user:
        return jsonify({"error": "User not found"}),401

    bio = request.json.get('bio')
    github = request.json.get('github')
    facebook = request.json.get('facebook')
    instagram = request.json.get('instagram')
    twitter = request.json.get('twitter')
    avatar = request.json.get('avatar')

    if bio:
        user.profile.bio = bio
    if github:
        user.profile.github = github
    if facebook:
        user.profile.facebook = facebook
    if instagram:
        user.profile.instagram = instagram
    if twitter:
        user.profile.twitter = twitter
    if avatar:
        user.profile.avatar = avatar
    
    user.save()

    return jsonify({
        "status": "success",
        "user updated": user.serialize()
    }),200
