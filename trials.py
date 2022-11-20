"""Python functions for JavaScript Trials 1."""

# 
def output_all_items(items):
    pass  # TODO: replace this line with your code
    for item in items:
        print(item)
    


def get_all_evens(nums):
    pass  # TODO: replace this line with your code
    even_num=[]
    for num in nums:
        if num %2 ==0:
            even_num.append(num)
    return even_num


def get_odd_indices(items):
    #// Given an array, return all elements at odd numbered indices.

    result=[]
    for i in items:
        if i %2 !=0:
            result.append(items[i])

    return result

#Given an array, output a numbered list.
# Ex.:
# // > printAsNumberedList([1, 'hello', true]);
# // 1. 1
# // 2. hello
# // 3. true
def print_as_numbered_list(items):
    pass  # TODO: replace this line with your code
    i=1
    for item in items:
        print(f'{i}. {item}')
        i+=1
              
# // Return an array of numbers in a certain range.
# //
# // Ex.:
# // > getRange(0, 5);
# // [0, 1, 2, 3, 4]
# //
# // > getRange(1, 3);
# // [1, 2]
def get_range(start, stop):
    nums=[]
    for num in start and num in stop:
        nums.append(num)
    return nums   
 
# // Given a string, return a string where vowels are replaced with '*'.
# //
# // Ex.:
# //   > censorVowels('hello world');
# //   'h*ll* w*rld'
def censor_vowels(word):
    char=[]
    for letter in word:
        if 'aeiou'.contains(letter):
            char.append("*")
        else:
            char.append(letter)
    return " ".join(char)        


def snake_to_camel(string):
    pass  # TODO: replace this line with your code
    camel_case = []
    for word in string.split("_"):
        camel_case.append(f'{word[0].upper()} {word.slice(1)}')
    return "".join(camel_case)

def longest_word_length(words):
    pass  # TODO: replace this line with your code
    longest=len(words[0])
    for word in words:
        if longest< len(word):
            longest=len(word)
    return longest

def truncate(string):
    pass  # TODO: replace this line with your code
    result = []
    for char in string:
        if len(result==0 or char !=result[-1]):
            result.append(char)  
    return "".join(result)
            
        

def has_balanced_parens(string):
    pass  # TODO: replace this line with your code
    parens = 0
    for char in string:
        if char =="(":
            parens +=1
        elif char ==")":
            parens -=1
        if parens<0:
            return False        
    return parens==0
def compress(string):
    compressed = []
    curr_char=""
    char_count=0
    for char in string:
        if char != curr_char:
            compressed.append(curr_char)
            if char_count > 1:
                compressed.append(str(char_count))
            curr_char=char
            char_count=0
            
        char_count+=1
    compressed.append(curr_char)   
    if char_count >1:
        compressed.append(str(char_count)) 
    return "".join(compressed)    
