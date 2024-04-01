print("**********************************")
print("   Welcome to Quiz Game : ")
question_bank = [{"text":"1. Who developed Python Programming Language?","Answer":"c"},
            {"text":"2. Is Python case sensitive when dealing with identifiers?","Answer":"b"},
            {"text":"3. Which of the following is the correct extension of the Python file?","Answer":"c"},
            {"text":"4. Which of the following is used to define a block of code in Python language?","Answer":"a"},
            {"text":"5. Python supports the creation of anonymous functions at runtime, using a construct called","Answer":"c"},
            {"text":"6. What does pip stand for python?","Answer":"c"},
            {"text":"7. Which of the following is the truncation division operator in Python?","Answer":"b"},
            {"text":"8. Which of the following is the use of id() function in python?","Answer":"b"},
            {"text":"9. Which of these is the definition for packages in Python?","Answer":"b"},
            {"text":"10. What arithmetic operators cannot be used with strings in Python?","Answer":"b"}, ]


options = [["a. Wick van Rossum ","b. Rasmus Lerdorf","c. Guido van Rossum" ,"d. Niene Stom"],
           ["a. No ","b. Yes ","c. Machine dependent" ,"d. None of these"],
           ["a. .python ","b. .pl ","c. .py" ,"d..p"],
           ["a. indention ","b. key","c. bracket " ,"d. All of mention"],
           ["a. pi ","b.anaonymaous","c. lambda" ,"d. None of the mentiones"],
           ["a.pip install puthon ","b. pip install packahges","c.prefersed installer program" ,"d. All of the mention"],
           ["a. | ","b. // "," c. / " ,"d. %"],
           ["a. Every object doesn’t have a unique id ","b. Id returns the identity of the object","c.All of the mentioned" ,"d. None of the mentioned"],
           ["a. A set of main module  ","b. A folder of python modules","c.  A number of files containing Python definitions and statements" ,"d.  A set of programs making use of Python modules"],
           ["a.* ","b.-","c.+ " ,"d. All of the mention"]]


score = 0
def check_answer(user_guess,correct_answer):
    if user_guess==correct_answer:
        return True
    else :
        return False

for question_number  in range(len(question_bank)):
    print("*********************************")
    print(question_bank[question_number]["text"])
    for i in options[question_number]:
        print(i)
        
    guess=input("Enter your answer (a/b/c/d):")
        
    is_correct= check_answer(guess,question_bank[question_number]["Answer"])
    if is_correct:
        print(" Correct answer ")
        score +=1
    else:
        print(" Incorrect answer ")
        print(f" The correct answer is: {question_bank[question_number]['Answer']} ")
    
    print(f"Your current score {score}/{question_number+1} ")
print(f"Your have gievn  {score } Annwer")
print(f"Your Score is{(score/len(question_bank))*100}%")
  
