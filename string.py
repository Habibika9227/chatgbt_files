# def main():
#     user_input=input("Word: ")
#     result=""

#     for index,char in enumerate(user_input):
#         if char.isalpha() and char.lower() :
#             result+="#"
#             if index % 2 ==0:
#                 result+=char.upper()
#             else:
#                 result+=char.lower()
#         else:
#             result+=char
#     print(f"new_result: {result}")
            
# main()


def master():
    get_input=input("Sentence: ")
    result=""
    for index,char in enumerate(get_input):
        if char.isalpha() and char.lower() not in "aeiou":
            result+="#"
            if index % 2 ==0:
                result+=char.upper()
            else:
                result+=char.lower()
        else:
            result+=char
    print(result)
    
master()