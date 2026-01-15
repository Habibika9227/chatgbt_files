
def main():

    user_name=input("Enter Username: ")
    if is_valid(user_name):
        print("valid")
    else:
        print("Invalid")
def is_valid(username):
    #. Step1: get length and determines it's validation.
    if len(username)<4 or len(username)>10:
        return False
    #.Step2:first character through indexing
    if not(username[0].isalpha()):
        return False
    #.Step3: check whether the username is letters and numbers only.

    #.Step4:create a flag to track changes in our loop
    tracker=False
    for char in username:
        if char.isdigit():
            if not tracker:

                if char=="0":
                    return False
                tracker=True
        else:
            if tracker: #if tracker has seen letter, we set the tracker to false 
                return False
    
    return True



        
        


main()