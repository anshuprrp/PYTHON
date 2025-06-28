# print("Anshu ji")
# import os
# print(os.getcwd())
# print(os.listdir())
# print(os.rmdir("venv"))
# print("saanvi")



#Chapter-2  Practice Set





# Q1_____WAP in python to add two numbers
# a=int(input("Enter first num:-"))
# b=int(input("Enter second number:-"))
# c=a+b
# print(c)
# print(a+b)



#Q2_______WAP in python to find remainder when a number is divided by Z
# any_num=int(input("Enter any number:-"))
# z=int(input("Enter value of Z:-"))
# rem=any_num%z
# print(rem)
# print(any_num%z)




#Q3______Check the type of the variable assigned using input() function
# a=input("Enter any character value:-")
# b=int(input("Enter any integer value:-"))
# c=float(input("Enter any float value:-"))
# d=input("Enter any mix char and int value:-")
# e=bool(input("Enter any boolean value:-"))
# print({a,b,c,d,e})
# print(type(a,b,c,d,e))
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)

#Other Question_relatedpractice
# e=(input("Enter any boolean (true/false):-"))
# print(e)
# print(type(e))
# if e.lower()=="true":
#     print(e)
#     e=True
# elif e.lower()==False:
#     print(e)
#     e=False
# else:
#     print("wrong input")
# print(type(e))
# print(e)







#Q3_____compair the input enter by user which are grether or less than
# a=int(input("Enter the first value:-"))
# b=int(input("Enter the second value :-"))
# c=a>b
# print("A is grether than B:-","value of a:--",a,"--",c)
# d=a<b
# print("B is grether than A:-","value of b:--",b,"--",d)
# e=a==b
# print("A is equale to B:-","value of a:--",a,"value of b:--",b,"---",e)
    





# import numpy as np  # Import NumPy

# # Create two arrays
# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])

# # Add the arrays
# result = a + b

# # Print the result
# print("Array A:", a)
# print("Array B:", b)
# print("Sum:", result)

# a=7
# b=5
# print(a>b)
# print(a<b)
# print(int((a+b)/2))
# inn=int(input("enter num :-"))
# print(inn**2)







#########################################################################



#CHAPTER      3 STRING


# na="anshu kumar"
# ank=na[0:3]
# print(len(na))
# print(ank)
# na1=na[0:len(na)]
# na2=na[0:8]
# na3=na[:]
# print("na1:",na1)
# print(na2)
# print(na3)






# na="saanvi"
# na1=na[-5:-1]
# na2=na[-5:]
# na3=na[:-1]
# na4=na[-6:len(na)]
# print(na1)
# print(na2)
# print(na3)
# print(len(na))
# print("na4:",na4)
# print(len(na4))



# pa="saanvi and anshu"
# print(len(pa))
# pa1=pa[0:16:2]
# pa2=pa[1:16:2]
# pa3=pa[0:16:3]
# pa4=pa[:len(pa):1]
# print([pa,pa1,pa2,pa3,pa4])



# gf="saanvi"
# pri=gf.endswith("vi")
# print(pri)
# print(gf.endswith("vi"))

# pp=None
# print("kk1",pp)
# print("xyz",type(pp))
# # print("ddgf",len(pp))
# print("ansh",None)
# mm=pp[0:]
# print(mm)



# pp="saanvi and anshu"
# print(pp.count("a"))
# print(pp.count("aa"))
# print(pp.count("an"))






# sp="saanvi and anshu"
# print(sp)
# sp.capitalize()
# print(sp.capitalize())
# nn="itc"
# print(nn.capitalize())
# mm=nn.capitalize()
# nn.capitalize()
# print(nn)






# pp="saanvi and saanvi or saanvi"
# # print(pp)
# # print(pp.find("an"))
# # print([type(pp),(len(pp))])
# # print(pp,("anshu"))
# print("anshu \t","saanvi","\n")
# print(pp,"\t \nanshu")









# ak="saanvi and saanvi or rohini"
# print(ak)
# print(ak.replace("rohini","rakhi"))
# ak.replace("rohini","rakhi")
# print(ak)




###########################################################################
#PRACTICE  SET 3



#Q1
# m=input("enter your name:- ")
# print(f"welcome and good afternoon {m}")
# print("welcome and good afternoon",m)







#Q2
# letter='''Dear <|name|>,
# You are selected!
#     <|date|>'''
# name=input("Enter your name:- ")
# date=input("Enter the date:- ")
# print(letter)
# print(letter.replace("<|name|>", name).replace("<|date|>", date))
# letter=letter.replace("<|name|>", name)
# letter=letter.replace("<|date|>", date)
# print("anshu")
# print(letter)







##################################################################################
#CHAPTER   6   
#PRACTICE    SET  6
#Q 1
# f1=int(input("enter first num:-"))
# f2=int(input("enter second num:-"))
# f3=int(input("enter third num:-"))
# f4=int(input("enter fourth num:-"))
# if f1>f2 and f1>f3 and f1>f4:
#     print(f"f1 is greatest{f1}")
# elif f2>f1 and f2>f3 and f2>f4:
#     print(f"f2 is greatest{f2}")
# elif f3>f1 and f3>f2 and f3>f4:
#     print(f"f3 is greatest{f3}")
# else:
#     print(f"f4 is greatest{f4}")






