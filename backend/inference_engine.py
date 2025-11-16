class InferenceEngine:
    """Rule-based inference engine using forward chaining"""
    
    def __init__(self, knowledge_base):
        self.knowledge_base = knowledge_base
    
    def diagnose(self, user_symptoms):
        """
        Perform diagnosis using forward chaining algorithm
        Returns a list of possible conditions with confidence scores
        """
        if not user_symptoms:
            return []
        
        # Normalize user symptoms to lowercase for comparison
        user_symptoms_lower = [s.lower() for s in user_symptoms]
        
        diagnoses = []
        rules = self.knowledge_base.get_rules()
        
        for rule in rules:
            # Check if this rule matches the symptoms
            match_score = self.calculate_match_score(user_symptoms_lower, rule)
            
            if match_score['confidence'] > 0:
                diagnoses.append({
                    'condition': rule['condition'],
                    'confidence': match_score['confidence'],
                    'matched_symptoms': match_score['matched_symptoms'],
                    'missing_symptoms': match_score['missing_symptoms'],
                    'description': rule.get('description', ''),
                    'recommendations': rule.get('recommendations', '')
                })
        
        # Sort by confidence score (highest first)
        diagnoses.sort(key=lambda x: x['confidence'], reverse=True)
        
        # Return top 5 diagnoses
        return diagnoses[:5]
    
    def calculate_match_score(self, user_symptoms, rule):
        """
        Calculate confidence score for a rule based on symptom matching
        Uses forward chaining logic to determine if rule fires
        """
        rule_symptoms = [s.lower() for s in rule['symptoms']]
        required_symptoms = [s.lower() for s in rule.get('required_symptoms', [])]
        
        # Check if all required symptoms are present
        required_matched = all(req in user_symptoms for req in required_symptoms)
        
        # If required symptoms are not met, confidence is 0
        if required_symptoms and not required_matched:
            return {
                'confidence': 0,
                'matched_symptoms': [],
                'missing_symptoms': rule_symptoms
            }
        
        # Count matched symptoms
        matched_symptoms = []
        for symptom in user_symptoms:
            if symptom in rule_symptoms:
                matched_symptoms.append(symptom)
        
        # Calculate confidence based on percentage of rule symptoms matched
        if len(rule_symptoms) > 0:
            base_confidence = (len(matched_symptoms) / len(rule_symptoms)) * 100
            
            # Bonus for matching required symptoms
            if required_symptoms and required_matched:
                bonus = 10
                base_confidence = min(100, base_confidence + bonus)
            
            # Penalty if user has many symptoms not in the rule
            extra_symptoms = len(user_symptoms) - len(matched_symptoms)
            if extra_symptoms > 0:
                penalty = min(20, extra_symptoms * 5)
                base_confidence = max(0, base_confidence - penalty)
        else:
            base_confidence = 0
        
        # Get missing symptoms
        missing_symptoms = [s for s in rule_symptoms if s not in user_symptoms]
        
        return {
            'confidence': round(base_confidence, 2),
            'matched_symptoms': matched_symptoms,
            'missing_symptoms': missing_symptoms
        }
    
    def forward_chain(self, facts, rules):
        """
        Generic forward chaining algorithm
        Start with facts (symptoms) and apply rules to derive conclusions
        """
        inferred_facts = set(facts)
        new_facts_added = True
        
        while new_facts_added:
            new_facts_added = False
            
            for rule in rules:
                # Check if all conditions (symptoms) of the rule are in facts
                if all(condition in inferred_facts for condition in rule.get('conditions', [])):
                    # Add conclusion if not already present
                    conclusion = rule.get('conclusion')
                    if conclusion and conclusion not in inferred_facts:
                        inferred_facts.add(conclusion)
                        new_facts_added = True
        
        return inferred_facts
    
    def explain_diagnosis(self, condition_name, user_symptoms):
        """
        Provide explanation for why a particular diagnosis was suggested
        """
        condition_info = self.knowledge_base.get_condition_info(condition_name)
        
        if not condition_info:
            return "Condition not found in knowledge base."
        
        user_symptoms_lower = [s.lower() for s in user_symptoms]
        match_score = self.calculate_match_score(user_symptoms_lower, condition_info)
        
        explanation = f"Diagnosis: {condition_name}\n\n"
        explanation += f"Confidence: {match_score['confidence']:.1f}%\n\n"
        explanation += f"Matched Symptoms ({len(match_score['matched_symptoms'])}):\n"
        
        for symptom in match_score['matched_symptoms']:
            explanation += f"  ✓ {symptom}\n"
        
        if match_score['missing_symptoms']:
            explanation += f"\nOther symptoms associated with {condition_name}:\n"
            for symptom in match_score['missing_symptoms']:
                explanation += f"  - {symptom}\n"
        
        if condition_info.get('description'):
            explanation += f"\nDescription: {condition_info['description']}\n"
        
        if condition_info.get('recommendations'):
            explanation += f"\nRecommendations: {condition_info['recommendations']}\n"
        
        return explanation
