# Enumerate
l=[10,20,30,40,50]

for i in enumerate(l):
    print(i)
print()
# Another method
for i,j in enumerate(l):
    print(i,"",j)


# Given a list of shares' names, enumerate and print each name with its corresponding index.

us_shares = ['Apple', 'Microsoft', 'Amazon', 'Google', 'Facebook']
in_shares=['Reliance','Hdfc','Icici','Infosys','TCS','Hul','Adani','Mrf','Irctc','Indigo']

print("Foreign shares")
for index, share in enumerate(us_shares):
    print(f"Share {index+1}: {share}")
print()
print("Indian shares:")
for index, share in enumerate(in_shares):
    print(f"Share {index+1}: {share}")