# a = 8
# b = 7
# sum = a+b
# print(sum)
# print(a+b)
# def sum(a,b):
#     sum=a+b
#     print(sum)
#     sum=a*b
#     print(sum)
#     return sum
# sum (2,5)
# sum(45,25)


# def avg(a,b,c):
#     ag=int((a+b+c)/3)
#     print(ag)
#     return ag

# avg(2,4,6)
# g=avg(8,6,4)
# print(type(g))






# ram=["sita","saanvi",45,14.2,"anshu","saanvi","rohini"]
# ram=[1,5,3,4,8,2,5,1,]
# ram.sort()
# print(ram)
# ram.reverse()
# print(ram)
# ram.append(20)
# ram.insert(2,2020)
# ram.sort()
# print(ram)
# ram.reverse()
# # print(ram.pop())

# print(ram)






# m=0
# num=[]
# while m<5:
#     pp=int(input("enter num:-"))
#     num.append(pp)
#     m+=1
#     print(num)
# mm=num
# print(num)
# nn=num.reverse()
# print(num)
# if nn==mm:
#     print("palendrom number")
# else:
#     print("not palendrom number")




# ram=[1,5,3,4,8,2,8,5,1,]
# ram.sort()
# print(ram)
# ram.pop(1)
# print(ram)
# ram.remove(8)
# print(ram)
# print(ram.pop(1))
# print(ram.remove(8))
# ram=(1,5,3,4,8,2,1,1,1,1,8,5,1,0)
# print(ram)
# print(ram.count(1))
# print(ram.index(1))







#CHAPTER      4    Practice Set:-4
###############################################################################################################
#_____Q1
# ram=[]
# m=0
# while m<7:
#     m+=1
#     vv=input("Enter num or name:-")
#     ram.append(vv)
# print(ram)
# print(len(ram))




#_____Q2
# sub=[]
# print(sub)
# a1=(input("Enter computer subject name :--"))
# a2=(input("Enter maths subject name :--"))
# a3=(input("Enter science subject name :--"))
# a4=(input("Enter hindi subject name :--"))
# a5=(input("Enter english subject name :--"))
# a6=(input("Enter socle science subject name :--"))
# sub.append(a1)
# sub.append(a2)
# sub.append(a3)
# sub.append(a4)
# sub.append(a5)
# sub.append(a6)
# print(sub)









#___Q3

#____try--1
# tata=()
# tata.append("anshu")

#____try--2
# tata=(1,3,4,5,6,7,8,9,0,4,5,6,7,8,90,)
# print(tata.pop(7))

#____try--3
# tata=(1,3,4,5,6,7,8,9,0,4,5,6,7,8,90,)
# print(tata.remove(7))

#____try--4
# tata=(1,3,4,5,6,7,8,9,0,4,5,6,7,8,90,)
# print(tata.insert(7,5))









#___Q4
# kuku=[]
# m=0
# while m<4:
#     mm=int(input("enter num:-"))
#     kuku.append(mm)
#     m+=1
# print(kuku)










#___Q5
# a=(7,0,8,0,0,9)
# print(a.count(0))








#__________Chapter----9




# h=open("practice.txt","w")
# h.write("hi everyone\nwe are learning File I/O\n using java.\nI like programming in java.")
# h.close
# f=open("practice.txt","r")
# ap=f.read()

# print(ap)


# f=open("saanvi.txt","w")
# ap=f.write("Anshu and Saanvi\nAnshu&Saanvi")
# print(ap)



#Dicts
# ak={}
# ak["cat"]="this is a cute pet"
# ak["dog"]="a honest pet"
# print(ak)





# ak={ 10.00,10.000,"10.000",9,9.00,9,8,1,2,3}
# print( ak)


#______________________________find occurrence in str___
# word="ak&kp$count&df&  nk&jjjj&"
# # print(word.count())
# print(len(word))
# print(word.count("&"))



#___________________________Ood &even number___
# num=int(input("enter number:-"))
# if num%2==0:
#     print("Even number")
# else:
#     print("Odd number")




#____________WAP to find the greatest of 3 numbers entered by the user.___.

# num1=int(input("enter num1 :-"))
# num2=int(input("enter num2 :-"))
# num3=int(input("enter num3 :-"))

# if num1>num2 and num1> num3:
#     print("num 1 is greatest:-",num1)

# elif num2> num1 and num2> num3:
#     print("num 2 is greatest:-",num2)

# else:
#     print("num 3 is greatest:-",num3)




#_______WAP to check if a number is a multiple of 7 or not.______
# kk=int(input("enter num:--"))
# if kk%7==0:
#     print(f"yes this {kk} is multipale of 7")
# else:
#     print("It is not multipale of 7:--",kk)




