"""
The Dial: A Predictive Coding Simulation
Models the computational psychiatry of perception, belief, and mental health.
"""

class PredictionEngine:
    def __init__(self, initial_prior=0.5, prior_precision=1.0):
        # The internal model of the world (0.0 = terrible/danger, 1.0 = safe/rewarding)
        self.prior = initial_prior 
        
        # The Dial: How much we trust our own model vs. sensory evidence
        self.prior_precision = prior_precision 
        
        # Standard sensory precision (how loud the actual world is)
        self.evidence_precision = 1.0 

    def perceive(self, evidence, context="Everyday life"):
        """
        The core loop: Belief -> Guess -> Reality -> Surprise -> Update
        """
        # 1. The machinery calculates the weight of evidence vs prior
        total_precision = self.prior_precision + self.evidence_precision
        prior_weight = self.prior_precision / total_precision
        evidence_weight = self.evidence_precision / total_precision
        
        # 2. The hallucination meets the territory
        experience = (self.prior * prior_weight) + (evidence * evidence_weight)
        
        # 3. Prediction error is generated (how wrong were we?)
        prediction_error = evidence - self.prior
        
        # 4. The Q-table/Prior updates based on the error and the dial setting
        update_magnitude = prediction_error * evidence_weight
        self.prior += update_magnitude
        
        print(f"[{context}]")
        print(f"  Incoming Evidence  : {evidence:.2f}")
        print(f"  Prior (Expectation): {self.prior - update_magnitude:.2f}")
        print(f"  Pred. Error (Surprise): {prediction_error:+.2f}")
        print(f"  Felt Experience    : {experience:.2f}")
        print(f"  New Prior Updated  : {self.prior:.2f}")
        print(f"  Dial (Prior Prec)  : {self.prior_precision:.2f}\n")
        
        return experience

    def traumatic_event(self, evidence):
        """
        Overwrites the prior at maximum precision from a single n=1 event.
        """
        print(">>> CATACLYSMIC SENSORY INPUT. SURVIVAL OVERRIDE TRIGGERED. <<<")
        self.prior = evidence
        self.prior_precision = 1000.0 # Firewalled from future updates
        print(f"  Traumatic Prior Written: {self.prior:.2f}")
        print(f"  Dial locked at extreme precision: {self.prior_precision:.2f}\n")

    def apply_medication(self, med_type):
        """
        Interventions shift the dial, not the content.
        """
        if med_type == "Antipsychotic":
            # D2 Antagonists turn down the precision on priors
            self.prior_precision = max(1.0, self.prior_precision * 0.1)
            print(">>> ANTIPSYCHOTIC APPLIED: Prior precision reduced. Volume turned down. <<<\n")
            
        elif med_type == "SSRI":
            # Serotonin reuptake inhibitors gently reduce precision on fixed negative priors
            self.prior_precision = 3.0
            print(">>> SSRI APPLIED: Prior precision gently softened. Neuroplasticity increasing. <<<\n")
            
        elif med_type == "Psychedelic":
            # 5-HT2A Agonists temporarily flatten every prior in the system
            self.prior_precision = 0.1
            print(">>> PSYCHEDELIC APPLIED: Prior precision flattened. Gates open for update. <<<\n")
            
        elif med_type == "Integration":
            # The compound clears. The brain re-consolidates around its new baseline.
            self.prior_precision = 1.0
            print(">>> COMPOUND CLEARS: Integration phase. Dial returns to healthy baseline. <<<\n")


# ==========================================
# THE SIMULATION
# ==========================================

if __name__ == "__main__":
    
    print("=== SCENARIO 1: THE HEALTHY DIAL ===")
    mind = PredictionEngine(initial_prior=0.5, prior_precision=1.0)
    # Evidence is positive (0.8). The mind updates gracefully.
    mind.perceive(evidence=0.8, context="Meets a friendly dog")
    mind.perceive(evidence=0.9, context="Has a good conversation")
    
    print("=== SCENARIO 2: PSYCHOSIS (High Prior Precision) ===")
    mind_psychotic = PredictionEngine(initial_prior=0.1, prior_precision=50.0)
    # The world is safe (0.9), but the prior is so strong the evidence is dismissed as noise.
    mind_psychotic.perceive(evidence=0.9, context="Friend says 'I love you'")
    mind_psychotic.perceive(evidence=1.0, context="Gets promoted at work")
    
    # Medication intervenes on the machinery, not the story
    mind_psychotic.apply_medication("Antipsychotic")
    mind_psychotic.perceive(evidence=0.9, context="Friend says 'I love you' (Medicated)")

    print("=== SCENARIO 3: DEPRESSION (The Model That Says 'Don't Bother') ===")
    mind_depressed = PredictionEngine(initial_prior=0.0, prior_precision=20.0)
    # Good things happen, but the futility prior suppresses them.
    mind_depressed.perceive(evidence=0.8, context="Beautiful sunny day")
    mind_depressed.perceive(evidence=0.9, context="Completes a difficult task")
    
    # SSRI gently lowers the dial, allowing slow, compounding updates over time
    mind_depressed.apply_medication("SSRI")
    mind_depressed.perceive(evidence=0.8, context="Beautiful sunny day (Week 2)")
    mind_depressed.perceive(evidence=0.9, context="Completes a difficult task (Week 4)")

    print("=== SCENARIO 4: PTSD (The Prior That Will Not Decay) ===")
    mind_trauma = PredictionEngine(initial_prior=0.8, prior_precision=1.0)
    # The system is running normally until catastrophic training data arrives
    mind_trauma.traumatic_event(evidence=0.0)
    
    # Decades of safe evidence cannot penetrate the firewalled prior. Notice the massive Prediction Error being ignored.
    mind_trauma.perceive(evidence=0.9, context="Hears a car backfire (10 years later)")
    mind_trauma.perceive(evidence=1.0, context="Safe at home with family")
    
    # Psychedelic-Assisted Therapy resets the dial to allow the update
    mind_trauma.apply_medication("Psychedelic")
    mind_trauma.perceive(evidence=1.0, context="Therapeutic container: 'I am safe now'")
    mind_trauma.perceive(evidence=0.9, context="Processing memory: World is not entirely dangerous")
    
    # The compound clears, and the mind retains its newly written baseline
    mind_trauma.apply_medication("Integration")
    mind_trauma.perceive(evidence=0.8, context="Everyday life, post-integration")
