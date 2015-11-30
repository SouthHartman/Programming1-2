# john
# period 4
# 11/23/15

# 9.2.1

# this will get a name and grade level, and print out a greeting

name = input("What is your name?  ")
grade = int(input("What grade are you in?  "))

if grade == 9:
    print ("Hello, %s, welcome to your first year of high school." %(name))
elif grade == 10:
    print ("I hope to see you in class %s." %(name))
elif grade == 11:
    print ("You're almost a senior, %s." %(name))
elif grade == 12:
    print ("Woo hoo last year I have to deal with you, %s." %(name))
else:
    print ("Sorry invalid grade.")
