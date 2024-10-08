class QuizBrain:
    def __init__(self, question_list):
        self.question_number = -1
        self.question_list = question_list
    
    def next_question(self, question_number):
        self.question_number = question_number + 1
        return self.question_list[self.question_number]

# check if the answer is correct
    def check_answer(self, answer):
        if self.question_list[self.question_number].answer == answer:
            return True 
        else:
            return False
                    
                     
    def is_end (self):
        # if question number is max then return true
        # a better way:
        # return self.question_number < len(self.question_list)-1:
        if self.question_number < len(self.question_list)-1:
            print(self.question_number)
            print(len(self.question_list))
            return True
        else:
            print(self.question_number)
            print(len(self.question_list))
            return False
            