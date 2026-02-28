

email = input(" Enter you email abc@xyz.com  format >-< ")
k = 0
j = 0
d = 0

if len(email) >= 10: 
    if email[0].isalpha():
        if("@" in email) and (email.count("@")==1):
            if (email[-4] ==".") ^ (email[-3] == "."):
                    for i in email:
                        if i== i.isspace():
                            k = 1
                        elif i.isalpha():
                            if i == i.upper():
                                # check for the upper case
                                j - 1
                                # now check the digits 
                        elif i.isdigit():
                            continue
                        elif i =="_" or i =="." or i == "@":
                            continue
                        else:
                            d = 1

                    if k == 1 or j == 1 or d == 1:
                         print("ERROR:(  type the correct py")
            
            else: (" wrong position of .")
        else: # error 3
            print("error don't use more than 1 @ \n ")
    else: #error 2
        print("wrong email :( make all the alphabet lowercase ")
else:#error 1
    print("wrong email :( \n please full fill the letters requirementa (>-<) ")
print("you typed correct form of email :)")