#               24/9/2026
#مشروع لحساب تكلفة دهان الحائط 

str_length=input('Please enter type length :')
str_width=input('Please enter type widgth :')
str_coast=input(' How much for 1 meter? :')

length=float(str_length)
width=float(str_width)
coast=float(str_coast)

area=length*width
the_coast=area*coast

str_area=str(area)
str_the_coast=str(the_coast)

print('The total area is:'+str_area)
print('Give the guy : $'+str_the_coast)