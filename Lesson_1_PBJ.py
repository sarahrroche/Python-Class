#		How much jelly do you have? (make this a number that reflects how many sandwiches-worth of jelly you have)

# For this exercise, we'll assume you have the requisite tools (plate, knife, etc)

# Once you've defined your variables that tell you how much of each ingredient you have, use conditionals to test whether you have the right amount of ingredients

##if bread_sammy >= 1 and jelly >= 1 and peanut_butter >=1:
##    print "You can make yourself a PB&J!"
##else:
##    print "No lunch. Ever."
##    
    


# Based on the results of that conditional, display a message.

# To satisfy the first goal:
#		If you have enough bread (2 slices), peanut butter (1), and jelly (1), print a message like "I can make a peanut butter and jelly sandwich"; 
#		If you don't; print a message like "Looks like I don't have a lunch today"

# To satisfy the second goal:
#		Continue from the first goal, and add:
#		If you have enough bread (at least 2 slices), peanut butter (at least 1), and jelly (at least 1), print a message like "I can make this many sandwiches: " and then calculate the result.
#		If you don't; you can print the same message as before

if peanut_butter>=1 and jelly >=1 and bread_sammy >=1:
    sandwich = bread_sammy
    if peanut_butter <= sandwich:
        sandwich = peanut_butter
    if jelly <= sandwich:
        sandwich = jelly
    print "You can make {0} sandwiches".format(sandwich)
    if bread % 2 == 1:
        print "You can make an open faced sandwich."
else:
    print "You can't make any sandwiches"

if jelly < 1:
        print "You are out of jelly!"
elif peanut_butter < 1:
        print "You need more PB. You only have some J"
elif bread_sammy < 1:
        print "Head to the bakery!"
else:
    print "You have all the ingredients"


# To satisfy the third goal:
#		Continue from the second goal, and add:
#		If you have an odd number of slices of bread* and odd amount of peanut butter and jelly, print a message like before, but mention that you can make an open-face sandwich, too.
#		If you don't have enough ingredients; still print the same message as before
#		* To calculate whether you have an odd number, see https://github.com/shannonturner/python-lessons/blob/master/section_01_(basics)/simple_math.py

# To satisfy the fourth goal:
#		Continue from the third goal, but this time if you have enough bread and peanut butter but no jelly, print a message that tells you that you can make a peanut butter sandwich
#		Or if you have more peanut butter and bread than jelly, that you can make a certain number of peanut butter & jelly sandwiches and a certain number of peanut butter sandwiches

# To satisfy the fifth goal:
#		Continue from the fourth goal, but this time if you don't have enough ingredients, print a message that tells you which ones you're missing.

