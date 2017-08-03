#Udacity project 2
#Thank you for reading!



#variable
name = ""
#intro
print ("How well do you superheroes?")
name = input("But first..what's your name?")
print ("Hi "+ name + "!")


#These list of blanks are in the same order as shown below
blanks = ["___1___","___2___","___3___"]

#These strings range from easy to hard difficulty
easy = '''Superman aka Clark ___1___ is an awesome superhero. He is from planet ___2___. His weakness is ___3___.'''
medium = '''Iron man is portrayed by ___1___ Downey Jr.  He began making ___2___ thousand dollars for the first movie. For the Avengers, the infinity wars, he is expected to make ___3___ million dollars.'''
hard = '''Spiderman has been played by three actors since 2002.  Their full names are ___1___, ___2___, and ___3___.'''
#These are the correct answers
answers_list_easy = ["Kent", "Krypton", "Kryptonite"]
answers_list_medium = ["Robert", "500", "200"]
answers_list_hard = ["Tobey Maguire", "Andrew Garfield", "Tom Holland"]




#This has the various difficulty levels available to the player
listuserlvl = ["easy","medium","hard"]
userlvl = ""
userlvl = input("Type in your difficulty level")


#input received matches to levels of difficulty paragraph
def lvl(userlvl):
    if userlvl == "easy" or userlvl == "Easy" or userlvl == "EASY":
        return easy
    elif userlvl == "medium" or userlvl == "Medium" or userlvl == "MEDIUM":
        return medium
    elif userlvl == "hard" or userlvl == "Hard" or userlvl == "HARD":
        return hard
    else:
        print ("Not an option.  Try again.")
    pass


#Takes input and compares it with answer
def compare(userlvl):
    if lvl(userlvl) == easy:
        return answers_list_easy
    if lvl(userlvl) == medium:
        return answers_list_medium
    if lvl(userlvl) == hard:
        return answers_list_hard
    pass


#This part determines right or wrong
def check(user_answer, answers_list, answers_index):
    if user_answer == answers_list[answers_index]:
        return ("Right")
    return ("Incorrect")
    pass



#The part to actually play the game
def playgame():
    quiz = lvl(userlvl)        
    print 
    print quiz
    print ("You get 3 tries. GL!")
    
    
    answers_list = compare(userlvl)    
    
    #these are the preset values 
    answers_index = 0  
    blanks_index = 0                                                               
    guesses_limit = 0  
    number_of_guesses = 3       
    
    #This loop continues as the number of blanks aren't changed
    while blanks_index < len(blanks):   
        user_answer = ""
        user_answer = input("Input answer for " + blanks[blanks_index] )
        
        if check(user_answer,answers_list,answers_index) == "Right":
            print ("You got it")
            quiz = quiz. replace(blanks[blanks_index],user_answer)
            
            answers_index += 1
            number_of_guesses = 3
            blanks_index += 1
            
            print quiz
            if blanks_index == len(blanks):
                print ("You did amazing " + name)
        else:
            number_of_guesses -= 1
            if number_of_guesses == guesses_limit:
                print ("Game over " + name + "!")
            else:
                print ("Please try again " + name)
                print ("You have " + str(number_of_guesses) + " more tries.")


                
                
playgame
#End of code