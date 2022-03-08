def isPalindrome(word):
    sample_list = []
    for i in word:
        sample_list.append(i)
    reverse_list=[]
    reverse_list = sample_list.copy()
    reverse_list.reverse()
    if sample_list == reverse_list:
        return 1
    else:
        return 0


words = ['reviver', 'rotor', 'python']
for j in words:
    if isPalindrome(j) == 1:
        print("It is a palindrome")
    else:
        print("It is not a palindrome")

