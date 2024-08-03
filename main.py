from BrierUtilityFunctions import BrierHelperFunctions
from Prediction import BrierScore

def main():
    brier_score_instance = BrierScore()
    try:
        while True:
            user_initial_integer = int(input("Welcome to the function. Input 1 to read in a file, 2 to analyze participants, 3 to clear data, 4 to update question status, and 5 to quit: ")) 
            if user_initial_integer == 1:
                BrierHelperFunctions.read_file(brier_score_instance)
            elif user_initial_integer == 2:
                user_sub_option = int(input("Input 1 to see find an individual's score, 2 to see each score for each participant, and 3 to exit: "))
                if user_sub_option == 1:
                    name = input("Input a name: ")
                    print(name, " had a score of ", brier_score_instance.find_score_by_name(name))
                elif user_sub_option == 2:
                    brier_score_instance.find_each_score()
                elif user_sub_option == 3:
                    break
            elif user_initial_integer == 3:
                brier_score_instance.clear_all()
            elif user_initial_integer == 4:
                print("The following are currently active questions: ")
                brier_score_instance.unique_and_active_questions()
                BrierHelperFunctions.question_updater(brier_score_instance)
            elif user_initial_integer == 5:
                print("Quitting program")
                break
            else:
                print("Invalid option, please enter 1, 2, 3, or 4.")
    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except ValueError as e:
        print(f"Value error: {e}")
    except TypeError as e:
        print(f"Type error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred in the main loop: {e}")

if __name__ == "__main__":
    main()

