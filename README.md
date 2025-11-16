# Healthcare Bot - Medical Diagnosis Expert System

A full-stack expert system chatbot that diagnoses medical conditions based on symptoms using a rule-based approach with forward chaining inference engine.

## 🌟 Features

- **Rule-Based Expert System**: Uses forward chaining algorithm for medical diagnosis
- **Comprehensive Knowledge Base**: 16+ medical conditions with detailed symptoms and recommendations
- **Intelligent Symptom Extraction**: NLP-based symptom recognition from natural language
- **Confidence Scoring**: Calculates match confidence for each potential diagnosis
- **Interactive Chat Interface**: Modern React-based UI with real-time responses
- **User Authentication**: Login/signup system with secure session management
- **Consultation History**: Track and review past diagnoses and recommendations
- **Session Management**: Maintains conversation context throughout diagnosis
- **Responsive Design**: Works seamlessly on desktop and mobile devices

## 🏗️ Architecture

### Backend (Python/Flask)
- **Expert System**: Core diagnostic engine
- **Knowledge Base**: Medical rules and conditions database
- **Inference Engine**: Forward chaining algorithm implementation
- **REST API**: Flask endpoints for chat interaction

### Frontend (React)
- **Chat Interface**: Real-time conversational UI
- **Message Components**: Rich message display with diagnosis cards
- **State Management**: Session-based conversation tracking
- **Responsive Design**: Mobile-first approach

## 📋 Prerequisites

- Python 3.8 or higher
- Node.js 14 or higher
- npm or yarn

## 🚀 Installation & Setup

### Backend Setup

1. Navigate to the backend directory:
```powershell
cd backend
```

2. Create a virtual environment (recommended):
```powershell
python -m venv .venv
.\.venv\Scripts\Activate
```

3. Install dependencies:
```powershell
pip install -r requirements.txt
```

4. Run the Flask server:
```powershell
python app.py
```

The backend server will start at `http://localhost:5000`

### Frontend Setup

1. Open a new terminal and navigate to the frontend directory:
```powershell
cd frontend
```

2. Install dependencies:
```powershell
npm install
```

3. Start the development server:
```powershell
npm start
```

The frontend will open automatically at `http://localhost:3000`

## 🩺 How It Works

### Rule-Based Expert System

The system uses a **forward chaining** inference algorithm:

1. **Symptom Collection**: User describes symptoms in natural language
2. **Symptom Extraction**: NLP techniques identify medical symptoms from input
3. **Rule Matching**: Inference engine matches symptoms against knowledge base rules
4. **Confidence Calculation**: Each condition receives a confidence score based on:
   - Percentage of rule symptoms matched
   - Presence of required symptoms
   - Penalty for extra unmatched symptoms
5. **Diagnosis Presentation**: Top 5 conditions sorted by confidence with recommendations

### Knowledge Base Structure

Each medical rule contains:
- **Condition**: Disease/condition name
- **Symptoms**: List of associated symptoms
- **Required Symptoms**: Must-have symptoms for diagnosis
- **Description**: Explanation of the condition
- **Recommendations**: Treatment and care advice

### Inference Engine Algorithm

```python
def calculate_match_score(user_symptoms, rule):
    # Check required symptoms
    if required_symptoms not present:
        return 0% confidence
    
    # Calculate base confidence
    matched_count / total_rule_symptoms * 100
    
    # Apply bonuses and penalties
    + bonus for required symptoms matched
    - penalty for extra unmatched symptoms
    
    return final_confidence_score
```

## 📁 Project Structure

