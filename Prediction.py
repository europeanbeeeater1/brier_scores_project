import datetime
from BrierUtilityFunctions import BrierHelperFunctions as BrierHelpers
import pandas as pd

class Prediction:
    def __init__(self, question, name, confidence, prediction_date, active, result):
        self.question = question
        self.name = name
        self.confidence = confidence  
        self.prediction_date = prediction_date
        self.active = active
        self.result = result if result is not None else ""
    
    # Get functions
    def get_question(self):
        print(self.question)
    
    def get_name(self):
        print(self.name)

    def get_confidence(self):
        print(self.confidence)
    
    def get_prediction_date(self):
        print(self.prediction_date)
    
    def get_active(self):
        print(self.active)
    
    def get_result(self):
        if self.result:
            print(self.result)
        else:
            raise ValueError(f"The question is not yet resolved.")
    
    # Set functions
    def set_question(self, newQuestion):
        self.question = newQuestion
    
    def set_name(self, newName):
        self.name = newName
    
    def set_confidence(self, newConfidence):
        BrierHelpers.confidence_checker(newConfidence)
        self.confidence = newConfidence
    
    def set_prediction_date(self, newPredictionDate):
        current_year = datetime.datetime.now().year
        BrierHelpers.date_checker(newPredictionDate, current_year)
        self.prediction_date = newPredictionDate
    
    def set_active(self, active):
        BrierHelpers.active_checker(active)
        self.active = active 
    
    def set_result(self, result):
        BrierHelpers.result_checker(result)
        self.result = result 

class BrierScore:
    def __init__(self):
        self.predictions = []
    
    def add_prediction(self, prediction):
        if isinstance(prediction, Prediction):
            self.predictions.append(prediction)
        else:
            raise TypeError(f"{prediction} is not a member of the Prediction class")
    
    def remove_last_prediction(self):
        if self.predictions:
            self.predictions.pop()
        else:
            raise ValueError(f"The list has no elements")
    
    def remove_given_prediction(self, prediction):
        if isinstance(prediction, Prediction):
            if prediction in self.predictions:
                self.predictions.remove(prediction)
            else:
                raise ValueError(f"{prediction} is not in the list")
        else:
            raise TypeError(f"{prediction} is not an instance of Prediction class")

    def active_status_updater(self, question, active):
        if active == False:
            result = int(input("Type 1 if the answer was 'Yes' and 0 if the answer was 'No'"))
            if not (result == 1 or result == 0):
                raise ValueError(f"{result} is an invalid input")
            for prediction in self.predictions:
                if prediction.question == question:
                    prediction.active = False
                    prediction.result = result 
            
    def question_deleter(self, question):
        self.predictions = [p for p in self.predictions if p.question != question]

    def name_deleter(self, name):
        self.predictions = [p for p in self.predictions if p.name != name]

    def unique_names(self):
        return list({p.name for p in self.predictions}) # Create a set and change it to a list

    def find_score_by_name(self, name):
        if name not in self.unique_names():
            raise ValueError("f{name} is not found")
        sum_squares_step = 0
        sum_squares_total = 0
        counter = 0
        brier_score = 0
        for p in self.predictions:
            if p.name == name and (p.result == 1 or p.result == 0):
                sum_squares_total = sum_squares_total + (p.result - sum_squares_step)**2
                counter += 1
        if counter == 0:
            return None # 0 predictions found
        brier_score = (1/counter) * sum_squares_total
        print("The user ", name, " has a score of ", brier_score)
    
    def find_each_score(self):
        unique_names = self.unique_names()
        score = 0
        name_score_pair = {}
        for p in unique_names:
            score = self.find_score_by_name(p)
            if score is not None:
                name_score_pair[p] = score 
        initial_df = pd.DataFrame(list(name_score_pair.items()), columns = ["Name", "Score"])
        print(initial_df)

    def clear_all(self):
        self.predictions.clear()


    
