# def greet_user():
#     name=input("what's your name?")
  
#     return name

# go=greet_user()
# print(f"hello, {go}")


# def add_numbers(x,y):
#     return x+y
# x=int(input("enter a value of x: "))
# y=int(input("enter a value of x: "))
# z=add_numbers(x,y)
# print(f"the sum is: {z}")


# def convert_minutes(minutes):
#     return minutes*60
# user_input=int(input("Enter a number min->sec: "))

# convertion=convert_minutes(user_input)
# print(convertion)

# def format_name(full_name):
#     name=full_name
#     name=name.strip().title()
#     return name

# user_input=format_name(input("whats your name?  "))
# # call=format_name(user_input)
# print(user_input)


# def fast_last(name):
#     return name[0] + name[-1]

# user_input=input("what is your name? ")
# call=user_input.strip().title()
# ser=fast_last(call)
# print(ser)

def main():
   
   user_input=input("what is the price of the item? ")
   discount_input=input("How much is the price? ")
   price=dollar_to_float(user_input)
   discount=percent_to_float(discount_input)
   result=price*(1-discount)
   print(result)


def dollar_to_float(d):
    d=d.replace("$","")
    return float(d)

    


def percent_to_float(p):
    p=p.replace("%","")
    return float(p)/100



main()

# def main():
#     price_string = input("How much is the item? ")
#     discount_string = input("What is the discount? ")

#     price = dollar_to_float(price_string)
#     discount = percent_to_float(discount_string)

#     final_price = price * (1 - discount)

#     print(f"Final price: ${final_price:.2f}")


# def dollar_to_float(d):
#     d = d.replace("$", "")
#     return float(d)


# def percent_to_float(p):
#     p = p.replace("%", "")
#     return float(p) / 100


# main()