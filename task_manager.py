# Capstone Project IV
from datetime import date # imports module that provides current date

'''
tasks_file = open ("tasks.txt", "r") # Opens file for reading only
for line in tasks_file:
    text = line
    print (text)

tasks_file.close() # Close file

user_file = open ("user.txt", "r+") # Opens file for reading and writing
user_file.write("admin, adm1n\nuserA, user1\nuserB, user2\nuserC, user3")

user_file.close()

in_user_file = open ("user.txt", "r")# Opens file for reading only
for data in in_user_file:
    info = data
    print(info)
    
in_user_file.close() # Close file
'''

def login_user ():
    
    login = False # Sets Boolean operator as false

    print ("")
    global username # Allows the variable in this function to be used in another function
    username = str(input("Enter username: \n"))
    password = str(input("Enter password: \n"))


    in_file = open ("user.txt","r+") # Open file
    for line in in_file:

        split_line = line.split(",")
        user_check = split_line[0].strip()
        pass_check = split_line[1].strip()
        if username == user_check and password == pass_check:
            login = True
            #return login #19/05
            menu()
        else:
            print("Invalid credentials")
            login_user ()

    in_file.close()

def menu():

    print ("r - register user")
    print ("a - add task")
    print ("va - view all tasks")
    print ("vm - view my tasks")
    print ("gr - generate report")
    print ("ds - display statistics")
    print ("e - exit")

    run_menu()


#def menu(username):#19/05

def run_menu():
    
    options = 0

    while True:
   
        options = input ("Please select one of the options: ")
        if options == "r":
            reg_user()

        elif options == "a":
            add_task()

        elif options == "va":
            view_all ()

        elif options == "vm":
            view_mine ()

        elif options == "gr":
            generate_reports ()

        elif options == "ds":
            display_statistics()


        elif options == "e":
           exit() # Exits application
        else:
            menu() # Displays menu again if anything else is entered

    print ("Goodbye")
        


def reg_user(): # Defines reg_user as a function

    if username  == "admin": # Allows admin to only use this function
        
    
        new_username = input("Enter new username: \n")
        check_username = open ("user.txt","r+")
        for text in check_username:
            
            if text in new_username  == text.split(",")[0]: # Checks for duplication
                print ("Username alredy exists!!!")
                new_username = input("Enter new username: \n")
                
        check_username.close()
            
        new_password = input ("Enter new password: \n")
        confirm_password = input ("Confirm new password: \n")

        if new_password == confirm_password:
            text_register = (new_username + "," +" " +new_password)
            print (text_register)
            text_register_user_file = open ("user.txt", "r+") # Opens file for reading and writing
            text_register_user_file.write(text_register)

            text_register_user_file.close()

        stats_option = input ("Would you like to display statistics? (yes/no)")

        if stats_option == "yes":
        
            stats_display_task = open("tasks.txt","r")
            num_of_tasks =0
            for stats in stats_option:
                num_of_tasks += 1
                text_task = ("Number of Tasks: " + str(num_of_tasks))
                print (text_task)
            
            stats_display_user = open ("user.txt","r")
            num_of_user =0
            for statsuser in stats_display_user:
                num_of_user +=1
                text_user = ("Number of Users: " + str(num_of_user))
                print (text_user)
            
            
                
                
        if stats_option == "No":
            exit() # Exits application
    else:
        print("Only admin may register new user")


    
    
def add_task(): # Defines add_task as a function

    assign = input ("Enter the username of the person that the task is assigned to: \n")
    title = input ("What is the title of the task?\n")
    description = input ("Provide a description of the task: \n")
    due_date = input ("When is the task due?[dd/mm/yyyy]")
    today_date = date.today()
    current_date = today_date.strftime("%d/%m/%Y")
    assign_text = (assign + ", " + title + ", " + description + ", " + due_date + ", " + current_date + ", No")
    print (assign_text)

    assign_file = open ("tasks.txt", "w")
    assign_file.write(assign_text)

    assign_file.close()    

def view_all ():  #Defines view_all as a function


    view_all = open ("tasks.txt", "r")
    for task in view_all:
        task = task.split(",")
        assign_task = task[0]
        title_task = task[1]
        description_task = task[2]
        due_date_task = task[3]
        current_date_task = task[4]
        no = task[5]

        task_text = ("Assigned to:" + assign_task + "\n" + "Task:  " + title_task + "\n" + "Description: "+ description_task + "\n" + "Due date:" + due_date_task + "\n" + "Date Assigned: "+  current_date_task + "\nCompleted: "+ no)
        print(task_text)






