#email validation using string function
k ,j, d = 0 ,0, 0# flags
email = input("Enter your email:-")
if len(email) >= 6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@") == 1) :
            if (email[-3] == '.' )^(email[-4] == '.'):
                for i in email:
                    if i == i.isspace():
                        k =  1
                    elif i.isalpha():
                        if i == i.upper():
                            j = 1
                    elif i.isdigit():
                        continue
                    elif i == "_" or i =="." or i =="@":
                        continue
                    else:
                        d = 1
                if k  == 1 or j == 1 or d == 1:
                    print("wrong email 5 check the spaces ,letters")
                else :
                    print("right email eneter :)")
            else:print(" wrong email 4 check the no of '.")
        else:print("wrong email 3 check the no. of the @")
    else:print("wrong email 2 check the first letter of the email ")
else:print("wrong email 1 check the starting letter\n")