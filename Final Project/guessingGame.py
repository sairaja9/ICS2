#import colors

# Intro to Computer Science: Final Project Template
characters = {
    # Athletes
    'Stephen Curry': ['30-35', 'tall', 'basketball player', 'shooting'],
    'Usain Bolt': ['30-35', 'tall', 'track runner', 'speed'],
    'Serena Williams': ['35-40', 'average', 'tennis player', 'championships'],
    # Actors/Singers
    'Justin Bieber': ['20-25', 'average', 'male singer', 'voice'],
    'Dwayne Johnson': ['45-50', 'tall', 'male actor', 'The Rock'],
    'Taylor Swift': ['25-30', 'average', 'female singer', 'voice'],
    # Scientists/Engineers/Business Owners
    'Elon Musk': ['45-50', 'tall', 'businessman', 'Tesla'],
    'Bill Gates': ['60-65', 'average', 'businessman', 'Microsoft'],
    'Mark Zuckerburg': ['30-35', 'short', 'businessman', 'Facebook'],
    # Political Figures
    'Barack Obama': ['55-60', 'average', 'politician', 'president'],
    'George W. Bush': ['70-75', 'tall', 'politician', 'president'],
    'Bill Clinton': ['70-75', 'tall', 'politician', 'president']
}

########## Introduction ##########
intro_text = '''
The quick fun associated with a guessing game can help you kill time in a car ride, a long line, or any of the million boring situations.  Run this program with your friends and family whenever you feel the need to have some fun.  Think of a famous person right now.  The program will ask you questions like: how old is your character, is he an athlete? etc.  The program will continue to ask you questions until it chooses a character.  See if you can outthink the program.  If you want more of a challenge, add a new character to program’s dictionary.  Have fun!\n'''

############ Functions ##############


class gamePath(object):

    def __init__(self):
        self.inputOptions_a1 = []
        self.inputOptions_a2 = []
        self.inputOptions_a3 = []
        self.inputOptions_a4 = []
        self.q1 = str(input("\nHow old is your character (e.g. 40-45)? "))
        self.q2 = str(
            input("Do you consider your person to be tall, short, or average in height? "))
        self.q3 = str(input(
            "What is the occupation of your character?(businessman, politician, actor, or _[sport]_ player.) "))
        self.q4 = str(input(
            "What is your character known for? (president, [company name], nickname, voice, speed, championships, etc.). "))

    def getInputOptions(self, dictionary):

        attributes = characters[person]

        for person in characters:
            self.inputOptions_a1.append(attributes[0])

        for person in characters:
            self.inputOptions_a2.append(attributes[1])

        for person in characters:
            self.inputOptions_a3.append(attributes[2])

        for person in characters:
            self.inputOptions_a4.append(attributes[3])

    def questions(self):
        if self.q1 not in self.inputOptions_a1:
            print("That age range is invalid. Try again.")
        elif self.q2 not in self.inputOptions_a2:
            print("That height is invalid. Try again.")
        elif self.q3 not in self.inputOptions_a3:
            print("That occupation is invalid. Try again.")
        elif self.q4 not in self.inputOptions_a4:
            print(
                "That input is invalid. Please choose one of the example inputs. Try again.")

    def checkWithDictionary(self, dictionary):

        self.input_list = []
        self.input_list.append(q1)
        self.input_list.append(q2)
        self.input_list.append(q3)
        self.input_list.append(q4)

        for person in characters:
            attributes = characters[person]
            if attributes == input_list:
                #final_question = input("\n\nIs " + colors.red(person) + " your character? ")
                final_question = input("\n\nIs " + person + " your character? ")
                if final_question == 'yes' or final_question == 'y':
                    print("\nHaha! I can read your mind.")
                else:
                    print("Looks like you can out think me.  I challenge you to another game!")

    def add():
        pass


game = gamePath()
############ Main Game Loop #########
run = True
print(intro_text)
while run:
    question1 = input("\nWould you like to play the guessing game? ")
    if question1 == 'yes' or question1 == 'y':
        print("\nHere is a list of characters to choose from.")
        for count, item in enumerate(characters, 1):
            #print(count, colors.green(item))
            print(count, item)
        question3 = input("\nPress c to continue or press any key to quit. ")
        if question3 == 'c':
            game.getInputOptions(characters)
            game.questions()
            game.checkWithDictionary(characters)
        else:
            run = False
    else:
        question2 = input("Would you like to add a character? ")
        if question2 == 'yes' or question2 == 'y':
            add()
        else:
            question3 = input("Press any key to quit the game? ")
            if question3 == 'y':
                run = False
            else:
                run = False
