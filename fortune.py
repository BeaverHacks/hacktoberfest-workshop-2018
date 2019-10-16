from random import randint

fortunes = [
"The princess is in another castle", # Adam
"The future looks bright!", # jesse
"Keep up the hard work", # jesse
"Remember to use Git Bash for workshops", # jesse
"Get good sleep and drink lots of water", # Andrew
"¯\\_(ツ)_/¯", # jesse
"Jesse rocks! Loving the workshop.", # Sora
"Today you will meet someone that will impact your entire existance, pay attention", # vinny
"new fortune", #greg
"Every man is the architect of his own fortune",
"Fortune favors the brave",
"When fortune knocks open the door"
]

print("""
              *    .
        '  +   ___    @    .
            .-" __"-.   +
    *      /:.'`__`'.\\       '
        . |:: .'_ `. :|   *
   @      |:: '._' : :| .
      +    \\:'.__.' :/       '
            /`-...-'\\  '   +
   '   jgs /         \\   .    @
     *     `-.,___,.-'
""")
# source: http://www.oocities.org/spunk1111/mythical.htm#crystal

print("Enter any key to get a fortune, or q to quit:")
user_input = input()
while user_input is not "q" and user_input is not "Q":
	# to generate a random index from 0 to length - 1
	# printing the fortune at random index generated
	random_index = randint(0, len(fortunes) - 1)
	print(fortunes[random_index])
	user_input = input()
