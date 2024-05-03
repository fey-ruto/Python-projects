def ignore_string(m):
    ignore_str =m.strip().lower()
    return ignore_str

def anagram(word1,word2):
    ignored_string1 = ignore_string(word1)
    ignored_string2 = ignore_string(word2)
    
    my_dict1 = {}
    my_dict2 = {}
    
    for char in ignored_string1:
        if char in my_dict1:
            my_dict1[char] = char+1
            
        else:
            my_dict1[char] = 1
            
            
    for char in ignored_string2:
        if char in my_dict2:
            my_dict2[char] = char+1
            
        else:
            my_dict2[char] = 1
            
    
    return my_dict1 == my_dict2

word1 =input("Enter word1:")
word2 =input("Enter word2:")
print(anagram(word1,word2))