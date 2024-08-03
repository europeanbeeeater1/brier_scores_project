import datetime, os
from csv import reader

class BrierHelperFunctions():      
    @staticmethod
    def date_checker(date_obj, current_year):
        day = date_obj.day
        month = date_obj.month 
        year = date_obj.year
        if not(1 <= month <= 12 and 1 <= day <= 31 and 1 <= year <= current_year):
            raise ValueError(f"{date_obj} is an invalid date.")
        else:
            return True
        
    @staticmethod
    def confidence_checker(confidence):
        if not(0 <= confidence <= 1):
            raise ValueError(f"{confidence} is not between 0 and 1.")
        else:
            return True
    
    @staticmethod
    def active_checker(active):
        if not (active == False or active == True):
            raise ValueError(f"{active} is not True or False.")
        else:
            return True

    @staticmethod
    def result_checker(result):
        if not (result == "1" or result == "0" or result == ""):
            raise ValueError(f"{result} is not equal to 1/Yes, 0/No, or "".")
        else:
            return True

    @staticmethod
    def read_file(brier_score):
        from Prediction import Prediction
        fileName = input("Write a file name: ")
        if not os.path.isfile(fileName):
            raise FileNotFoundError(f"{fileName} is not in the current directory.")
        invalidRowCounter = 0
        with open(fileName, mode = 'r', newline = '', encoding = 'utf-8') as file:
            fileReader = reader(file)
            next(fileReader) # Skip the first row 
            for row in fileReader:
                errorFlag = False
                question, name, confidence, prediction_date, active, result = row
                if not (active == "FALSE" or active == "TRUE"):
                    raise ValueError("f{active} is invalid")
                if active == "FALSE":
                    active = False
                if active == "TRUE":
                    active = True
                date_obj = datetime.datetime.strptime(prediction_date, "%Y/%m/%d")
                current_year = datetime.datetime.now().year
                confidence = float(confidence)
                if not(BrierHelperFunctions.date_checker(date_obj, current_year) and BrierHelperFunctions.confidence_checker(confidence) and BrierHelperFunctions.result_checker(result)):
                    errorFlag = True
                    invalidRowCounter += 1
                if errorFlag != True: 
                    if result == "":
                        prediction = Prediction(question, name, confidence, prediction_date, active, result)
                        brier_score.add_prediction(prediction)
                    else:
                        result = int(result)
                        prediction = Prediction(question, name, confidence, prediction_date, active, result)
                        brier_score.add_prediction(prediction)
                else:
                    invalidRowCounter += 1
            print("This file had", invalidRowCounter, "rows with issues")
    
    @staticmethod
    def question_updater(brier_score):
        changing_question = input("Input the question to change: ")
        # Check if the question exists in any of the predictions
        if not any(p.question == changing_question for p in brier_score.predictions):
            raise ValueError(f"{changing_question} is an invalid input")
        brier_score.active_status_updater(changing_question)
    
   
