print("welcome")


score = 0

answer1 = input("what language are we using: ") #Python
if answer1.lower() == "python":
    print("bravo")
    score += 1

answer2 = input("what command starts a git: ") #Python
if answer2.lower() == "git init":
    print("bravo")
    score += 1


else:
    print("wrong")
    print("your score is: ", score)