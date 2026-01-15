
# def main():
#     user_input=input("Enter Code: ")
#     if is_valid(user_input):
#         print("Valid")
#     else:
#         print("Invalid")

# def is_valid(code):
#     #Step1: check length and should be 8 chars
#     if len(code)!=9:
#         return False
#     #Step2:check the 1st chars t be uppercased letters
#     if not( code[0].isalpha() and code[1].isalpha() and code[7].isalpha() and code[8].isalpha()):
#         return False
#     #step: positions for (-)
   
#     if not (code[2]=="-" and code[6]=="-"):
#         return False
#     #step4:checking the required digits in the middle( not 0 or 999)
#     if not(code[3:6].isdigit()):   
#            return False
#     if code[3:6]=="999" or code[3]=="0":
#         return False
#     #step4: 1st and lst two letters should'nt be the same.
#     if code[0]==code[1] or  code[7]==code[8]: #You cannot compare boolean with another boolean.
#         return False
#     return True
        

# main()

def main():
    user_input = input("Enter Code: ")
    if is_valid(user_input):
        print("Valid")
    else:
        print("Invalid")

def is_valid(code):
    # Step 1: length
    if len(code) != 9:
        return False

    # Step 2: letters
    if not (code[0].isalpha() and code[1].isalpha() and code[7].isalpha() and code[8].isalpha()):
        return False

    # Step 3: hyphens
    if not (code[2] == "-" and code[6] == "-"):
        return False

    # Step 4: digits
    if not code[3:6].isdigit():
        return False

    if code[3:6] == "999" or code[3] == "0":
        return False

    # Step 5: similar letters
    if code[0] == code[1] or code[7] == code[8]:
        return False

    return True

main()






