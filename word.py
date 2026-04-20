print("        WELCOME TO WORLD GUESSING GAME     ")
print("___________________________________________")
print()
# general Total score award
score=0
print("FOR  ENTER THE GAME PLEASE ENTER THE WORD  START ->0 ")
s=int(input())
if(s==0):
    print("Now Let's  start")
    print()
    print("  HOW TO  PLAY " )
    print("1. Read the question carefully ")
    print("2.Fill in the blanks to guess the word")
    print("3.Use underscores to represent missing letters")
    print("4.Each correct guess will earn you points")
    print()
    print("Please enter the number 1 ")
    i=int(input())
    if(i==1):
       class part1:
            def set_Name(self, Name):
                self.Name = Name

            def get_name(self):
                return self.Name

            def set_score(self, score):
                if score == 0:
                    self.score = 0
                elif score == 3:
                    self.score = score
                else:
                    self.score = score

            def get_score(self):
                return self.score

    p = part1()

    print("Enter Your Name : ")
    ame = input()
    p.set_Name(ame)

    score = 0

        # function defined properly
    def play_level(question, answer):
            print("          Guess The Word         ")
            print("___________________________________")
            print(question)

            attempts = 3
            while attempts > 0:
                guess = input("Enter the word: ").lower()

                if guess == answer:
                    print("Correct!")
                    return 3
                else:
                    attempts -= 1
                    print("Try again")

            print("Out of attempts")
            return 0

        # levels
    score += play_level("J_p_n", "japan")
    print("Level -2")

    score += play_level("M_x_c_", "mexico")
    print("Level -3")

    score += play_level("A_E_T_R_A_M", "amsterdam")

        # update score in class
    p.set_score(score)

    print(p.get_name())
    print("Your Score is :", p.get_score())
    print("THANK FOR VISITING OUR GAME ")
    exit()

else:
    print()
    print("THANK FOR VISITING OUR GAME ")
    exit()