string1 = "Text "
string2 = "text "
string3 = "tralala "
string4 = "for "
string5 = "tralalala "

print(string1 + string2 + string3 + string4 + string5)  # with +

print("Text " "text " "tralala " "for " "tralalala ")   # without +

print("Hello " * 5)         #Hello Hello Hello Hello Hello

print("Hello " * (5 + 4))   #Hello Hello Hello Hello Hello Hello Hello Hello Hello
print("Hello " * 5 + "4")   #Hello Hello Hello Hello Hello 4

today = "friday"
print("day" in today)       #True
print("fri" in today)       #True
print("thur" in today)      #False
print("parrot" in "fjord")  #False
