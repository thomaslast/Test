"""

Program that checks 2 stings for the same characters

"""

string1 = "harpoon"
string2 = "countryside"
array=[]
count=0
for i in string1[0:]:
  for d in string2[0:]:
    if i == d:
      print (i)
      array.append(i)
      count=count+1
print (set(array))