```
healthcare-bot-expert-system/
│
├── backend/
│   ├── app.py                 # Flask application & API endpoints
│   ├── expert_system.py       # Main expert system logic
│   ├── knowledge_base.py      # Medical knowledge base
│   ├── inference_engine.py    # Forward chaining algorithm
│   ├── user_database.py       # User authentication & history
│   ├── users_db.json          # User data storage
│   └── requirements.txt       # Python dependencies
│
└── frontend/
    ├── public/
    │   └── index.html
    ├── src/
    │   ├── components/
    │   │   ├── ChatInterface.js    # Main chat component
    │   │   ├── ChatInterface.css
    │   │   ├── Message.js          # Message display component
    │   │   ├── Message.css
    │   │   ├── LoginPage.js        # User login/signup
    │   │   ├── LoginPage.css
    │   │   ├── HistoryPage.js      # Consultation history
    │   │   └── HistoryPage.css
    │   ├── contexts/
    │   │   └── AuthContext.js      # Authentication context
    │   ├── App.js                  # Root component
    │   ├── App.css
    │   ├── index.js
    │   └── index.css
    └── package.json
```

## 🔌 API Endpoints

### POST /api/chat
Send a message and receive diagnosis
```json
Request:
{
  "session_id": "session_123",
  "message": "I have a fever and headache"
}

Response:
{
  "session_id": "session_123",
  "message": "Bot response text",
  "diagnosis": [...],
  "suggestions": [...],
  "state": "collecting_symptoms"
}
```

### POST /api/reset
Reset conversation session
```json
Request:
{
  "session_id": "session_123"
}
```

### GET /api/symptoms
Get all available symptoms

### GET /api/conditions
Get all medical conditions

### GET /health
Health check endpoint

## 🏥 Supported Medical Conditions

1. Common Cold
2. Influenza (Flu)
3. COVID-19
4. Migraine
5. Gastroenteritis
6. Pneumonia
7. Bronchitis
8. Strep Throat
9. Sinusitis
10. Allergic Rhinitis
11. Tension Headache
12. Urinary Tract Infection (UTI)
13. Asthma Attack
14. Food Poisoning
15. Dehydration
16. Anxiety Disorder

## 🎯 Usage Example

1. **Start Conversation**: Open the app and greet the bot
2. **Describe Symptoms**: "I have a fever, cough, and body aches"
3. **Receive Diagnosis**: Bot analyzes symptoms and provides top matches
4. **View Details**: Each diagnosis shows:
   - Condition name
   - Confidence score
   - Matched symptoms
   - Description
   - Recommendations
5. **Take Action**: Follow medical advice and consult professionals

## ⚠️ Important Disclaimer

**This is an educational AI-assisted diagnostic tool and should NOT replace professional medical advice.** Always consult qualified healthcare professionals for proper diagnosis, treatment, and medical care.

## 🔧 Customization

### Adding New Conditions

Edit `backend/knowledge_base.py`:

```python
self.rules.append({
    'condition': 'Your Condition',
    'symptoms': ['symptom1', 'symptom2'],
    'required_symptoms': ['must_have'],
    'description': 'Condition description',
    'recommendations': 'Treatment advice'
})
```

### Modifying Inference Logic

Edit `backend/inference_engine.py` to adjust:
- Confidence calculation algorithm
- Symptom matching criteria
- Penalty/bonus weights

## 🛠️ Technologies Used

### Backend
- Flask 3.0.0
- Flask-CORS 4.0.0
- Python 3.x

### Frontend
- React 18.2.0
- Axios 1.6.0
- CSS3 with modern features

## 📈 Future Enhancements

- [ ] Machine learning integration for improved accuracy
- [ ] User authentication and medical history tracking
- [ ] Multi-language support
- [ ] Voice input for symptoms
- [ ] Integration with external medical APIs
- [ ] PDF report generation
- [ ] Doctor appointment booking
- [ ] Medication reminder system

## 🤝 Contributing

This is an educational project. Feel free to:
- Add more medical conditions
- Improve the inference algorithm
- Enhance the UI/UX
- Add new features

## 📄 License

This project is for educational purposes.

## 👥 Authors

Diwakar - PBL 5th Semester Project

## 🙏 Acknowledgments

- Medical knowledge sourced from standard diagnostic references
- UI design inspired by modern healthcare applications
- Expert system methodology based on classical AI approaches

---

**Remember**: This tool is for educational and informational purposes only. Always seek professional medical advice for health concerns.
