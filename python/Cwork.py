restart = 0
change_info = ""
list_marks = []
list_names = []
account = ""

def PASS():
    id_dessalli = "Jimdjio Frank"
    password_dessalli = "king"
    password_public = "every"

def ENTERMARK():
    mark = 0
    p = 0
    while (mark != -1):
        mark = int(input("Enter student's mark :"))
        if (mark <0 or mark >20) and mark != -1:
            print("Enter a correct mark")
        elif mark == -1:
            break
        else:
            list_marks.insert(p, mark)
            name = str(input("Enter student's name :"))
            list_names.insert(p, name)
            p = p+ 1

full_name = str(input("Enter your full name :"))
print("Welcome " , full_name)

while restart != -1:
    print("SELECT THE NUMBER OF THE OPERATION YOU WANT TO PERFORM")
    print("1-ENTER STUDENT MARKS")
    print("2-UPDATE ACCOUNT INFO")
    print("3-VIEW ACCOUNT INFO")
    print("4-VIEW STUDENT MARKS ANALYSIS")
    n = int(input())

    if n == 1:
        ENTERMARK()
        i = 0
        print ("Table of student marks")
        print ("=======================")

        for i in range(len(list_marks)):
            print (list_names[i], " ", list_marks[i])
            i = i + 1

    elif n == 2:
        user_name = str(input("Enter your user name :"))
        nick_name = str(input("Enter your nick name :"))
        nationality = str(input("Enter your nationality :"))
        print("Do want to change or rectify any error (yes/no) :")
        change_info = str(input())

        if change_info == "yes":
            #full_name == str(input())
            user_name = str(input("Renter your user name :"))
            nick_name = str(input("Renter your nick name :"))
            nationality = str(input("Renter your nationality :"))

    elif n == 3:
        print(full_name)
        print(user_name)
        print(nick_name)
        print(nationality)

    elif n == 4:
        a = 0
        #e = 0
        print ("Table of analysis")
        print ("=================")
        while a <len(list_marks):
            print(list_names[a] , "*"*list_marks[a])
            a = a + 1
            #e  = e + 1

    else:
        print ("enter a correct correct value")

    restart = int(input("press -1 to save and exit \npress  1 go to continue \n :)"))

print ("your work is save")