#create dialogbox get input name
import tkinter as tk
from tkinter import simpledialog
ROOT=tk.Tk()
ROOT.withdraw()
name=simpledialog.askstring(title="Name",prompt="Enter Your Name")
#loop for play again
play_again="yes"
while play_again=="yes":
    #variables
    name=""
    num=0
    my_list=0
    attempt_no=0
    count=0
    List_length1=0
    List_length2=0
    point=""
    IS_have=False
    marks=0   
    #output(user  interface)
    print()
    print("_________________________________________________________________""Hi",name,"Welcome to GameInt""________________________________________________________________")
    print()
    print("Number to Guess - XXXX","Color Mapping:".rjust(240))
    print("1-White 2-Blue 3-Red".rjust(130))
    print("4-Yellow 5-Green 6-Purple".rjust(135))
    print("If you want to stop the game, input four 0's")
    print()
    print("Attempt No;","Guess".center(80),"Result".rjust(7))

    #create list
    mark_list=[]
    # import random number and create list
    import random
    number_list=[1,2,3,4,5,6]
    Computer_list=[]
    Computer_list=(random.sample(number_list,4))
    
    #create list
    my_list=[]
    stop_list=[0,0,0,0]
    #loop for 8 chances
    while attempt_no<=8:
        #create dialogbox for input4 numbers
        import tkinter as tk
        from tkinter import simpledialog
        User_input=tk.Tk()
        User_input.withdraw()
        for i in range (4):
            num=simpledialog.askinteger(title="Input number",prompt="Enter number" +str(i+1))
            my_list.append(num)#4 numbers append my list
        #It checks if the input number is less than 6 and checks if it is an integer
        ints= True
        for k in my_list :
            try:
                a = int(k)
                if a>6:
                    print("Please note that the number you have entered is incorrect and enter a number from 1-6")
                    break
            except ValueError:
               print("err")
               break
        #geting the length of list   
        List_length1=int(len(Computer_list))
        List_length2=int(len(my_list))
       #if user enter 4 zero this game will be end
        if my_list == stop_list:
            print ("End game")
            break
        #Check whether the my_list and the stop_list are the same, and if they are the same, the game ends 
        if my_list==Computer_list:
            
            mark_list=[1,1,1,1]
            marks=(100-(12.5*attempt_no))
            attempt_no=attempt_no+1
            my=''.join(str(e)for e in my_list)
            Mark=''.join(str(m)for m in mark_list)
            print(attempt_no,my.center(100) ,Mark.rjust(5))
            print("Congratulations!!!!   You have won the game...:")
            break
        else:
            #Checking whether the my_list and the computer_list match and giving the relevant output
            count=0
            mark_list=[]
            while count<=(List_length1-1):
                for i in range(0,List_length2):
                    if Computer_list[count]==my_list[i]:
                        IS_have=True
                        if count == i:
                            point="1"
                            
                            break
                        else:
                            point="0"
                            break
                if IS_have==False:
                    point="*"
                else:
                    IS_have=False

                        
                
                mark_list.append(point)
                count=count+1
            
        attempt_no=attempt_no+1
        my=''.join(str(e)for e in my_list)
        Mark=''.join(str(m)for m in mark_list)
        print(attempt_no,my.center(100) ,Mark.rjust(5))
        print("_"*153)
        my_list=[ ]
    #outputing the scores
    print("You have scored",marks,"points.")
    play_again="no"    
    import tkinter as tk
    from tkinter import messagebox as msg
    Play_A=tk.Tk()
    Play_A.withdraw()
    play_again=msg.askquestion('Play again',"Do you want to play again")
