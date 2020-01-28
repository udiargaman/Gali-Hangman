import pandas as pd

class theGame:
    #
    # Manages the game
    # loads the questions and creates a random subset based on game size
    # Or
    # Loads the questions and takes a list of indexes, to create the subset needed and cont a game
    # Can init a new game, or cont a prev game based on the context passed in __init__

    def __init__(self, game_size=10, qlist_str=None, current_question=0, wrong_answers=0):
        self.current_question = current_question
        self.wrong_answers = wrong_answers
        self.game_size = game_size
        self.qlist = None

        if qlist_str:
            self.parseQListString(qlist_str)
            self.game_size = len(self.qlist)

        self.game_on = self.loadQuestions()

        return


    def loadQuestions(self):
        self.full_questions = pd.read_excel("static/questions.xlsx")

        if self.game_size >= len(self.full_questions.index):
            self.game_size = len(self.full_questions.index)

        # if qlist is not defined, set it here (initial setting)
        # else use the index list (qlist) accepted on the instance creation
        if not self.qlist:
            self.game_questions = self.full_questions.sample(self.game_size)
            self.qlist = self.game_questions.index.tolist()
        else:
            self.game_questions = self.full_questions.iloc[self.qlist]

        return True


    # return 2 args (T/F, question object)
    #
    def getCurrentQuestion(self):
        if not self.game_on:
            return False, None

        if self.current_question >= self.game_size:
            return False, None

        try:
            data = self.game_questions.iloc[self.current_question]
            question = oneQuestion(
                data[0],                        #question
                [data[1], data[2], data[3]],    #3 answers
                data[4])                        #index (0,1,2) of correct answer          
        except:
            raise RuntimeError

        return True, question


    def submitAnswerAndMove(self, answer):
        # false -> game over
        if self.current_question >= self.game_size  or  not self.game_on:
            self.game_on = False
            return False

        if answer != self.game_questions.iloc[self.current_question][4]:
            self.wrong_answers += 1

        self.current_question += 1        

        return True


    def gameOn(self):
        return self.game_on


    # return a stringified comma separated list of the question indexes, so it can be stored as a string
    def getQListString(self):
        return ",".join([str(i) for i in self.qlist])
        
    def parseQListString(self, qlist_str):
        self.qlist = [int(i) for i in qlist_str.split(",")]
  

    def getScore(self):
        return self.current_question - self.wrong_answers

    
    def __repr__(self):
        return f'GameOn: {self.game_on}  /  Game size:  {self.game_size}  /  Current: {self.current_question}  /  Wrong: {self.wrong_answers}'


class oneQuestion:
    def __init__(self, question, answers, correct_answer):
        self.question = question
        self.answers = answers
        self.correct_answer = correct_answer

        return

    def __repr__(self):
        return f'Q: {self.question}  /  A: {self.answers}  /  correct: {self.answers[self.correct_answer]}'
