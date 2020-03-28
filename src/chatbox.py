# chatbot text

import pyttsx3
import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone()
engine = pyttsx3.init()


class AskQuestion:
    def __init__(self, q):
        self.question = q
        self.answer = ""
    
    def get_response(self, mic):
        
        with mic as source:
            print("I am Listening...")
            audio = r.listen(source)
        
        print("Listening has stopped")
        
        return audio
    
    def ask(self):
        resp = False
        
        while not resp:
            engine.say(self.question)
            engine.runAndWait()
            
            audio = self.get_response(mic)
            
            try:
                ans = r.recognize_google(audio)
                print(ans)
                self.answer = ans
                resp = True
            except:
                engine.say("Please say that again.")


def ask_more_coughing_questions(resp, questions, patient_responses):
    
    if "no" in resp:
        engine.say("I'm glad that you have not been coughing.")
        return
        
    
    for q in range(len(questions)):
        Q = AskQuestion(questions[q])
        Q.ask()
        
        patient_responses.append({f"questions[q]": Q.answer})
        
        if "yes" in Q.answer:
            engine.say("I see")
        else:
            engine.say("Oh right")
    

def start():
    questions = [
        'How are you feeling?',
        'Did you sleep well?',
        'Do you feel tired?',
        'Have you been coughing',
        'Do you feel hot to touch on your chest or back?',
        'Do you feel a loss of taste?',
        'Do you have difficulty breathing',
        'Do you have a runny nose?',
        'Do you have a sore throat?',
        
    ]
    
    coughing_questions = [
        'Was it a continuous cough?',
        'Was it a dry cough?'
    ]
    
    patient_responses = []
    
    
    for q in range(len(questions)):
        Quest = AskQuestion(questions[q])
        Quest.ask()
        
        patient_responses.append({f"{questions[q]}.": Quest.answer})
        
        if q == 3:
            ask_more_coughing_questions(
                Quest.answer,
                coughing_questions,
                patient_responses
            )
    
    engine.say("These were all of your responses")
    
    for response in patient_responses:
        for q, ans in response.items():
            print(f"Q{response+1}: {q}")
            print(f"A: {ans}")

start()
