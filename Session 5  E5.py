##remove_dollar_sign, takes 1 parameter: s, where s is the input string, returns the new string with no dollar sign in it
##Hint: Google “Python string replace remove”

##s=input("Enter: ")
def remove_dollar_sign(s):
    
    s=s.replace("$","")
    print(s)
    return s
remove_dollar_sign("$80% percent of $life is to show $up")


#E6

string_with_no_dollars = remove_dollar_sign("$80% percent of $life is to show $up")
if string_with_no_dollars == "80% percent of life is to show up":
    print("Your function is correct")
else:
    print("Oops, there's a bug")
