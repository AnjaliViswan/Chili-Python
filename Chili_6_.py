'''Description @Anjali Viswan
This code figures out if a user's input is a palindrome or not.
'''
#prompt
x = str(input("Input string: "))
x = x.lower()
#initial vars
PALINDROME = False
word1 = str("")
#feeding first half into var word1
for i in x:
    word1 = word1 + i
    if ( len(word1) == (len(x))/2 ):
        break
#initial vars
counter = int(len(x))
word2 = str("")
#feedomg 2nd half into var word2
for i in range(len(x), 0, -1):
    counter-=1
    word2 = word2 + x[counter]
    if (len(word2) == (len(x))/2):
        break
#comparing first half to second half (word1 to word2)
if (word1 == word2):
    PALINDROME = True
#output
print("\nPalindrome check: ")
print(PALINDROME)
print("\n")








# palindrome ex racecar, tacocat, mam, 
# put the string into an array (list)
# if a[0] = a[-1], if a[1] = a[-2]

#if the first half equals the second half but backwards, its a palindrome
#also, if the list forward is the same backwards, its a palindrome