#____ WAP to ask the user to enter 
# _________________names of their 3 favorite movies & store them in a list.

# mo_li=[]
# print(type(mo_li))
# mov1=input("Enter movies name:--")
# mo_li.append(mov1)
# mov2=input("Enter movies name:--")
# mo_li.append(mov2)
# mov3=input("Enter movies name:--")
# mo_li.append(mov3)
# print(mo_li)



#__ WAP to check if a list contains a palindrome of elements.
#  (Hint: use copy( ) method)
#  [1, 2, 3, 2, 1]
#  [1, “abc”, “abc”, 1


# jj=[]
# jj.append(input("enter num:--"))
# jj.append(input("enter num:--"))
# jj.append(input("enter num:--"))
# jj.append(input("enter num:--"))
# jj.append(input("enter num:--"))
# kk=jj.copy()
# kk.reverse()
# if jj == kk:
#     print(" palindrome word:--",jj)
# else:
#     print("Not palindrome word:--",jj)



#__WAP to count the number of students with the “A” grade in the following tuple.
#__ [”C”, “D”, “A”, “A”, “B”, “B”, “A”]
#__and after Store the above values in a list & sort them from “A” to “D”.

# lk=["C","D","A","A","B","B","A"]
# print(lk.count("A"))
# print(lk)
# lk.sort()
# print(lk)




# ____dic   concept practice--
# name={
#     "anshu":"saanvi",
#     "rahul":"khushabu",
#     "ravi":"aditi",
#     "nandan": "khushi",
# }
# print(name.get("saanvi"))
# print(name.items())
# nam={"ravi":"kritika","nandan":"richa","ankit":"riya","gautam":"soumya rani"}
# name.update(nam)
# print(name)




#__DICT__&__SETS

#__ Store following word meanings in a python dictionary : 
#        table : “a piece of furniture”, “list of facts & figures”
#        cat : “a small animal”


#_____Question__
# pate={
#     "table":"a piece of furniture" "list of facts & figures",
#     "cat" :"a small animal"
# }
# print(pate)


#__Question__
#                   You are given a list of subjects for students. Assume one classroom is required for 1
#                   subject. How many classrooms are needed by all students.
#                                     ”python”, “java”, “C++”, “python”, “javascript”,
#                                       “java”, “python”, “java”, “C++”, “C”

# rq={"python", "java", "C++", "python", "javascript","java", "python", "java", "C++", "C"}
# print(rq)
# print("class room required is :--",len(rq))

#__Question__
#___WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with
#  an empty dictionary & add one by one. Use subject name as key & marks as value.

# st={
# }
# sub1=input("enter subject 1 name:--")
# mk1=input("enter marks of subject:--")
# st.update({ sub1 :  mk1 })
# sub2=input("enter subject 2 name:--")
# mk2=input("enter marks of subject:--")
# st.update({ sub2 : mk2 })
# sub3=input("enter subject 3 name:--")
# mk3=input("enter marks of subject:--")
# st.update({ sub3 : mk3 })
# print(st)



#__Question__
#__----------- Figure out a way to store 9 & 9.0 as separate values in the set. 
# ------------(You can take help of built-in data types).

# case--1___not store
# st1={1,2,9,9.0}
# print(st1)

# case--2__yes store hear
# st2={1,2,9,'9.0'}
# print(st2)

#case--3__yes store hear
# st3={1,2,9,"9.0"}
# print(st3)






#____Loops___
#---Question____(while loop)
# ____________________Print numbers from 1 to 100.

# i=1
# while i<101:
#     print(i)
#     i+=1
# print("-:-END-:-")

#---Question---
#------------------- Print numbers from 100 to 1.

# i=100
# while i>0:
#     print(i)
#     i-=1
# print("-:END-:-")


#---Question---
#-----------------------Print the multiplication table of a number n.
# i=int(input("Enter number:-"))
# p=1
# while p<11:
#     print(i*p)
#     p +=1
# print(f"The multiple table of :-{i}")


#---Question---
#--------Print the elements of the following list using a loop: ___[1, 4, 9, 16, 25, 36, 49, 64, 81,100]


# ________case--1

# li=[1, 4, 9, 16, 25, 36, 49, 64, 81,100]
# i=0

# while i < len(li):
#     print(li[i])
#     i += 1

# print("-:-END-:-")

# ________case--2--

# li=[1, 4, 9, 16, 25, 36, 49, 64, 81,100]
# i = 1

# while i < 11 :
#     m = i*i
#     i += 1
#     print(m)

# print("-:-END-:-")




#---Question---

#____Search for a number x in this tuple using loop:
#_______ (1, 4, 9, 16, 25, 36, 49, 64, 81,100)_____

tp=(1, 4, 9, 16, 25, 36, 49, 64, 81,100)

n=int(input("enter number:--"))

p=16

i=1
while i < 10 :
    if n == tp.count(n):
        tp.index(p)
        print(f"Fount at index:{n}")
    else:
        print("number not found in this tuple")
    i += 1

print("-:-END-:-")















































#____OOPS   concept
