# WAP to displau7y liss of elements of a lists along with positive and negative index

# input --> [10,20,30,40,50,60,70,80,90] 

"""expected output

10 is present at index 0 / -9
20 is present at index 1 / -8
30 is present at index 2 / -7
40 is present at index 3 / -6
50 is present at index 4 / -5
60 is present at index 5 / -4
70 is present at index 6 / -3
80 is present at index 7 / -2
90 is present at index 8 / -1
"""

l=[10,20,30,40,50,60,70,80,90]

n=len(l)

for i in range(n):
    print("{} is present at index {} / {}".format (l[i],i,i-n))