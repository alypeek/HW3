# Your name: Alyssa Peek
# Your student id: 87576945
# Your email: alypeek
# Who or what you worked with on this homework (including generative AI like ChatGPT): Carolina Janicke, Asa Garcia, ChatGPT

# If you worked with generative AI also add a statement for how you used it.  
# e.g.: 
# Asked Chatgpt hints for debugging and suggesting the general sturcture of the code


import random

# create a magic 8 ball class
class MagicEightBall():

    # create the constructor (__init__) method 
    # ARGUMENTS: 
    # Self the current object
    # Answers a list of potential answers
    # RETURNS: None
    def __init__(self, answers):
        self.answers_list = answers 
        self.questions_history_list = []
        self.answers_history_list = []
        
    # Create the __str__ method
    # ARGUMENTS: 
    # Self the curent object
    # RETURNS: a string with all of the questions in the questions_history_list separated by commas
    #        iIf no questions have been asked, return an empty string
    def __str__(self):
        if self.questions_history_list == []:
            return []
        else:
            return ','.join(self.questions_history_list)
    

    # Creates the get_fortune method
    # ARGUMENTS:

    # Question: the question the user wants to ask the magic 8 ball
    # RETURNS: a string with the answer
    def get_fortune(self, question):
        if question in self.questions_history_list:
            return "I’ve already answered this question"
        else:
            index = random.randint(0, len(self.answers_list) - 1)
            answer = self.answers_list[index]
            self.answers_history_list.append(index)
            return answer

    # Creates play_game method
    # ARGUMENTS:
    #self the current object
    # RETURNS: None
    def play_game(self):
        user_ques = input("Please enter a question: ")
        while user_ques != "I'm done playing":
            print(self.get_fortune(user_ques))
            self.questions_history_list.append(user_ques)
            user_ques = input("Please enter a question: ")
        if user_ques == "I'm done playing":
            print("Goodbye")
        

    # Create the print_answer_frequencies method
    # ARGUMENTS: 
    #self the curent object
    # RETURNS: dictionary that maps answers to frequencies
    #          if no answers have been given, return an empty dictionary
    def print_answer_frequencies(self):
        
        if self.answers_history_list == []:
            print("None yet")
        
        freq_dict = {}
        unique_answers = set(self.answers_history_list)

        for answer in self.answers_history_list:
            if answer != "I’ve already answered this question":
                freq = self.answers_history_list.count(answer)
                print(f"The answer {self.answers_list[answer]} has been given {freq} times.")
                freq_dict[self.answers_list[answer]] = freq
        
        return freq_dict



def test():
    answers_list = ['yes', 'no', 'maybe']
    eight_ball = MagicEightBall(answers_list)

    print("Test __init__:")
    print(f"Answer History List: Expected: {[]}, Actual: {eight_ball.answers_history_list}")
    print(f"Question History List: Expected: {[]}, Actual: {eight_ball.questions_history_list}")
    print(" ")

    print("Test __str__:")
    eight_ball.questions_history_list = ['will it snow today?', 'should I make soup?']
    expected = "will it snow today?, should I make soup?"
    print(f"Expected: {expected}, Actual: {str(eight_ball)}")
    print(" ")


    print("Testing return value of get_fortune:")
    res = eight_ball.get_fortune('test question')
    print(f"Expected: {str}, Actual: {type(res)}")
    print(" ")

    print("Testing get_fortune:")
    eight_ball.answers_list = ['yes']
    res = eight_ball.get_fortune('test question 2')
    print(f"Expected: {'yes'}, Actual: {res}")
    print(" ")

    print("Testing that get_fortune adds answer index to answer_history_list:")
    eight_ball.answers_list = ['yes']
    eight_ball.answers_history_list = []
    eight_ball.get_fortune('test question 2')
    expected = [0]
    res = eight_ball.answers_history_list
    print(f"Expected: {expected}, Actual: {res}")
    print(" ")

    print("Testing that get_fortune does not add 'I've already answered this question' to answer_history_list:")
    eight_ball.answers_list = ['yes']
    eight_ball.answers_history_list = [0]
    eight_ball.questions_history_list = ['test question 3']
    eight_ball.get_fortune('test question 3')
    expected = [0]
    res = eight_ball.answers_history_list
    print(f"Expected: {expected}, Actual: {res}")
    print(" ")


    print("Testing return value print_answer_frequencies")
    eight_ball.answers_list = ['yes', 'no', 'maybe']
    eight_ball.answers_history_list = [0, 0, 0, 1, 1, 2]
    res = type(eight_ball.print_answer_frequencies())
    print(f"Expected: {dict}, Actual: {res}")
    print(" ")

    print("Testing return value print_answer_frequencies keys")
    eight_ball.answers_history_list = [0, 0, 0, 1, 1, 2]
    res = type(list(eight_ball.print_answer_frequencies().keys())[0])
    print(f"Expected: {str}, Actual: {res}")
    print(" ")

    print("Testing print_answer_frequencies")
    eight_ball.answers_history_list = [0, 0, 0, 1, 1, 2]
    res = eight_ball.print_answer_frequencies()
    expected = {'yes': 3, 'no': 2, 'maybe': 1}
    print(f"Expected: {expected}, Actual: {res}")
    print(" ")

def mytest():
    answers_list = ['yes', 'no', 'maybe']
    eight_ball = MagicEightBall(answers_list)

    print("Testing print_answer_frequencies when no questions have been asked.")
    eight_ball.answers_history_list = []
    res = eight_ball.print_answer_frequencies()
    expected = {}
    print(f"Expected: {expected}, Actual: {res}")
    print()

    print("Testin print_answer_frequencies when answers_list is ['It is certain', 'Don't count on it']")
    eight_ball.answers_list = ['It is certain', "Don't count on it"]
    eight_ball.answers_history_list = [0, 1, 1]
    res = eight_ball.print_answer_frequencies()
    expected = {'It is certain': 1, "Don't count on it": 2}
    print(f"Expected: {expected}, Actual: {res}")
    print()

    print("Testing get_fortune when a question has already been asked.")
    eight_ball.questions_history_list = ['Test question 3']
    res = eight_ball.get_fortune('Test question 3')
    expected = "I've already answered this question"
    print(f"Expected: {expected}, Actua;: {res}")
    print()    

def main():
    #defines the possible answers
    possible_answers = ["Definitely", "Most likely", "It is certain", "Maybe", "Cannot predict now", "Very doubtful", "Don't count on it", "Absolutely not"]
    # Creates a MagicEightBall object
    magic_8_ball = MagicEightBall(possible_answers)
    #initiates the game play using the play_game method
    magic_8_ball.play_game()
    # shows the output of print_answer_frequencies
    frequencies = magic_8_ball.print_answer_frequencies()
    print(f'Answer frequencies: {frequencies}')
    



# Only run the main function if this file is being run (not imported)
if __name__ == "__main__":
    main()
    test() 
    mytest()
    # TODO: Uncomment if you do the extra credit