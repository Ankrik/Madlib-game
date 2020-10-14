""" Mad Libs Generator
       Game...
    HAPPY CODING 
"""

loop = 1
while (loop < 10):
#These are the questions asked by the computer to the player
    noun = input("Enter a noun: ")
    p_noun = input("Enter a plural noun: ")
    noun2 = input("Enter a noun: ")
    place = input("Name a place: ")
    adjective = input("Enter an adjective (Describing word): ")
    noun3 = input("Enter a noun: ")
#This code will display the story based on the users input
    print ("------------------------------------------")
    print ("Be kind to your",noun,"- footed", p_noun)
    print ("For a duck may be somebody's", noun2,",")
    print ("Be kind to your",p_noun,"in",place)
    print ("Where the weather is always",adjective,".")
    print ()
    print ("You may think that is this the",noun3,",")
    print ("Well it is.")
    print ("------------------------------------------")
# Loop back to "loop = 1"
    loop = loop + 1