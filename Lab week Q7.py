def anagram(word1,word2):
    my_dict1 = {}
    my_dict2 = {}
    
    for char in word1:
        if char in my_dict1:
            my_dict1[char] = char + 1
            
        else:
            my_dict1[char] = 1
            
            
    for char in word2:
        if char in my_dict2:
            my_dict2[char] = char + 1
            
        else:
            my_dict2[char] = 1
            
    
    if my_dict1 == my_dict2:
        return True

word1 =input("Kindly enter word1:")
word2 =input("Kindly enter word2:")
print(anagram(word1,word2))