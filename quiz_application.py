def menu_index():
 menu=["="*15,"1) Start Quiz\n","2) Help\n","3) Exit\n","="*15]
 for i in menu:
   print(i)
qus1={"q":"\nwhat is python?","ope":"\n1) Programming language\n2) Database\n3) Operating system\n4) Web broswer","ans":1,"crt_ans":"1) programming language"}
qus2={"q":"\nWhich functoin is used to display output?","ope":"\n1) read()\n2) print()\n3) input()\n4) display","ans":2,"crt_ans":"2) print()"}
qus3={"q":"\nwhich function is used to get input from user?","ope":"\n1) read()\n2) print()\n3) input()\n4) scan()","ans":3,"crt_ans":"3) input()"}
qus4={"q":"\nWhich keyword is used to define a function in python ?","ope":"\n1) function\n2) def\n3) define\n4) fun","ans":2,"crt_ans":"2) def"}                       
qus5={"q":"\nWhich symbol is used for comments in python ?","ope":"\n1) //\n2) #\n3) *\n4) -","ans":2,"crt_ans":"2) #"}
qus6={"q":"\nWhich datatype stores True or Fals value ?","ope":"\n1) int\n2) str\n3) bool\n4) float","ans":3,"crt_ans":"3) bool"}
qus7={"q":"\nWhich loop is mainly used to iterate over a sequence ?","ope":"\n1) while\n2) for\n3) switch\n4) do-while","ans":2,"crt_ans":"2) for"}
qus8={"q":"\nWhich data structure stores key-value pairs ?","ope":"\n1) list\n2) tuple\n3) dictonary\n4) set","ans":3,"crt_ans":"3) dictonary"}
qus9={"q":"\nWhich operator is used to check equality ?","ope":"\n1) =\n2) ==\n3) !=\n4) >=","ans":2,"crt_ans":"2) =="}
qus10={"q":"\nWhich keyword is used to exit the loop immideatly ?","ope":"\n1) continue\n2) pass\n3) break\n4) exit","ans":3,"crt_ans":"3) break"}
questions=[qus1,qus2,qus3,qus4,qus5,qus6,qus7,qus8,qus9,qus10]
score=0
def ask_qus():
    for i in range(0,len(questions)):
     dict_qus=questions[i]
     print(dict_qus["q"])
     print(dict_qus["ope"])
     user_ans=int(input("\nEnter your option:"))
     
     if dict_qus["ans"]==user_ans:
         print("\nYour answer is correct!!!")
        
         global score
         score=score+1
         print("\n******************","\nYour current score is :",score,"\n*******************")
         print("\n _______________Question end ________________")
     elif(user_ans not in range(1,5)):
         print("\nINVALID answer , Please select your option !!")
         ask_qus()
     else:
          print("\nYour answer is wrong!!")
          print("\n the correct answer is :",dict_qus["crt_ans"])
          print("\nYour current score is :",score)
          print("\n _______________Question end ________________")
if score>=8:
    performance="EXCELLENT !!"
    
elif score>=6 and score<=8:
    performance="GREAT !!"
elif score>=4 and score<=6:
    performance="GOOD"
elif score>=2 and score<=4:
    performance="GOOD TRY,NEED IMPROVEMENT !!"
elif score<2:
    performance="BAD !, TRY AGAIN !"
else:
    print("invalid score count")
    
             
    
def help():
    print("""It is a quiz based on python. Each question has one score\n * If you answered one question the score will be added !\n * I You answerd wrong the score will be not addedd\n * Good Luck !! """)
    

running=True
while running:
    menu_index()
    player_ope=int(input("Enter your option:"))
    if player_ope==1:
        ask_qus()
        print(" *********************")
        print("\nYour total score=",score)
        print("\nYour performance :",performance)
        print("\nYour percentage :",score*10,"%")
        print(" *********************") 
    elif player_ope==2:
        help()
    elif player_ope==3:
        print("exit")
        running=False
    else:
        print("invalid option")
    

