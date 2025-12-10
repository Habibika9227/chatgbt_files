def main():
    price=input("Enter the price of the item: ")
    discount=input("Enter discount: ")
    send_price=conv_price(price)
    send_discount=conv_discount(discount)
    discount_cal=send_price -(send_price * send_discount)
    print(f"Original: {send_price}")
    print(f"Discount percentage: {send_discount}")
    print(f"Final price: {discount_cal}")

def conv_price(conv):
    conv=conv.replace("$", "")
    return float(conv)

def conv_discount(disc):
    disc=disc.replace("%", "")
    return float(disc)/100



main()