class QuizBrain:
    def __init__(self, question_list):
        self.question_num = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        curr_q = self.question_list[self.question_num]
        self.question_num += 1
        user_answer = input(f"Q. {self.question_num}: {curr_q.text} (True/False): ")
        self.check_answer(user_answer, curr_q.answer)

    def still_has_q(self):
        return self.question_num < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Correct!")
            self.score_fun()
        else:
            print("Incorrect...")
        print(f"The correct answer is: {correct_answer}.")
        print(f"You current score is: {self.score}/{self.question_num}.\n")

    def score_fun(self):
        self.score += 1