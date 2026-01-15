def main():
    user_input=input("Expression ").replace("+"," + ")
    user_input=user_input.replace("-"," - ")
    user_input=user_input.replace("*", " * ")
    user_input=user_input.replace("/"," / ")
    

    parts=user_input.split()
    result=condi_tionals(parts)
    print(f"Result: {result:.2f}")

def condi_tionals(con):
    x=int(con[0])
    y=con[1]
    z=int(con[2])
    if y=="+":
       result=x+z
    elif y=="-":
       result=x-z
    elif y=="*":
       result=x*z
    else:
       result=x/z
        
    return result

main()