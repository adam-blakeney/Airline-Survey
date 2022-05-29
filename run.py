from datetime import date
import gspread
from google.oauth2.service_account import Credentials


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('airline_survey')


def intro():
    """
    Will explain to user the purpose of the app.
    """
    print("Welcome to AirLine surveys EU!")
    print("Please choose one of the following options.")
    choice = input("Start, Instructions or About: \n")
    choice = choice.lower()
    if choice == "start":
        print("Thank you for taking time to complete this survey")
        print("We are always looking to imporve your AirLine experience")
        print("With your help we hope to achieve that!")
    elif choice == "instructions":
        print("Instructions:")
        print("- You will be shown 5 quick questions on your experience")
        print("- Please answer questions by entering a number from 0 to 5.")
        print("- Number 1 being lowest and 5 being the highest.")
        print("- At the end we will let your confirm your entries")
        intro()
    elif choice == "about":
        print("Our questions has been put together to:")
        print("- Find out how happy our customers are with us.")
        print("- See what our customers think of our service.")
        print("- To help us improve your experience. \n")
        intro()
    else:
        print("Please choose one of the above options. \n")
        intro()


def idents():
    """
    This is where the user enters their credentials
    """
    idents_data = ['First-Name', 'Last-Name']
    user_input = ''
    idents.user = dict.fromkeys(idents_data, user_input)
    idents.user['First-Name'] = input("Please type your first name: \n")
    idents.user['Last-Name'] = input("Please type your second name: \n")
    

def feedback():
    """
    Feedback input from user.
    User chooses an input 0-5
    will loop if not in range
    """
    feedback.final_answers = []

    surveys = [
        "How would you rate your in terminal experience with us?",
        "How would you rate youe in flight experience?",
        "How comfortable did you feel on your whole journey?",
        "How were the staff towards you on your journey?",
        "How likely are you to recommend us to someone?"
    ]

    for survey in surveys:
        answer = get_answer(0, 5, f"{survey}? \n")
        feedback.final_answers.append(answer)
    return feedback.final_answers


def get_answer(low, high, prompt):
    """
    Will check if values are equal to or between 0-5.
    Raises ValueError if not in range
    """
    while True:
        answer = input(prompt)
        if answer.isnumeric():
            if low <= int(answer) <= high:
                return int(answer)
            else:
                print("Make sure your answer is between 0-5")
        else:
            print("This is not a number, please try again.")


def submit():
    """
    Checks if user is happy with input by typing yes/no
    If yes, survey ends.
    If no, loops back to questions.
    If neither, provides error and repeats yes/no question.
    """
    print("Would you like to submit these answers?")
    user_submit = input("Please enter yes or no: \n")
    lower_submit = user_submit.lower()
    if lower_submit == "yes":
        print("Thank you for your time and hope to see you soon!")
        print(f"Hope you and have a great day!{idents.user['First-Name']}  \n")
    elif lower_submit == "no":
        main_repeated()
    else:
        print("Please answer yes or no.")
        submit()


def user_data(data):
    """
    To collect all of users data and push to google sheet.
    """
    print("Submitting your answers.....\n")
    update_sheet = SHEET.worksheet("names")
    update_sheet.append_row(data)
    print("Answers sent! Thank you!")
    print("Have a nice day!:)")


def main():
    """
    Run all program functions
    """
    intro()
    idents()
    now = date.today()
    today = now.strftime("%d/%m/%Y")
    print("Today's date is:", today)
    print("Please answer the below questions.")
    print("Your answer should be a figure between 0-5")
    print("0 = Thoroughly disagree; 5 = Very much agree.\n")
    feedback()
    print(f"Thank you {idents.user['First-Name']}!")
    print(f"Here are your final answers: {feedback.final_answers}")
    submit()
    user_data(feedback.final_answers)


def main_repeated():
    """
    Repeats all program functions
    """
    print("Please answer the below questions.")
    print("Your answer should be a figure between 0-5")
    print("0 = Thoroughly disagree; 5 = Very much agree.\n")
    feedback()
    print(f"Thank you {idents.user['Name']}!")
    print(f"Here are your final answers: {feedback.final_answers}")
    submit()
    user_data(feedback.final_answers)


main()