def view_mine (): #Defines view_mine as a function
    
    task_dict ={}
    counterr = 0
    in_file = open ("tasks.txt","r+")
    for line in in_file:
        counterr += 1
        text =line.split(",")
        task_name = text[1]
        key, values =task_name, counterr
        task_dict[key] = values
    print (task_dict)
    in_file.close()
    
    counter = 0
    view_my = open ("tasks.txt", "r+")
    for veiw in view_my:
        
            
        veiw = veiw.split(",")
        #login_user ()#19/05
        if veiw[0] == username:
            counter += 1
            
            assign_veiw = veiw[0]
            title_veiw = veiw[1]
            description_veiw = veiw[2]
            due_date_veiw = veiw[3]
            current_date_veiw = veiw[4]
            no = veiw[5]

            veiw_text = ("Assigned to:" + assign_veiw + "\n" + "Task:  " + title_veiw + "\n" + "Description: "+ description_veiw + "\n" + "Due date:" + due_date_veiw + "\n" + "Date Assigned: "+  current_date_veiw + "\nCompleted: "+ no)
            print(veiw_text)
    

    if counter == 0:
        print ("No tasks assigned yet")
        global amend

        amend = ""
        
    if counter != 0:
        amend = input("Please select a task to amend \nPress -1 to return exit")
        
        
        if amend == "-1":
        
            exit()
        

        if amend != "":
            choice = input("Please make a selection: \n1 Mark task complete \n2 Mark task incomplte \n3 Edit username\n4 Edit due date")
        
    
        change_view_my = open ("tasks.txt", "r+")
        #complete = input("Is the task complete?(Yes/No)")
        if choice == "1":
        
            change_view_my_text = (assign_veiw + "," + title_veiw + "," + description_veiw + ","  + due_date_veiw + "," + current_date_veiw + ",Yes")
        elif choice == "2":
            change_view_my_text = (assign_veiw + "," + title_veiw + "," + description_veiw + "," + due_date_veiw + "," + current_date_veiw + ","+ no)

        elif choice == "3":
            new_username = input("Enter edited username")
            change_view_my_text = (new_username + "," + title_veiw + "," + description_veiw + "," + due_date_veiw + "," +  current_date_veiw + ","+ no)

        elif choice == "4":
            new_due_date = input("Enter new due date")
            change_view_my_text = (assign_veiw + "," + title_veiw + "," +description_veiw + "," + new_due_date + "," + current_date_veiw + ","+ no)

        change_view_my.write(change_view_my_text)
        change_view_my.close

def generate_reports (): #Defines generate_reports as a function
    

    wanted_yes = "Yes"
    count_yes = 0
    wanted_no = "No"
    count_no = 0
        
    view_my =open ("tasks.txt","r+")
    task_counter = 0
    for veiw in view_my:
        
        task_counter += 1
    

    
    

        
        assign_veiw = veiw[0]
        title_veiw = veiw[1]
        description_veiw = veiw[2]
        due_date_veiw = veiw[3]
        current_date_veiw = veiw[4]
        no = veiw[5]
        
    generate_reports_task = open("task_overview.txt","w")
    
        
    num_task = task_counter
    print (num_task)
        
    for  veiw in view_my:# Search for the word yes, for each word yes, counter increases by one
        
        if wanted_yes in veiw :
                count_yes +=1
                
    for veiw in view_my: # Search for the word no, for each word no, counter increases by one

        if wanted_no in veiw:
            count_no += 1
                
    complete = count_yes   # Define variable complete to be count_yes
   
    incomplete = count_no  # Define variable incomplete to be count_no
    

    overdue_count = 0
        
    for lines in view_my:
        lines =lines.split(",")
        due_date = lines[4]

        if due_date < date.today(): # Checks if today has supast the due date
            overdue_count += 1

    #overdue = overdue_count

    percentage_incomplete = (count_no /num_task) *100
    print (percentage_incomplete)

    #percentage_overdue = (overdue /num_task) *100
    #print (percentage_overdue)

    text = ("The total number of tasks: " + str(num_task) +"\n" + "The total number of completed tasks: " + str(complete) + "\n"+ "The total number of uncompleted tasks: " +str(incomplete)+"\n"  + "The percentage of tasks that are incomplete: "+str(percentage_incomplete) +"\n" )


    generate_reports_task.write(str(text))

    #print (print_text)    
    #percentage-overdue = 
    #generate_reports_task.write(num_task)

    

    in_user_file = open ("user.txt", "r+")# Opens file for reading and writing
    counter = 0
    for line in in_user_file:
            counter += 1
    print(counter)
    
    in_user_file.close() # Close file
        

    generate_user_task = open ("user_overview.txt","w") # Opens file for writing


    #login_user ()#19/05
    total_users = num_task
    total_task = counter 
    login_user () # Since a variable from another function is used, that function  is typed before its variable can be used
    if veiw[0] == username:
            counter += 1

            for  veiw in view_my:#################################################################################
        
                if wanted_yes in veiw :
                
                    count_yes +=1
                
            for veiw in view_my:

                 if wanted_no in veiw:
                    
                    count_no += 1
            
            assign_veiw = veiw[0]
            title_veiw = veiw[1]
            description_veiw = veiw[2]
            due_date_veiw = veiw[3]
            current_date_veiw = veiw[4]
            no = veiw[5]

    
    task_assigned = counter
    percentage_assigned = (counter /num_task) * 100
    perc_complete = count_yes
    perc_incomplete = count_no
    #overdue = overdue_count

    

    genrate_text = ("Total users: "+str(total_users) +"\n" +"Total tasks: "+str(total_task)+"Number of tasks assigned to you" + str(task_assigned)+"\n" + "Percentage of the total tasks: "+str(percentage_assigned)+"\n"+"Percentage complete: " +str(perc_complete)+"\n" +"Percentage incomplete: " + str(perc_incomplete) )


    generate_user_task.write(str(genrate_text))

    
    
    view_my.close()
    in_user_file.close()

    generate_user_task.close()



def display_statistics(): #Defines display_statistics as a function
    in_task_overview = open("task_overview.txt","r")
    for line in in_task_overview:
        print (line) #Prints text in task_overview.txt
    
    in_task_overview.close # Closes in_task_overview
    
    int_user_overveiw = open("user_overview.txt","r")
    for line in int_user_overveiw:
        print (line) #Prints text in user_overview.txt
    int_user_overveiw.close() # Closes int_user_overveiw





login_user ()# calls the function

     





    
     
            
