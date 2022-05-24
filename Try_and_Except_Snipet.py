print ("Start test")
try:
    x = input(" Enter a letter:")
    x = int(x)
except:
    print ("Sorry Dave... I can't do that")
else:
    print (f"x={x}")