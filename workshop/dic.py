d = {1:10,
     2:20,
     3:30,
     4:40,
     5:50,
     6:60}
n = int(input("Enter the key "))
if n in d.keys():
    print("Exist")
else:
    print("Not Exist")