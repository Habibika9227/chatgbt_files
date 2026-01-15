
def main():
    new_dic={}
    while True:
     try:
        data=input("> ").lower().strip()

        splitted=data.split()
        x=splitted[0]
        if x != "add":
            continue
        y=splitted[1]
        z=float(splitted[2])
        if z==

        if y in new_dic:
            new_dic[y].append(z)
        else:
            new_dic[y]=z
        

