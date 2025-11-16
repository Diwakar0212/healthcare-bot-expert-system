from flask import Flask, request, jsonify
from flask_cors import CORS
from expert_system import MedicalExpertSystem
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Initialize the expert system
expert_system = MedicalExpertSystem()

# Store conversation sessions
sessions = {}

@app.route('/api/chat', methods=['POST'])
def chat():
    """Handle chat interactions"""
    data = request.json
    session_id = data.get('session_id')
    user_message = data.get('message', '').strip()
    
    if not session_id:
        session_id = f"session_{datetime.now().timestamp()}"
    
    if session_id not in sessions:
        sessions[session_id] = {
            'symptoms': [],
            'history': [],
            'state': 'initial'
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

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
