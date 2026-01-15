# def main():
#     var=input("Input: ")
#     var2=check_length(var)
#     print(var2)


# def check_length(s):
#     var3=len(s)
#     if 2 <= var3 <=6:
#         return True
#     else:
#         return False


# main()
# def main():
#     get_input=input("Input: ")
#     var1=check_first_two_letters(get_input)
#     print(var1)

# def check_first_two_letters(s):
#     if s[0].isalpha() and s[1].isalpha():
#         return True
#     else:
#         return False
# main()
# def main():
 
#  var1=input("Input: ")
#  var2=check_letter_number_order(var1)
#  print(var2)

# def check_letter_number_order(s):
#  memory_flag=False
#  for order in s:
#   if order.isdigit():
#    memory_flag=True

#   elif order.isalpha() and memory_flag:
#    return False
  
#  return True


# main()

# def main():
#     user_input=input("Input: ")
#     buffer_memory=False

#     for check in user_input:
#         if check.isdigit():
#             if not buffer_memory:
#                 if check=="0":
#                     return False
#                 buffer_memory=True
                
    

# main()
# def check_first_number():
#     user_input=input("Input: ")
#     number_started = False

#     for ch in user_input:
#         if ch.isdigit():
#             if not number_started:  # first digit
#                 if ch == "0":
#                     return False  # reject immediately
#                 number_started = True  # valid first number
#             # later digits → no check needed

#     return True  # plate passed first number check
# check_first_number()
# def main():
#     get_input=input("Input: ")
#     if len(get_input)<2 or len(get_input)>6:
#         print("Invalid")
#         return #stops the condition if the rule fails
#     if not(get_input[0].isalpha() and get_input[1].isalpha()):
#         print("Invalid")
#         return
#     get_number_started=False
#     for char in get_input[2:]:
#         if char.isdigit():
#             if not get_number_started:
#                 if char=="0":
#                     print("Invalid")
#                     return False
#                 get_number_started=True
                


#     print("Valid")
    
# main()

def main():
    plate = input("Input: ")

    # Step 1: Check length
    if len(plate) < 2 or len(plate) > 6:
        print("Invalid")
        return  # Stop if length is wrong

    # Step 2: Check first two characters are letters
    if not (plate[0].isalpha() and plate[1].isalpha()):
        print("Invalid")
        return  # Stop if first two chars are not letters

    # Step 3: Check numbers rules
    number_started = False  # Flag to track if we've seen a number yet

    for c in plate[2:]:  # Start checking after the first two letters
        if c.isdigit():
            if not number_started:  # First number we see
                if c == '0':  # First number cannot be 0
                   
                    return False
                number_started = True  # First number is okay, now flag is on
            # If number_started is already True, numbers can continue
        else:  # Character is a letter
            if number_started:  # Letter after a number → invalid
                print("Invalid")
                return
            # Otherwise, letters before numbers are fine

    # Step 4: If all rules passed
    print("Valid")


main()
