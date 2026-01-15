



def main():
    price=input("Enter the price of the item: ")
    discount=input("Enter the discount: ")
    send_price_to_conv=conv_dollar(price)
    send_discount_to_per=conv_percent(discount)
    final_price=cal_all(send_price_to_conv,send_discount_to_per)
    print_result(send_price_to_conv,send_discount_to_per,final_price)

def conv_dollar(doll):
    doll=doll.replace("$", "")
    return float(doll)

def conv_percent(perc):
    perc=perc.replace("$","")
    return float(perc)/100

def cal_all(price,discount):
    return price - (price * discount)
def print_result(price,conv,doll):
    print(f"Original: {price:.2f}")
    print(f"Discount: {conv:.2f}")
    print(f"Final: {doll:.2f}")
main()