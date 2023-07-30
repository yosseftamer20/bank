
def creat():
    x=open("data", "r")
    print("Open an account")
    id=0
    last=x.readlines()
    if last:
        id=int(last[-1][0])
    id+=1
    x.close()
    name=input("name:")
    dob=input("dob:")
    address=input("address:")
    job=input("job:")
    telephone_number=input("telephone_number:")
    balance=0
    x=open("data", "a")
    if name.isalpha() and job.isalpha() and telephone_number.isdigit():
        x.write(f"""{id},{name},{dob},{address},{job},{telephone_number},{balance}\n""")
        x.close()
    else:
        print("Invalid input")
def inquery():
    x = open("data", "r")
    inquery_id=input("inquery_id:")
    if inquery_id.isdigit():
        for i in x.readlines():
            if inquery_id==i[0]:
                print(i)
    else:
        print("Invalid id")
def deposit():
    x = open("data", "r")
    data=x.readlines()
    x.close()

    pass_id = input("pass_id:")
    found=None
    for i,line in enumerate(data):
        if pass_id == line[0]:
            found = True
            added_amount=input("added amount:")
            if added_amount.isdigit():
                added_amount=int(added_amount)
                balance=line.split(",")[-1].strip()
                balance = int(balance) +added_amount
                line=line.split(",")[:-1]
                line.append(str(balance)+"\n")
                line = ",".join(line)
                data[i]=line
            else:
                print("Invalid amount ")
    if found:
        o = open("data", "w")
        o.writelines(data)
    else:
        print("ID not found")
def withdraw():
    x = open("data", "r")
    data = x.readlines()
    x.close()
    pass_id = input("pass_id:")
    found=None
    for i, line in enumerate(data):
        if pass_id == line[0]:
            found=True
            losted_amount = input("added amount:")
            balance = line.split(",")[-1].strip()
            if losted_amount.isdigit():
                losted_amount=int(losted_amount)
                if int(balance) >= losted_amount:
                     balance = int(balance) - losted_amount
                     line = line.split(",")[:-1]
                     line.append(str(balance) + "\n")
                     line = ",".join(line)
                     data[i] = line
                else:
                     print("Insufficient Balance !")
            else:
                print("Invalid")
    if found:
        o = open("data", "w")
        o.writelines(data)
    else:
        print("ID not found")
def transfer():
    x = open("data", "r")
    data = x.readlines()
    x.close()
    pass_id = input("your id:")
    if not  pass_id.isdigit():
        print("Invalid id")
        return
    The_amount_required = input("The_amount_required:")
    pass_id2 = input("beneficiary id:")
    if not pass_id2.isdigit():
        print("Invalid id")
        return
    found=None
    for i, line in enumerate(data):
        if pass_id == line[0]:
            found=True
            balance = line.split(",")[-1].strip()
            if not The_amount_required.isdigit():
                print("Invalid amount")
                return
            The_amount_required=int(The_amount_required)
            if int(balance) >= The_amount_required:
                balance = int(balance) - The_amount_required
                line = line.split(",")[:-1]
                line.append(str(balance) + "\n")
                line = ",".join(line)
                data[i] = line
            else:
                print("Insufficient Balance !")
                return

    if found:
        o = open("data", "w")
        o.writelines(data)
    else:
        print("ID not found")

    for i, line in enumerate(data):
        if pass_id2 == line[0]:
            found=True
            balance = line.split(",")[-1].strip()
            if int(balance) >= The_amount_required:
                balance = int(balance) + The_amount_required
                line = line.split(",")[:-1]
                line.append(str(balance) + "\n")
                line = ",".join(line)
                data[i] = line
            else:
                print("Insufficient Balance !")
    if found:
        o = open("data", "w")
        o.writelines(data)
    else:
        print("ID not found")

while True:
    print("""
      ____                    _         _____                 _                      
     |  _ \                  | |       / ____|               | |                     
     | |_) |   __ _   _ __   | | __   | (___    _   _   ___  | |_    ___   _ __ ___  
     |  _ <   / _` | | '_ \  | |/ /    \___ \  | | | | / __| | __|  / _ \ | '_ ` _ \ 
     | |_) | | (_| | | | | | |   <     ____) | | |_| | \__ \ | |_  |  __/ | | | | | |
     |____/   \__,_| |_| |_| |_|\_\   |_____/   \__, | |___/  \__|  \___| |_| |_| |_|
                                                 __/ |                               
                                                |___/                                
    """)
    print("what do you want ?\n1-create new accaunt.\n2-inquery\n3-deposit\n4-withdraw\n5-transfer")
    choice=input("enter youe choice:")
    if choice.isdigit() :
        choice=int(choice)
        if choice == 1:
            creat()
        elif choice == 2:
            inquery()
        elif choice == 3:
            deposit()
        elif choice == 4:
            withdraw()
        elif choice == 5:
            transfer()
    else:
        print("Invalid Choice")






