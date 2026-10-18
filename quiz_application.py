def menu_index():
    menu=["="*15,"1) Start Quiz","2) Help","3) Exit","="*15]
    for i in menu:
        print(i)

qus1={"q":"\nWhat is python?","ope":"\n1) Programming language\n2) Database\n3) Operating system\n4) Web browser","ans":1,"crt_ans":"1) Programming language","explanation":"Python is a programming language used to write programs."}
qus2={"q":"\nWhich function is used to display output?","ope":"\n1) read()\n2) print()\n3) input()\n4) display","ans":2,"crt_ans":"2) print()","explanation":"print() shows output on the screen."}
qus3={"q":"\nWhich function is used to get input from user?","ope":"\n1) read()\n2) print()\n3) input()\n4) scan()","ans":3,"crt_ans":"3) input()","explanation":"input() waits for the user to type something and returns it."}
qus4={"q":"\nWhich keyword is used to define a function in python ?","ope":"\n1) function\n2) def\n3) define\n4) fun","ans":2,"crt_ans":"2) def","explanation":"def is the keyword that starts a function definition."}
qus5={"q":"\nWhich symbol is used for comments in python ?","ope":"\n1) //\n2) #\n3) *\n4) -","ans":2,"crt_ans":"2) #","explanation":"Python ignores everything after # on that line."}
qus6={"q":"\nWhich datatype stores True or False value ?","ope":"\n1) int\n2) str\n3) bool\n4) float","ans":3,"crt_ans":"3) bool","explanation":"bool can only hold True or False."}
qus7={"q":"\nWhich loop is mainly used to iterate over a sequence ?","ope":"\n1) while\n2) for\n3) switch\n4) do-while","ans":2,"crt_ans":"2) for","explanation":"A for loop goes through each item of a sequence one by one."}
qus8={"q":"\nWhich data structure stores key-value pairs ?","ope":"\n1) list\n2) tuple\n3) dictionary\n4) set","ans":3,"crt_ans":"3) dictionary","explanation":"A dictionary stores data as key : value pairs."}
qus9={"q":"\nWhich operator is used to check equality ?","ope":"\n1) =\n2) ==\n3) !=\n4) >=","ans":2,"crt_ans":"2) ==","explanation":"== compares two values, while = assigns a value."}
qus10={"q":"\nWhich keyword is used to exit the loop immediately ?","ope":"\n1) continue\n2) pass\n3) break\n4) exit","ans":3,"crt_ans":"3) break","explanation":"break stops the loop right away."}
questions=[qus1,qus2,qus3,qus4,qus5,qus6,qus7,qus8,qus9,qus10]
score=0
performance=""
def ask_qus():
    global score
    score=0
    for i in range(0,len(questions)):
        dict_qus=questions[i]
        print(dict_qus["q"])
        print(dict_qus["ope"])
        while True:
            try:
                user_ans=int(input("\nEnter your option:"))
            except ValueError:
                print("\nINVALID answer , Please enter a number from 1 to 4 !!")
                continue
            if user_ans in range(1,5):
                break
            print("\nINVALID answer , Please select your option from 1 to 4 !!")

        if dict_qus["ans"]==user_ans:
            print("\nYour answer is correct!!!")
            score=score+1
            print("\n******************","\nYour current score is :",score,"\n*******************")
            print("\n _______________Question end ________________")
        else:
            print("\nYour answer is wrong!!")
            print("\nThe correct answer is :",dict_qus["crt_ans"])
            print("Explanation :",dict_qus["explanation"])
            print("\nYour current score is :",score)
            print("\n _______________Question end ________________")

def find_performance():
    global performance
    if score>=8 and score<=10:
        performance="EXCELLENT !!"
    elif score>=6 and score<=7:
        performance="GREAT !!"
    elif score>=4 and score<=5:
        performance="GOOD"
    elif score>=2 and score<=3:
        performance="GOOD TRY,NEED IMPROVEMENT !!"
    else:
        performance="BAD !, TRY AGAIN !"

def help():
    print("""It is a quiz based on python. Each question has one score\n * If you answered one question the score will be added !\n * If you answered wrong the score will not be added !\n * Good Luck !! """)


running=True
while running:
    menu_index()
    try:
        player_ope=int(input("Enter your option:"))
    except ValueError:
        print("invalid option , Please enter a number from 1 to 3")
        continue
    if player_ope==1:
        ask_qus()
        find_performance()
        percentage=int(score*100/len(questions))
        print(" *********************")
        print("\nYour total score=",score,"/",len(questions))
        print("\nYour performance :",performance)
        print("\nYour percentage :",percentage,"%")
        print(" *********************")
    elif player_ope==2:
        help()
    elif player_ope==3:
        print("exit")
        running=False
    else:
        print("invalid option , Please select 1, 2 or 3")