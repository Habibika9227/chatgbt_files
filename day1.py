
def main():
    while True:
        try:
            user_input=input("Sentence: ").strip()
            if not user_input:
                raise ValueError("Input cannot be empty")
            if not any(char.isalpha() for char in user_input):
                raise ValueError("Input must contain atleast on letter")
            break
        except ValueError as e:
            print("Error:",e)
    result=anlyzer(user_input)
    print(f"Characters no space:{result}")
    result2=analyzer2(user_input)
    print(f'Words:{result2}')
    result3=unique_word(user_input)
    print(f"Unique words: {result3}")
    result4=frequency(user_input)
    for key, value in result4.items():
        print(f"{key}->{value}")
    result5=longest_word(user_input)
    print(f"Longest word(s):{result5}")

def anlyzer(l):
    
    #counting the length of chars in the sentence
    count=0
    for char in l:
        if not (char.isspace()):
            count+=1
    return count

def analyzer2(words):
    #Total words
    count_words=0
    flag_words=False #checks whether we're inside or outside a word.
    for chars in words:
        if chars.isspace():
            flag_words=False
        else:
            if not flag_words: # Is this the first char of a new word
                flag_words=True # If yes set it true
                count_words+=1

    return count_words    

def  unique_word(unique):
    #Checking uniqueness and the goodness of set that it removes duplicates
    unique=unique.lower().split() #converts str to a workable list.
    empty_set=set(unique)
    return empty_set 
    
def frequency(freq):
   #Since str are immutable, we need to move them into new variable,so that we can work on it.
   clean=""
   
   for char in freq:
       if char.isalpha() or char.isspace():
           clean+=char

   word=clean.lower().split() # This is gonna be list
   fre={}
   for w in word:
       if w in fre:
           fre[w]+=1
       else:
           fre[w]=1
   return fre

def longest_word(length):
    #here we built the str
    new_str=""
    for word in length:
        if word.isalpha() or word.isspace():
            new_str+=word
    # we then seperate the built str into list
    clean=new_str.split()
    if not clean: #checking if the list contains exclusively words
        raise ValueError("No valid words found")
    
    
    long=0 #we initiated because we wanted to make comparision
    longest=[]# here is where we keep updating the word based on their length
    for letter in clean:
        if len(letter)>long:
            long=len(letter)
            longest=[letter]

        elif len(letter)==long:
            longest.append(letter)
    longest=list(set(longest))
    if len(longest)==1:
        return longest[0]
    else:
        return tuple(longest)
    

main()
