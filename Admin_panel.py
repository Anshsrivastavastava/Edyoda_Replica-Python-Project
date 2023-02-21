import random
import json

class Admin:
    topic = []
    def __init__(self):
        self.Modules_details = {}
        self.Trainer_Details = {}
        self.students = {}
        self.main_details ={}
        self.main_trainer ={}
        self.Batch = {}

  

    def Add_modules(self):
        key = random.randint(100,999)
        module_name = input("Enter Module Name :")
        dueration = input("Enter the Dueration of Module :")
        topic_nos = int(input("Enter How Many Topics You Wants to Add :"))
        for i in range(1,topic_nos+1):
            topic_name = input("Enter Your Topic Name :")
            Admin.topic.append(topic_name)
        d = {"Module Name":module_name,"Dueration":dueration,"Topic Name":Admin.topic}
        self.Modules_details[key]=d
        print()
        print(f"Your {i} Modules Got Added")
        key = random.randint(100,999)
        with open("Modules_Details.json",'w') as f:
            json.dump(self.Modules_details,f,indent= 4)
        return "Modules Got Added Sucessfully"
    
    def Add_trainers(self):
        main_key = random.randint(0,123)
        print("---------->>>>For Add Trainer Enter Details Mentions Below<<<<-----------\n")        
        nos = input("Enter How Many Trainer You Want to Edit :")
        for i in range(int(nos)):
            Id = input("Enter Trainer ID :")
            name = input("Enter Trainer Name :")
            age = input("Enter Trainer Age :")
            Gender = input("Enter Trainer Gender :")
            phone_no = input("Enter Trainer Phone Number :")
            email = input("Enter your Email Address :")
            Qulification = input("Enter Your Qulification :")
            exprience = input("Enter Your Expricnce :")
            password = input("Enter Your Password Here :")
            print()
            d = {"Name":name,"Age":age,"Gender":Gender,
                "Phone Number":phone_no,"Email":email,"Qulification":Qulification,
                "Exprience":exprience,"Password":password}
            self.Trainer_Details[Id] = d
            self.main_trainer[main_key] = self.Trainer_Details
        with open("Trainer_Details.json",'w') as f:
            json.dump(self.main_trainer,f,indent= 4)
        return "Your Trainer Key Got Added"


    def add_student(self):
        key = random.randint(100,999)
        main_key = random.randint(1,99)
        nos = input("Enter How Many Student You Want to Add :")
        for i in range(1,int(nos)+1):
            name = input("Enter Student Name :")
            age = input("Enter Student Age :")
            Gender = input("Enter Student Gender :")
            phone_no = input("Enter Student Phone Number :")
            email = input("Enter Student Email Address :")
            Qulification = input("Enter Student Qulification :")
            exprience = input("Enter Your Expricnce :")
            password = input("Enter Your Password Here :")
            print()
            d = {"Name":name,"Age":age,"Gender":Gender,
            "Phone Number":phone_no,"Email":email,"Qulification":Qulification,
            "Exprience":exprience,"Password":password}
            self.students[key] = d
            self.main_details[main_key] = self.students
        with open("Student_Details.json","w") as f:
            json.dump(self.main_details,f,indent=4)
        return "Details Got Created"
    
    def add_batch(self):
        Batch_name = "DS"+str(random.randint(10112,99999))+"A"
        stud_key = input("Enter Student ID :")
        train_Id = input("Enter Trainer ID :")
        modules_id = input("Enter Modules ID :")
        d= {"Batch Name":Batch_name,"Student Key":stud_key,"Trainer ID ":train_Id,"Modules":modules_id}
        self.Batch[random.randint(0,999)] = d
        with open("Batch_details.json",'w') as f:
            json.dump(self.Batch , f ,indent= 4)
        return "Your Batch Got Added Sucessfully"
    
    def Get_student_Details(self):
        with open("Student_Details.json","r") as f:
            self.temp = json.load(f)
        for i in self.temp.values():
            for j ,k in i.items():
                print(f"------------>>>>Details for ID: {j} Student <<<------------\n")
                for o , p in k.items():
                    print(f"{o}: {p}")
                print()
            return ""
    
    def Get_traniner_Details(self):
        with open("Trainer_Details.json","r") as f:
            self.temp = json.load(f)
        for i in self.temp.values():
            for j ,k in i.items():
                print(f"------------>>>>Details for ID: {j} Trainers <<<------------\n")
                for o , p in k.items():
                    print(f"{o}: {p}")
                print()
            return ""
    
    def get_batch_details(self):
        with open("Modules_Details.json","r") as f:
            temp = json.load(f)
        for i in temp.values():
            for j,p in i.items():
                print(f"{j}:{p}")
            print()
        return ""
    
    def remove_module(self):
        with open("Modules_Details.json",'r') as f:
           temp = json.load(f)
        key = input("Enter Your Modules Key Which You Want to Remove :")   
        if key in temp:
            del temp[key]
            with open("Modules_Details.json",'w') as f:
                json.dump(temp,f,indent = 4)
            return "Your Module Got Delete"
        else:
            return "Enter A Valid Module Key"

    def admin_login(self):
        user = input("Enter Your User Name :")
        passw = input("Enter Your Password :")
        if user =="Admin" and passw == "admin@123":
            return True
        else:
            return False    
              
        

