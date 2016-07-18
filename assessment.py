"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

The three main design advantages that object orientation can provide are
Encapsulation, Abstraction and Polymorphism. Encapsulation references keeping
the data close to the functions used to manipulate the data. Abstraction refers 
to the ability to hide the details of data manipulation such that it is not
necessary to know how it works, just how to make it do what you want. For 
example, Python provides the "append" method. Abstraction is what allows me to 
use this method without actually knowing how the code works underneath. 
Polymorphism allows you to make use of methods that you have written in other
circumstances as to not reinvent the wheel every time you have a new class.  

2. What is a class?

An object in python. Classes allow us to store data in a structured fashion, as 
well as allowing us to define our own methonds on how to manipuate the data. 
Unlike a dictionary, classes are not limited to the actions possible to
dictionaries, they have their own smarts!

3. What is an instance attribute?

An attribute that belongs to an instance of a class. For example, if I create a 
class called "books," and I instantiate that class by creating an instance 
called my_book. I can attach certain attributes to my_book such as the title, 
number of pages, genre, etc. 

4. What is a method?

A method is a function that is defined inside of a class. 

5. What is an instance in object orientation?

An instance is an object created in the class, once instantiated can be
manipulated by using all methods within the class. 

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

A class attribute is an attribute associated with every instance that is 
instantiated in a class, it is a piece of data on the class itself. An instance 
#attribute is an attribute particular to an instance, it is set directly on the 
#object. For example, using the book example above, lets say I create a 
subclass of the Book class called "FictionBooks." I could make a class attribute 
called "genre" and set it to fiction. I would not make a class attribute for 
"title" since we do not want all instances to have the same title. We would set 
this as an instance attribute, so that it could very based on the instance. 

"""
#define class called Student
class Student(object):
    """Student class."""
    #Instantiates a student

    def __init__(self, firstname, lastname, address):
        """Initialize a student."""

        self.firstname = firstname
        self.lastname = lastname    
        self.address = address

#define class called Question
class Question(object):
    """Question class"""
    #instantiates a question by asking for the question and its answer.
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
    
    #Asks the question of the user and checks if input matches the answer.
    def ask_and_evaluate(self):
        #prints the question
        print self.question
        #takes answer as user input. 
        user_answer = raw_input(">>>")

        #Checks if both user input and answer are strings. 
        if (type(user_answer) is str) and (type(self.answer) is str):
            #verifies if the strings are the same, if so returns True. 
            if user_answer.lower() == self.answer.lower():
                return True
            #if the strings do not match, returns False. 
            else:
                return False
        #In the instance that the answer requires a number, verifies if the 
        #numbers match, if they do returns True. Otherwise returns False. 
        if float(user_answer) == float(self.answer):
            return True
        else:
            return False
        #NOTE: this does not account for if someone is supposed to put a float, 
        #but puts a string. This will be an error. Not sure how to fix.



class Exam(object):
    """Exam class"""
    #Instantiates an exam by asking for the name of the exam.
    def __init__(self, name):
        self.name = name
        #automatically creates an attribute called questions so that questions
        #can be added to this empty list. 
        self.questions = []

    #Method that adds a question by requiring a questions and the correct answer.
    def add_question(self, question, correct_answer):
        #Makes the input an instance of the Question class. 
        new_question = Question(question, correct_answer)
        #adds this instance to the list of questions associated with the exam. 
        self.questions.append(new_question) 
        
    def administer(self):
        #Start with zero correct. 
        score = 0
        #for the questions in the questions list, it runs the ask_and_evaluate
        #method. 
        for s in self.questions:
            if s.ask_and_evaluate() == True:
                score = score + 1
        #Assigns the instance attribute score to the instance. 
        self.score = score
        return score

class Quiz(Exam):

    def administer(self):
        #calls the administer method from the Exam class. 
        super(Quiz, self).administer()
        
        #finds how many questions are in the list of questions.
        total_questions = len(self.questions)

        #Checks if the score is greater than or equal to 50% of questions. 
        #Returns "Pass" if yes, returns "Fail" if not. 
        if self.score >= float(total_questions)/2:
            return "Pass"
        else: 
            return "Fail" 

##### MY EXAM #####

def take_test(exam, student):
    #gets the students score after administering an exam.
    student_score = exam.administer()
    #Assigns student and instance attribute called score to the returned value 
    #student_score from the exam adminstration.
    student.score = student_score
    
    return student.score

def take_quiz(quiz, student):
    #gets the students score after administering an quiz.
    student_result = quiz.administer()
    #Assigns student and instance attribute called score to the returned value 
    #student_score from the exam adminstration.
    student.result = student_result
    
    return student.result

def testexample():
    exam = Exam('Midterm')

    #Exam questions being added to the instance in class Exam. 
    exam.add_question('What is the capital of California?','Sacramento')
    exam.add_question('What is the capital of Arizona?','Phoenix')
    exam.add_question('What is 3+3?', 6)
    exam.add_question('What is Hackbright\'s mascot?','Balloonicorn')

    #Created a fake student
    student = Student('Fakey','Student','555 Sutter')
    #call the take_test function.
    take_test(exam, student)
    #prints student name, name of the exam and score. 
    print "Score for {} on {}: {}".format(student.firstname, exam.name, student.score)

def quizexample():
    #created instance in class Quiz
    quiz = Quiz('Chapter Quiz')

    #Quiz questions being added to instance in class Quiz. 
    quiz.add_question('What is the capital of California?','Sacramento')
    quiz.add_question('What is the capital of Arizona?','Phoenix')
    quiz.add_question('What is 3+3?', 6)
    quiz.add_question('What is Hackbright\'s mascot?','Balloonicorn')
    quiz.add_question('What is the name of Krishelle\'s cohort?','Ada')

    #Created a fake student
    student = Student('Ima','Class-Clown','555 Sutter')
    #call the take_quiz function.
    take_quiz(quiz,student)
    #prints student name, name of quiz and 'pass' or 'fail' result. 
    print "Result for {} on {}: {}".format(student.firstname, quiz.name, student.result)

#Uncomment thisto test the testexample function. 
# my_test = testexample()

#Uncomment this to test the quizexample function.
# my_quiz = quizexample()















