#question 7
#Write 
fo = open("f1.txt", "w") 
fo.write( "Python is a great language.\nYeah its great!!\n")
fo.close()
#read
f = open("f1.txt", "r") 
print(f.readline())

