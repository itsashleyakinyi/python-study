#create a new file called extra_strings_task.py
#1 concatenation practice:
#create two variables, first name and last name and assign them to your first and last name respectively. concatenate them into a string called full_name with a space between the names. Print full_name

fname="Ashley"
lname="Naomi"
full_name=fname + " " +lname
print(full_name)

#2.indexing pracice:
#Given the string word="PYTHON", print the first and last characters using indexing
word="PYTHON"
print(word[0])
print(word[5])

#3. Slicing practice:
#Given the string phrase "Learning Python is fun!",use slicing to extract and print the substring "python"
phrase="Learning python is fun!"
print(phrase[8:15])

#4.Reversing a string:
#Given the string text "Reverse this",print the reversed versin of the string
txt="Reverse this"
print(txt[::-1])


#5.Character replacement
#Given a string 'greeting= "Hello World", replace "World" with "Python" and print the result

greeting="Hello World!"
greeting=greeting.replace("World","Python")
print(greeting)


#6.Uppercase and Lowercase
#Take the string 'msg="Python programming" and print it in all uppercase and all lowercase letters
msg="Python programming"
print(msg.upper())
print(msg.lower())

#7.Count occurences:
#Given the string sentence="This is a simple sentence." , count how amny times the letter "s "  appears in the string

sentence="This is a simple sentence"
letter_s=sentence.count("s")
print(letter_s)

#8.Check substring presence:
#Take the string quote="The best way to predict the future is to create it" and check if the substring "future" exists in the string

quote="The best way to predict the future is to create it"
print("future" in quote)



#9.String length:
#given the string 'description="Data Science" print the length of the string
description="Data Science"
print(description.__len__())




#10.Remove Whitespace
#-Given the string name="    John Doe   ",remove the leading and trailing spaces and print the result.
name="    John Doe   "
print(name.strip())