class student(Admin):
    def __init__(self):
        super().__init__()
    
    def view_Profile(self):
        with open("Student_Details.json","r") as f:
            temp = json.load(f)
        for i in temp.values():
            print()
            print(f"Student ID We Are Having {i.keys()}")
            while True:
                stude_ID = input("Enter Your ID Here :")
                if stude_ID in i:
                    passsword = input("Enter Your Password Here :")    
                    if passsword == i[stude_ID]["Password"]:
                        print()                
                        print(f"---------------------->>>>>Details for Student ID {stude_ID}<<<<<<<----------------------\n")
                        for j ,r in i[stude_ID].items():
                            print(f"{j}   :   {r}")
                        return ""
                    else:
                        print("Enter A Valid Password")
                else:
                    print("Enter A Valid ID ")

    def Update_Profile(self):
        with open("Student_Details.json","r") as f:
            temp = json.load(f)
        for i in temp.values():
            print()
            print(f"Student ID We Are Having {i.keys()}")
            stude_ID = input("Enter Your ID Here :")
            if stude_ID in i:
                passsword = input("Enter Your Password Here :")    
                if passsword == i[stude_ID]["Password"]:
                    print(f"---------------------->>>>>Details for Student ID {stude_ID}<<<<<<<----------------------\n")
                    for j ,r in i[stude_ID].items():
                        print(f"{j}   :   {r}")
                    print()
                    filed = input("Enter Field Which Your Want to Update :")
                    updated_value = input(f"Enter Your Updated Value for {filed} :")
                    i[stude_ID][filed] = updated_value
                    with open("Student_Details.json","w") as f:
                        json.dump(temp,f,indent= 4)
                    return "Your Profile Got Update"
                else:
                    print("Enter A Valid Password")
            else:
                print("Enter A Valid ID ")

class Trainer(student):
    def __init__(self):
        super().__init__()
    
    def View_Trainer_Profile(self):
        with open("Trainer_Details.json","r") as f:
                temp = json.load(f)
        for i in temp.values():
            print()
            print(f"Trainers ID We Are Having {i.keys()}")
            stude_ID = input("Enter Your ID Here :")
            if stude_ID in i:
                passsword = input("Enter Your Password Here :")    
                if passsword == i[stude_ID]["Password"]:
                    print()                
                    print(f"---------------------->>>>>Details for Trainer ID {stude_ID}<<<<<<<----------------------\n")
                    for j ,r in i[stude_ID].items():
                        print(f"{j}   :   {r}")
                    return ""
                else:
                    print("Enter A Valid Password")
            else:
                return "Please Enter Valid Trainer ID "

    def Update_Trainer_Profile(self):
        with open("Trainer_Details.json","r") as f:
            temp = json.load(f)
        for i in temp.values():
            print()
            print(f"Trainers ID We Are Having {i.keys()}")
            stude_ID = input("Enter Your ID Here :")
            if stude_ID in i:
                passsword = input("Enter Your Password Here :")    
                if passsword == i[stude_ID]["Password"]:
                    print(f"---------------------->>>>>Details for Trainer ID {stude_ID}<<<<<<<----------------------\n")
                    for j ,r in i[stude_ID].items():
                        print(f"{j}   :   {r}")
                    print()
                    filed = input("Enter Field Which Your Want to Update :")
                    updated_value = input(f"Enter Your Updated Value for {filed} :")
                    i[stude_ID][filed] = updated_value
                    with open("Trainer_Details.json","w") as f:
                        json.dump(temp,f,indent= 4)
                    return "Your Profile Got Update"
                else:
                    return "Please Enter A Valid Trainer ID"
            else:
                return "Please Enter A Valid Trainer ID "
                



            


    
       
           


        
