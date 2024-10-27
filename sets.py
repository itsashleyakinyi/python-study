days = {"monday","tuesday","wednesday","thursday", "friday","saturday","sunday","sunday","sunday","sunday"}
print(days)

# Remove friday and sunday from the set using methods.
# Add them back to the set

days.remove("friday")
days.remove("sunday")
print(days)


#set methods
days.add("mon")#-used to add one value
print(days)

days.update()#-used to add multiple values
days.clear()#-clears everything in a set
days.discard()#-deletes one element