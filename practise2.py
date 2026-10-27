# Roll_No=eval(input("Enter the roll no"))
# New_Roll_No=[]
# for i in Roll_No:
#     if(i in New_Roll_No):
#         continue
#     else:
#         New_Roll_No.append(i)
# for i in range(0, len(New_Roll_No),1):
#     print(New_Roll_No[i])
Roll_No=eval(input("Enter the roll no"))
New_Roll_No=[(1,'A',45),(2,'B',45)]
New_Roll_No.append(Roll_No)
id=eval(input("enter the id"))
for i in range(0,len(New_Roll_No),1):
    if(id==New_Roll_No[i][0]):
        print(New_Roll_No[i])
    else:
        continue
