class KnowledgeBase:
    """Medical knowledge base containing rules for diagnosis"""
    
    def __init__(self):
        # Define medical rules in the format:
        # {
        #   'condition': 'Disease Name',
        #   'symptoms': ['symptom1', 'symptom2', ...],
        #   'required_symptoms': ['must_have_symptom'],  # Optional
        #   'description': 'Description of the condition',
        #   'recommendations': 'What to do'
        # }
        
        self.rules = [
            {
                'condition': 'Common Cold',
                'symptoms': ['runny nose', 'sneezing', 'sore throat', 'cough', 'mild fever', 'fatigue'],
                'required_symptoms': ['runny nose'],
                'description': 'A viral infection of the upper respiratory tract',
                'recommendations': 'Rest, drink plenty of fluids, use over-the-counter cold medications. Usually resolves in 7-10 days.'
            },
            {
                'condition': 'Influenza (Flu)',
                'symptoms': ['fever', 'cough', 'sore throat', 'body ache', 'headache', 'fatigue', 'chills'],
                'required_symptoms': ['fever', 'body ache'],
                'description': 'A viral infection affecting the respiratory system',
                'recommendations': 'Rest, stay hydrated, antiviral medications may help if started early. Seek medical attention if symptoms worsen.'
            },
            {
                'condition': 'COVID-19',
                'symptoms': ['fever', 'cough', 'fatigue', 'loss of taste', 'loss of smell', 'shortness of breath', 'body ache', 'headache', 'sore throat'],
                'required_symptoms': ['fever', 'cough'],
                'description': 'Respiratory illness caused by SARS-CoV-2 virus',
                'recommendations': 'Self-isolate, get tested, rest, monitor oxygen levels. Seek immediate medical care if breathing becomes difficult.'
            },
            {
                'condition': 'Migraine',
                'symptoms': ['severe headache', 'nausea', 'sensitivity to light', 'sensitivity to sound', 'vomiting', 'dizziness'],
                'required_symptoms': ['severe headache'],
                'description': 'Intense headache often accompanied by nausea and sensitivity',
                'recommendations': 'Rest in a dark, quiet room. Take prescribed migraine medication. Consult a neurologist for persistent migraines.'
            },
            {
                'condition': 'Gastroenteritis (Stomach Flu)',
                'symptoms': ['nausea', 'vomiting', 'diarrhea', 'abdominal pain', 'fever', 'headache', 'fatigue'],
                'required_symptoms': ['diarrhea'],
                'description': 'Inflammation of the digestive tract',
                'recommendations': 'Stay hydrated with oral rehydration solutions, rest, eat bland foods. Seek medical care if dehydration occurs.'
            },
            {
                'condition': 'Pneumonia',
                'symptoms': ['cough', 'fever', 'shortness of breath', 'chest pain', 'fatigue', 'chills', 'confusion'],
                'required_symptoms': ['cough', 'fever', 'shortness of breath'],
                'description': 'Infection that inflames air sacs in the lungs',
                'recommendations': 'Seek immediate medical attention. Requires antibiotics or antiviral medications. May need hospitalization.'
            },
            {
                'condition': 'Bronchitis',
                'symptoms': ['persistent cough', 'mucus production', 'fatigue', 'shortness of breath', 'mild fever', 'chest discomfort'],
                'required_symptoms': ['persistent cough'],
                'description': 'Inflammation of the bronchial tubes',
                'recommendations': 'Rest, drink fluids, use a humidifier. See a doctor if symptoms persist beyond 3 weeks or worsen.'
            },
            {
                'condition': 'Strep Throat',
                'symptoms': ['severe sore throat', 'fever', 'swollen lymph nodes', 'difficulty swallowing', 'headache', 'rash'],
                'required_symptoms': ['severe sore throat', 'fever'],
                'description': 'Bacterial infection of the throat',
                'recommendations': 'Requires antibiotics. See a doctor for proper diagnosis and treatment to prevent complications.'
            },
            {
                'condition': 'Sinusitis',
                'symptoms': ['facial pain', 'nasal congestion', 'runny nose', 'headache', 'cough', 'fever', 'fatigue'],
                'required_symptoms': ['facial pain', 'nasal congestion'],
                'description': 'Inflammation or infection of the sinuses',
                'recommendations': 'Use saline nasal spray, apply warm compresses. See a doctor if symptoms persist beyond 10 days.'
            },
            {
                'condition': 'Allergic Rhinitis',
                'symptoms': ['sneezing', 'runny nose', 'itchy eyes', 'nasal congestion', 'fatigue'],
                'required_symptoms': ['sneezing', 'runny nose'],
                'description': 'Allergic reaction affecting the nose and eyes',
                'recommendations': 'Avoid allergens, use antihistamines, consider allergy testing. See an allergist for persistent symptoms.'
            },
            {
                'condition': 'Tension Headache',
                'symptoms': ['headache', 'pressure around forehead', 'neck pain', 'fatigue', 'difficulty concentrating'],
                'required_symptoms': ['headache'],
                'description': 'Most common type of headache caused by muscle tension',
                'recommendations': 'Rest, stress management, over-the-counter pain relievers. Practice good posture.'
            },
            {
                'condition': 'Urinary Tract Infection (UTI)',
                'symptoms': ['burning urination', 'frequent urination', 'abdominal pain', 'cloudy urine', 'fever', 'pelvic pain'],
                'required_symptoms': ['burning urination', 'frequent urination'],
                'description': 'Bacterial infection of the urinary system',
                'recommendations': 'Drink plenty of water, see a doctor for antibiotics. Don\'t delay treatment to prevent kidney infection.'
            },
            {
                'condition': 'Asthma Attack',
                'symptoms': ['shortness of breath', 'wheezing', 'cough', 'chest tightness', 'difficulty breathing'],
                'required_symptoms': ['shortness of breath', 'wheezing'],
                'description': 'Narrowing of airways causing breathing difficulty',
                'recommendations': 'Use rescue inhaler immediately. Seek emergency care if symptoms don\'t improve or worsen.'
            },
            {
                'condition': 'Food Poisoning',
                'symptoms': ['nausea', 'vomiting', 'diarrhea', 'abdominal pain', 'fever', 'weakness'],
                'required_symptoms': ['nausea', 'diarrhea'],
                'description': 'Illness from consuming contaminated food',
                'recommendations': 'Stay hydrated, rest. Seek medical care if symptoms are severe or persistent, or if blood in stool.'
            },
            {
                'condition': 'Dehydration',
                'symptoms': ['dizziness', 'fatigue', 'dry mouth', 'decreased urination', 'headache', 'confusion'],
                'required_symptoms': ['dizziness', 'dry mouth'],
                'description': 'Excessive loss of body fluids',
                'recommendations': 'Drink water or oral rehydration solutions. Seek medical care if severe symptoms persist.'
            },
            {
                'condition': 'Anxiety Disorder',
                'symptoms': ['rapid heartbeat', 'sweating', 'trembling', 'shortness of breath', 'dizziness', 'nausea', 'fear'],
                'required_symptoms': ['rapid heartbeat', 'fear'],
                'description': 'Mental health condition characterized by excessive worry',
                'recommendations': 'Practice relaxation techniques, consider therapy. Consult a mental health professional for proper treatment.'
            }
        ]
        
        # Create a set of all unique symptoms for quick lookup
        self.all_symptoms = set()
        for rule in self.rules:
            self.all_symptoms.update(rule['symptoms'])
    
    def get_all_symptoms(self):
        """Return list of all symptoms in the knowledge base"""
        return sorted(list(self.all_symptoms))
    
    def get_rules(self):
        """Return all diagnostic rules"""
        return self.rules
    
    def get_condition_info(self, condition_name):
        """Get detailed information about a specific condition"""
        for rule in self.rules:
            if rule['condition'].lower() == condition_name.lower():
                return rule
        return None
    
    def add_rule(self, rule):
        """Add a new diagnostic rule to the knowledge base"""
        self.rules.append(rule)
        self.all_symptoms.update(rule['symptoms'])
    
    def get_conditions_by_symptom(self, symptom):
        """Get all conditions that include a specific symptom"""
        conditions = []
        for rule in self.rules:
            if symptom.lower() in [s.lower() for s in rule['symptoms']]:
                conditions.append(rule['condition'])
        return conditions
