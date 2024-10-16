# Create a new python file stringtask.py and attempt the 5 questions below:
#Clean up the following variable to give the clean version in lower case. Using inbuilt methods in the str class 
#name = “  JOHn  .“ to “john”
#Slice the below string to get you the resulting sentence:
#sentence_one = “The Dog Breed is German Shepherd” only display “Breed is German”
#sentence_two = “Defeats for the Clinton forces, this was her moment of triumph” only display “Clinton forces”
#Split the below sentence using a semicolon i.e ; And display length of the result. 
#“The lazy dog; ran so fast; it hit the wall.” 
#first_name="  Joh.n"  last_name="   Do,e" Clean up and display Full name i.e John Doe

#Having the string r = '["E","W","C"]' #Manipulate it to display EWC
#Attempt questions in the link below. Whether you get the right answer or not, still read the solution explanation.



name="  JOHn  ."
name=name.lower()
name=name.replace("."," ")
name=name.strip()
print(name)

sentence_one="The Dog Breed is German Shepherd"
sliced_sentence_one=sentence_one[8:23]
print(sliced_sentence_one)

sentence_two="Defeats for the Clinton forces, this was her moment of truimph"
sliced_sentence_two=sentence_two[16:30]
print(sliced_sentence_two)

sentence_three="The lazy dog; ran so fast ;it hit the wall"
sentence_four=sentence_three.split(";")
print(sentence_four)

firstname="Joh.n".strip()
firstname=firstname.replace(".","")
lastname="Do,e".strip()
lastname=lastname.replace(",","")
fullname=firstname + " " + lastname
print(fullname)


string_r=["E","W","C"]
string_r2="".join(string_r)
print(string_r2)