from flask import Flask, request, jsonify, session
from flask_cors import CORS
from expert_system import MedicalExpertSystem
from user_database import UserDatabase
from datetime import datetime
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(32)  # Generate secret key for sessions
CORS(app, supports_credentials=True)

# Initialize the expert system and user database
expert_system = MedicalExpertSystem()
user_db = UserDatabase()

# Store conversation sessions
sessions = {}

@app.route('/api/chat', methods=['POST'])
def chat():
    """Handle chat interactions"""
    data = request.json
    session_id = data.get('session_id')
    user_message = data.get('message', '').strip()
    username = data.get('username')  # Get username for history tracking
    
    if not session_id:
        session_id = f"session_{datetime.now().timestamp()}"
    
    if session_id not in sessions:
        sessions[session_id] = {
            'symptoms': [],
            'history': [],
            'state': 'initial',
            'username': username
        }
    
    session = sessions[session_id]
    
    # Add user message to history
    session['history'].append({
        'role': 'user',
        'message': user_message,
        'timestamp': datetime.now().isoformat()
    })
    
    # Process the message and get response
    response = expert_system.process_input(user_message, session)
    
    # Add bot response to history
    session['history'].append({
        'role': 'bot',
        'message': response['message'],
        'timestamp': datetime.now().isoformat()
    })
    
    # Save diagnosis to user's medical history if diagnosis is complete and user is logged in
    if response.get('diagnosis') and username and session['state'] == 'diagnosis_complete':
        diagnosis_data = {
            'session_id': session_id,
            'symptoms': session['symptoms'],
            'diagnoses': response['diagnosis']
        }
        user_db.add_diagnosis_to_history(username, diagnosis_data)
    
    return jsonify({
        'session_id': session_id,
        'message': response['message'],
        'diagnosis': response.get('diagnosis'),
        'suggestions': response.get('suggestions', []),
        'state': session['state']
    })

@app.route('/api/reset', methods=['POST'])
def reset_session():
    """Reset a conversation session"""
    data = request.json
    session_id = data.get('session_id')
    
    if session_id and session_id in sessions:
        del sessions[session_id]
    
    return jsonify({'message': 'Session reset successfully'})

@app.route('/api/symptoms', methods=['GET'])
def get_symptoms():
    """Get list of all available symptoms"""
    return jsonify({
        'symptoms': expert_system.get_all_symptoms()
    })

@app.route('/api/conditions', methods=['GET'])
def get_conditions():
    """Get list of all conditions"""
    return jsonify({
        'conditions': expert_system.get_all_conditions()
    })

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'timestamp': datetime.now().isoformat()})

@app.route('/api/auth/signup', methods=['POST'])
def signup():
    """User registration endpoint"""
    data = request.json
    username = data.get('username', '').strip()
    email = data.get('email', '').strip()
    password = data.get('password', '')
    
    if not username or not email or not password:
        return jsonify({'success': False, 'message': 'All fields are required'}), 400
    
    success, message = user_db.create_user(username, email, password)
    
    if success:
        return jsonify({'success': True, 'message': message, 'username': username}), 201
    else:
        return jsonify({'success': False, 'message': message}), 400

@app.route('/api/auth/login', methods=['POST'])
def login():
    """User login endpoint"""
    data = request.json
    username = data.get('username', '').strip()
    password = data.get('password', '')
    
    if not username or not password:
        return jsonify({'success': False, 'message': 'Username and password required'}), 400
    
    success, message = user_db.authenticate_user(username, password)
    
    if success:
        user_data = user_db.get_user(username)
        return jsonify({
            'success': True,
            'message': message,
            'user': {
                'username': username,
                'email': user_data.get('email'),
                'created_at': user_data.get('created_at')
            }
        }), 200
    else:
        return jsonify({'success': False, 'message': message}), 401

@app.route('/api/auth/logout', methods=['POST'])
def logout():
    """User logout endpoint"""
    return jsonify({'success': True, 'message': 'Logged out successfully'}), 200

@app.route('/api/history/<username>', methods=['GET'])
def get_history(username):
    """Get user's medical history"""
    history = user_db.get_medical_history(username)
    return jsonify({
        'success': True,
        'history': history,
        'count': len(history)
    })

@app.route('/api/history/<username>', methods=['POST'])
def save_diagnosis(username):
    """Save diagnosis to user's medical history"""
    data = request.json
    success, message = user_db.add_diagnosis_to_history(username, data)
    
    if success:
        return jsonify({'success': True, 'message': message}), 201
    else:
        return jsonify({'success': False, 'message': message}), 400

@app.route('/api/history/<username>', methods=['DELETE'])
def clear_history(username):
    """Clear user's medical history"""
    success = user_db.clear_history(username)
    
    if success:
        return jsonify({'success': True, 'message': 'History cleared'}), 200
    else:
        return jsonify({'success': False, 'message': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
