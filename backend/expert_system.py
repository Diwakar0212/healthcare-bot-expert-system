import re
from knowledge_base import KnowledgeBase
from inference_engine import InferenceEngine

class MedicalExpertSystem:
    """Main expert system for medical diagnosis"""
    
    def __init__(self):
        self.knowledge_base = KnowledgeBase()
        self.inference_engine = InferenceEngine(self.knowledge_base)
        self.greeting_keywords = ['hello', 'hi', 'hey', 'greetings', 'good morning', 'good afternoon', 'good evening']
        self.symptom_keywords = ['symptom', 'feel', 'pain', 'ache', 'hurt', 'sick', 'fever', 'cough']
    
    def process_input(self, user_input, session):
        """Process user input and return appropriate response"""
        user_input_lower = user_input.lower().strip()
        
        # Handle greetings
        if session['state'] == 'initial' or any(keyword in user_input_lower for keyword in self.greeting_keywords):
            session['state'] = 'collecting_symptoms'
            return {
                'message': "Hello! I'm your Medical Diagnosis Assistant. I'll help you identify potential health conditions based on your symptoms.\n\nPlease describe your symptoms. You can mention multiple symptoms at once (e.g., 'I have a fever, headache, and cough').",
                'suggestions': ['I have a fever and headache', 'I feel tired and have body aches', 'I have a cough and sore throat']
            }
        
        # Extract symptoms from user input
        if session['state'] == 'collecting_symptoms':
            extracted_symptoms = self.extract_symptoms(user_input_lower)
            
            if extracted_symptoms:
                # Add new symptoms to session
                for symptom in extracted_symptoms:
                    if symptom not in session['symptoms']:
                        session['symptoms'].append(symptom)
                
                # Run inference to get possible diagnoses
                diagnoses = self.inference_engine.diagnose(session['symptoms'])
                
                if diagnoses:
                    # Format diagnosis results
                    diagnosis_text = self.format_diagnoses(diagnoses)
                    
                    session['state'] = 'diagnosis_complete'
                    
                    return {
                        'message': f"Based on the symptoms you've described ({', '.join(session['symptoms'])}), here are the possible conditions:\n\n{diagnosis_text}\n\n⚠️ **Important:** This is an AI-assisted preliminary assessment and should not replace professional medical advice. Please consult a healthcare provider for proper diagnosis and treatment.\n\nWould you like to start a new consultation?",
                        'diagnosis': diagnoses,
                        'suggestions': ['Start new consultation', 'Tell me more about these conditions', 'What should I do next?']
                    }
                else:
                    return {
                        'message': f"I've noted your symptoms: {', '.join(session['symptoms'])}.\n\nI need more information to make an accurate assessment. Can you describe any other symptoms you're experiencing?",
                        'suggestions': ['No other symptoms', 'I also have...']
                    }
            else:
                return {
                    'message': "I couldn't identify specific symptoms from your message. Please describe what you're feeling more clearly.\n\nFor example: 'I have a fever and sore throat' or 'I'm experiencing headache and nausea'.",
                    'suggestions': ['Common cold symptoms', 'Flu-like symptoms', 'Stomach issues']
                }
        
        # Handle post-diagnosis conversation
        if session['state'] == 'diagnosis_complete':
            if 'new' in user_input_lower or 'start' in user_input_lower or 'again' in user_input_lower:
                session['symptoms'] = []
                session['state'] = 'collecting_symptoms'
                return {
                    'message': "Let's start fresh. What symptoms are you experiencing?",
                    'suggestions': ['I have a fever and headache', 'I feel tired and have body aches', 'I have a cough and sore throat']
                }
            else:
                return {
                    'message': "I'm here to help! You can:\n- Start a new consultation\n- Ask about specific conditions\n- Get general health advice\n\nWhat would you like to do?",
                    'suggestions': ['Start new consultation', 'Explain my diagnosis', 'Prevention tips']
                }
        
        return {
            'message': "I'm not sure I understand. Could you please rephrase that?",
            'suggestions': ['Start consultation', 'List my symptoms', 'Get help']
        }
    
    def extract_symptoms(self, text):
        """Extract symptoms from user input text"""
        detected_symptoms = []
        all_symptoms = self.knowledge_base.get_all_symptoms()
        
        # Check for each known symptom in the text
        for symptom in all_symptoms:
            # Create pattern that matches the symptom with word boundaries
            pattern = r'\b' + re.escape(symptom.lower()) + r'\b'
            if re.search(pattern, text):
                detected_symptoms.append(symptom)
        
        # Also check for common variations and synonyms
        symptom_variations = {
            'fever': ['temperature', 'hot', 'burning up'],
            'headache': ['head pain', 'head hurts', 'migraine'],
            'cough': ['coughing', 'coughed'],
            'fatigue': ['tired', 'exhausted', 'weak', 'weakness'],
            'nausea': ['feel sick', 'queasy', 'sick to stomach'],
            'sore throat': ['throat pain', 'throat hurts'],
            'runny nose': ['nose running', 'nasal discharge'],
            'body ache': ['body pain', 'muscle pain', 'aches'],
            'shortness of breath': ['hard to breathe', 'breathing difficulty', 'can\'t breathe'],
            'chest pain': ['chest hurts', 'chest discomfort'],
            'dizziness': ['dizzy', 'lightheaded', 'vertigo'],
            'vomiting': ['throwing up', 'vomit', 'puking'],
            'diarrhea': ['loose stool', 'stomach runs'],
            'abdominal pain': ['stomach pain', 'belly pain', 'stomach ache'],
            'loss of appetite': ['not hungry', 'don\'t want to eat'],
            'chills': ['shivering', 'cold sweats'],
            'confusion': ['confused', 'disoriented'],
            'rash': ['skin rash', 'skin irritation', 'red spots']
        }
        
        for symptom, variations in symptom_variations.items():
            for variation in variations:
                if variation in text and symptom not in detected_symptoms:
                    detected_symptoms.append(symptom)
                    break
        
        return detected_symptoms
    
    def format_diagnoses(self, diagnoses):
        """Format diagnosis results for display"""
        if not diagnoses:
            return "No matching conditions found."
        
        formatted = []
        for i, diagnosis in enumerate(diagnoses, 1):
            condition = diagnosis['condition']
            confidence = diagnosis['confidence']
            matched_symptoms = diagnosis['matched_symptoms']
            
            # Get condition details from knowledge base
            condition_info = self.knowledge_base.get_condition_info(condition)
            
            formatted.append(f"**{i}. {condition}** (Confidence: {confidence:.1f}%)")
            formatted.append(f"   - Matched symptoms: {', '.join(matched_symptoms)}")
            
            if condition_info:
                if condition_info.get('description'):
                    formatted.append(f"   - Description: {condition_info['description']}")
                if condition_info.get('recommendations'):
                    formatted.append(f"   - Recommendations: {condition_info['recommendations']}")
            
            formatted.append("")
        
        return "\n".join(formatted)
    
    def get_all_symptoms(self):
        """Get list of all available symptoms"""
        return self.knowledge_base.get_all_symptoms()
    
    def get_all_conditions(self):
        """Get list of all conditions"""
        return [rule['condition'] for rule in self.knowledge_base.rules]
