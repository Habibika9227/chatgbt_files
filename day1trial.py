
def main():
    while True:
        try: 
            user_input=input("Enter Something: ")
            # Here we're checking validation
            if not user_input:  #if user did'nt provide an input we raise an  error
                raise ValueError("Input should'nt be empty")
            if not any(char.isalpha() for char in user_input): #checks and detects if that current char is alpha and returns true if not returns false.

                raise ValueError("Input must contain at least one letter")
            break  #break out of the loop if all above conditions are true
        except ValueError as e: # e stores the error raised in this block of code and prints 
                                # avoiding program to crash
            print("Error", e)   
    send_to_count_characters=count_characters(user_input)
    print(f"characters(no spaces): {send_to_count_characters}")
    send_to_count_total_words=count_total_words(user_input)
    print(f"Words: {send_to_count_total_words}")
    result1=unique_words(user_input)
    print(f"unique words: {result1}")
    result2=word_frequence(user_input)
    print("Frequency:")
    for key,value in result2.items():
        print(f"{key} -> {value}")
    longest=longest_word(user_input)


def count_characters(count):
    # How do we count characters.
    counting=0 # iniate a variable to track counting
    
    for char in count:
        if not char.isspace(): # if char is other than space,newline,taps it'll be considered

            counting+=1 # start counting if it's a letter
    return counting

def count_total_words(words):
    
    flag_check=False
    counting=0
    for count in words:
        if count.isspace(): # check at that particular char is space, if yes, set flag to 0
             flag_check=False
        else:
            if not flag_check: # if at that particular char is'nt space then set flag to true
                flag_check=True
                counting+=1
    return counting

def unique_words(unique):
    clean=""
    for char in unique:
        if char.isalpha() or char.isspace():
            clean+=char

    words=clean.lower().split()
    return set(words) # Set removes duplicates

def word_frequence(frequency):
    clean=""
    for char in frequency:
        if char.isalpha() or char.isspace():
            clean+=char

    words=clean.lower().split()
    fre={} # We use dict to count frequency
    for rep in words:
        if rep in fre:
            fre[rep]+=1
        else:
            fre[rep]=1
    return fre
def longest_word(words):
    clean=""
    for char in words:
        if char.isalpha() or char.isspace():
            clean+=char
    word=clean.lower().split()
    if not words: 
        raise ValueError("No valid words found")
    max_len=0
    longest=[]
    for lon in word:
        if len(lon) > max_len:
            len(lon)=max_len
            longest=[lon]

        elif len(lon)==max_len:
            longest.append(lon)
    longest=list(set(longest))

    if len(longest)==1: # Counts how many words are in the list
        return longest[0] # returns the first word in the list
    else:
        return tuple(sorted(longest))



main()