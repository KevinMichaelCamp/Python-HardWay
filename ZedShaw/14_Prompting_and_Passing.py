# Python - The Hard Way - Exercise 13 - Parameters, Unpacking, Variables

from sys import argv

script, user_name, age = argv
prompt = '~ '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I see you are %s years old." % age
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live, %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Move back to Colorado.
And you have a %r computer. Nice
""" % (likes, lives, computer)
