from truth_trees import one, two, three, four

fin = False
print("** Truth Tree creator **\n"
      "** one letter variables only **\n"
      "** spaces between all elements **\n"
      "** all implicit brackets must be explicit (eg. p v q v r won't be accepted **\n\n")
while not fin:
    print("Pick an option:\n"
          "1)Run examples\n"
          "2)Satisfiability of inputted set of sentences\n"
          "3)Contradiction of inputted set of sentences\n"
          "4)Tautology of a sentence\n"
          "5)Quit")
    correct = False
    while not correct:
        inp = input()
        if inp=="1":
            one()
            correct = True
        elif inp=="2":
            two()
            correct = True
        elif inp=="3":
            three()
            correct = True
        elif inp=="4":
            four()
            correct = True
        elif inp=="5":
            print("bye")
            correct = True
            fin = True
        else:
            print("\nIncorrect input, try again")
