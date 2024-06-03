def verify_code(entered_code, correct_code):
    return entered_code == correct_code

def access_quiz():
    correct_code = "1234" 
    entered_code = input("Enter the code to access the quiz: ")
    
    if verify_code(entered_code, correct_code):
        print("Code accepted. You can now access the quiz.")
        
    else:
        print("Incorrect code. Please try again.")

access_quiz ()