def randomString(stringLength):
 
 letters = string.ascii_letters
 return ''.join(random.choice(letters) for i in range(stringLength))
print ("Random String is ", randomString(5) )
