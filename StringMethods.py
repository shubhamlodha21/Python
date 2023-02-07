#Strings are Immutable

S = "!!!!!!!shUbhAM!!!!! !!!!!!!!!!!!!!!!!!! !!!!!!!! !!!LODHA!!!!!!! !!!AA"
print(len(S))
print(S.upper())
print(S.lower())
print(S.rstrip("!"))  #REMOVE RIGHT-END SIDES CHARACTER
print(S.lstrip("!"))  #REMOVE LEFT-END SIDES CHARACTER
print(S.replace("!!!","<")) #REPLACE IN ALL PLACE
print(S.split( )) # SPLIT STRING IF EMPTY SINGLE SPACE IS FIND

introduction = "welcome yOu !"
print(introduction.capitalize()) #FIRST LETTER CAPITALIZE AND REMAINING IN SMALL
print(introduction.center(50)) #ALLIGN TO CENTER
print(S.count("!")) #COUNT OCCARANCE OF STRING

print(S.endswith("!!")) #RETURN T/F IF ENDWITH STRING
print(S.endswith("AA",23,70))

print(S.find("LODHA")) #RETURN INDEX OF STRING

print(S.startswith("!!")) #RETURN T/F IF ENDWITH STRING

print(S.swapcase()) #SWAP CASE OF STRING

print(S.title()) #CONVERTING FIRST LETTER CAPITAL

IS METHODS ==>
# isalnum()	Returns True if all characters in the string are alphanumeric
# isalpha()	Returns True if all characters in the string are in the alphabet
# isascii()	Returns True if all characters in the string are ascii characters
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	Returns True if all characters in the string are whitespaces
# istitle()	Returns True if the string follows the rules of a title
# isupper()	Returns True if all characters in the string are upper case
# join()	Converts the elements of an iterable into a string
# ljust()	Returns a left justified version of the string
# lower()	Converts a string into lower case
# lstrip()	Returns a left trim version of the string