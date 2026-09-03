
# Strings are immutable datatyep
# strings are created by using ''
#  as string are immutable we cannot perform CRUD operation09?-
s = 'Today is a great day for me and manasa' 

# t = '''New Delhi: Prime Minister Narendra Modi posted yet another video on Instagram Friday night, where he said he 
#     wanted to forgive the young protesters
#  who hurled abuses at him and his late mother during the demonstrations at Jantar Mantar'''
# t = 'yes!!'

# how to convert strng into list by using sorted function
print(sorted(s))

print(s[1])


print(s.title()) 
# 'prints Sneha Adavimath first letter in upper case

print(s.upper())
# prints SNEHA ADAVIMATH

print(s.lower())
# prints sneha adavimath

print(s.capitalize())
# print Sneha adavimath

print(s.count('a'))
# prints count of a 4

print(s.strip())
# removes whitespaces

print(s.lstrip())
print(s.rstrip())

# slice(start:stop:step)
print(s[1:8:2])

print(s[::-1])
# htamivadAahens

print(len(s))

print(s.replace(' ', '' ))

