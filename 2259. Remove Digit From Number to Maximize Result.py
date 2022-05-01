# 2259. Remove Digit From Number to Maximize Result
# You are given a string number representing a positive integer and a character digit.
# Return the resulting string after removing exactly one occurrence of digit from number such that the value of the resulting string in decimal form is maximized. 
# The test cases are generated such that digit occurs at least once in number.
number = "123181"
digit="1"
best=""
for i,j in enumerate(number):
    if(digit==j):
        current=number[:i]+number[i+1:]
        if(best == "" or current>best):
            best=current
print(best)
    
