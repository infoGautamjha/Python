#Strings-it is a data type that store a sequence of characters
#String
str1 = "Hello"
str2 = 'Hello'
str3 = """Hello"""
str4= "Today's"
str5="This is a string"
 #print(str5)

#Escape Sequence characters
  #\n-Used for next line
str6= "this is a Book.It's price is 400."
str7= "Hii, I am Gautam.\nPassout from Arya"
 #\t-Tab space
str8="Book price is high.\t So Buy hindi Book"

#Basic Operation 1
   #Concatenation-Add two string with the help of + operators
      #"hello" + "world" = helloworld
str9="hello"+ "world"
str10="Kanak"
str11="LLP"
str12=str10 + str11

 #length of string
     #len(str)
'''
str13="KanakLLP"
 #print(len(str13))
a1="Arya"
a2="Group of College"
a3= a1+ " "+ a2
print(a3)
print(len(a3))
'''
#Indexing-Position(to access Character)
#ch =a1[2]
 #print(ch)
a4= "Gautam Jha"
ch= a4[9]
 #print(ch)

#Slicing-Accessing parts of a string
  #Str[Stating_ind: ending_end] #ending idx is not included
  #str="AryaCollege"
  #str[1:4] is "rya"
  #str[:4] is same as str[0:4]
  #str[1:] is same as str[1: len(str)]
''' 
a5="Village_Karanpur"
 #print(a5[1:6])
print(a5[ :7])
 #print(a5[5:]) 
print(a5[8:])
  
  #negative index

b1="Apple"
print(Str1[-4:])

#String Function
b2= "I am a coder"
  # str.endswith("coder") - it returns true if string end with substr
print(b2.endswith("coder"))
  #otherwise it returns false
print(b2.endswith("App"))

  #str.capitalize() - capitalize 1st char

b3= "i am a writer"
print(b3.capitalize())
print(b3)

b4="not a good leader"
b4= b4.capitalize()
print(b4)

     #str.replace(old,new)- replaces all occurances of old
b5="Hii, I am gautam From Karanpur which falls is madhubani Dist of Bihar"
print(b5.replace("a", "n"))
print(b5)
b5=b5.replace("gautam", "Pradeep Jha")
print(b5)
print(b5)

  #str.find(word)-returns 1st index of 1st occurrer
b6= "Last days i visit hawa mahal, it's a good place in kukkas"
print(b6.find("i"))
print(b6.find("visit"))
print  (b6.find("z"))
   #when string value not exists it return -1

#str.count()- counts the occurrence of substr
b7= "I am not a good Coder, but you are also not a good Coder"
print(b7.count("not"))
print(b7.count("o"))

'''



