from sys import argv

script, firstname, lastname = argv

firstname = raw_input("What's your first name")
lastname = raw_input("what's your last name")

print "The script is called:", script
print "Your first name is:", firstname
print "Your last name is:", lastname
print "\tYour name is ",firstname+lastname

