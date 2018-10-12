from random import randint

fortunes = [
"The princess is in another castle", # Adam
"The future looks bright!", # jesse
"Keep up the hard work", # jesse
"Get a flu shot this year", # jesse
"¯\\_(ツ)_/¯" # jesse
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
	random_index = randint(0, len(fortunes) - 1)
	print(fortunes[random_index])
	user_input = input()