#QUES1

import pandas as pd
number=int(input("Enter The Range : "))
num_list=[]
res=[]
for i in range(number):
    num=int(input("enter the number:"))
    num_list.append(num)
    res.append(num*num)
print(res)
s = pd.Series(res,index=[num_list])
print(s)



#QUES2
import pandas as pd
s = pd.Series([1,2,3,4,5])
p = pd.Series([1,2,3,4,5])
print(s)
print(p)
print("adition is:\n",(s+p))
print("sub is:\n",(s-p))
print("mul is:\n",(s*p))
print("div is:\n",(s/p))
print("rem is:\n",(s%p))
