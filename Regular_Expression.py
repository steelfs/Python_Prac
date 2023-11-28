'''
 . (matches any single character), ^ (beginning of a line), $ (end of a line), * (zero or more occurrences of the preceding element),
   and + (one or more occurrences of the preceding element).

   []	A set of characters	"[a-m]"	
\	Signals a special sequence (can also be used to escape special characters)	"\d"	
.	Any character (except newline character)	"he..o"	
^	Starts with	"^hello"	
$	Ends with	"planet$"	
*	Zero or more occurrences	"he.*o"	
+	One or more occurrences	"he.+o"	
?	Zero or one occurrences	"he.?o"	
{}	Exactly the specified number of occurrences	"he.{2}o"	
|	Either or	"falls|stays"	
()	Capture and group

\A	Returns a match if the specified characters are at the beginning of the string	"\AThe"	
\b	Returns a match where the specified characters are at the beginning or at the end of a word
(the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\bain"

r"ain\b"	

\B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
(the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\Bain"

r"ain\B"	

\d	Returns a match where the string contains digits (numbers from 0-9)	"\d"	
\D	Returns a match where the string DOES NOT contain digits	"\D"	
\s	Returns a match where the string contains a white space character	"\s"	
\S	Returns a match where the string DOES NOT contain a white space character	"\S"	
\w	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	"\w"	
\W	Returns a match where the string DOES NOT contain any word characters	"\W"	
\Z	Returns a match if the specified characters are at the end of the string
'''

import re
txt = 'The rain in spain'

count = re.findall('in', txt)
print(len(count))

# txt = 'it\'s raining Today'
# result = re.search('^it.$Today', txt)

# if result:
#     print('match')
# else:
#     print('there\'s Nothing')

#x = re.findall('in', txt)
# x = re.search('\s', txt)
# y = re.search('apple', txt)

# print(f'x = {x}')
# print(f'y = {y}')

# print('y exist') if y else print('there isn\'t')

#x = txt.split(' ', 3)
#print(x)
# x = re.sub('\s', '9', txt)
# print(x)
# y = re.split('\s', txt)
#print(y)
#x = re.search('in', txt)
    
# x = re.search('\bS\w+', txt)
# print(x)
