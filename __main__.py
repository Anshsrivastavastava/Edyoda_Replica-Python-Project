from Admin_panel import *

x = Trainer()
# Enter Admin Login ID Admin & Password admin@123

while True:
    print("------------------------------------------------>>>>>Welcome to Edyoda Replica<<<<<<------------------------------------------------\n")
    print("+="*35)
    print("Press 1 for login as Admin")
    print("Press 2 for Student Login")
    print("Press 3 for Trainer Login")
    print("Press 4 for Exit ")
    print("+="*35)
    choise = input("Select Your Choise :")
    if choise =="1":
        # while True:
            if x.admin_login()==True:
                print("================================================")
                print("1.  For Add Modules")
                print("2.  For Add Trainer ")
                print("3.  For Add Student")
                print("4.  For Add Batch")
                print("5.  For Get Student Details")
                print("6.  For Get Trainers Details")
                print("7.  For Get Batch Details")
                print("8.  For Remove Modules ")
                print("9.  For Exit")
                print("================================================")
                seltion = input("Press a Key :")
                if seltion =="1":
                    print(x.Add_modules())

                if seltion =="2":
                    print(x.Add_trainers())
                
                if seltion =="3":
                    print(x.add_student())
                
                if seltion =="4":
                    x.add_batch()
                
                if seltion =="5":
                    print(x.get_student_details())
                    break

                if seltion =="6":
                    print(x.get_trainer_details())
                
                if seltion =="7":
                    print(x.get_batch_details())
                
                if seltion =="8":
                    print(x.remove_module())

                if seltion =="9":
                    break   
            
            else :
                print("Invalid Login Please Login Again \n")

    if choise =="2":
        while True:
            print("*"*55)
            print("Press 1 for View Profile ")
            print("Press 2 for Update Profile")
            print("Press 3 for exit ")
            print("*"*55)
            student_selection = input("Enter A Button :")
            if student_selection =="1":
                print(x.view_Profile())
            
            if student_selection =="2":
                print(x.Update_Profile())
            
            if student_selection =="3":
                print("Thanks For Visiting Student Profile ")
                break

    if choise =="3" :
        while True:
            print("*"*55)
            print("Press 1 for View Profile ")
            print("Press 2 for Update Profile")
            print("Press 3 for exit ")
            print("*"*55)
            trainer_selection = input("Enter A Button :")
            if trainer_selection =="1":
                print(x.View_Trainer_Profile())
            
            if trainer_selection =="2":
                print(x.Update_Trainer_Profile())
            
            if trainer_selection =="3":
                print("Thanks For Visiting Trainer Profile ")
                break

    if choise =="4":
        print("      Thanks For Visiting             ")
        break

