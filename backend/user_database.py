import json
import os
from datetime import datetime

class UserDatabase:
    """Simple JSON-based user database for authentication and history"""
    
    def __init__(self, db_path='users_db.json'):
        self.db_path = db_path
        self.users = self._load_database()
    
    def _load_database(self):
        """Load users from JSON file"""
        if os.path.exists(self.db_path):
            try:
                with open(self.db_path, 'r') as f:
                    return json.load(f)
            except:
                return {}
        return {}
    
    def _save_database(self):
        """Save users to JSON file"""
        with open(self.db_path, 'w') as f:
            json.dump(self.users, f, indent=2)
    
    def create_user(self, username, email, password):
        """Create a new user"""
        if username in self.users:
            return False, "Username already exists"
        
        if any(user.get('email') == email for user in self.users.values()):
            return False, "Email already registered"
        
        self.users[username] = {
            'email': email,
            'password': password,  # In production, use proper password hashing
            'created_at': datetime.now().isoformat(),
            'medical_history': []
        }
        self._save_database()
        return True, "User created successfully"
    
    def authenticate_user(self, username, password):
        """Authenticate a user"""
        if username not in self.users:
            return False, "User not found"
        
        if self.users[username]['password'] != password:
            return False, "Invalid password"
        
        return True, "Authentication successful"
    
    def get_user(self, username):
        """Get user data"""
        return self.users.get(username)
    
    def add_diagnosis_to_history(self, username, diagnosis_data):
        """Add a diagnosis to user's medical history"""
        if username not in self.users:
            return False, "User not found"
        
        history_entry = {
            'timestamp': datetime.now().isoformat(),
            'symptoms': diagnosis_data.get('symptoms', []),
            'diagnoses': diagnosis_data.get('diagnoses', []),
            'session_id': diagnosis_data.get('session_id', '')
        }
        
        self.users[username]['medical_history'].append(history_entry)
        self._save_database()
        return True, "Diagnosis added to history"
    
    def get_medical_history(self, username):
        """Get user's medical history"""
        if username not in self.users:
            return []
        
        return self.users[username].get('medical_history', [])
    
    def clear_history(self, username):
        """Clear user's medical history"""
        if username in self.users:
            self.users[username]['medical_history'] = []
            self._save_database()
            return True
        return False
