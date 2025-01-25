class QuizBrain:
    def __init__(self,q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):
        total_questions = len(self.question_list)
        if self.question_number<total_questions:
            return True
        else:
            return False

    def check_answer(self,ans,choice):
        if ans == choice:
            self.score+=1

    def next_question(self):
        current_question = self.question_list[self.question_number]
        choice = input(f'Q{self.question_number+1}: {current_question.text} (True/False)').title()
        self.question_number+=1
        ans = current_question.answer
        self.check_answer(ans,choice)


    def display_mark(self):
        print(f"you have scored {self.score}")



