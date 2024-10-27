person={
    "name":"Ashley",
    "age":50,
    "gender":"Female",
    "location":["kiambu",518,"Thika"],
    "address":{
       "street":'Muthaiga',
       "city":"Nairobi",
       "Country":"Kenya"

    }
}
print(type(person))
print(person)

print(person['name'])
print(person['age'])
print(person['gender'])
print(person['location'][2])
print(person["address"]["Country"])
print(person["address"]["street"])
person['age']=60
person['location']="south c"
person["occupation"]="Programmer"
print(person)


print(person.keys())
print(person.values())
print(person.items())
person.pop('occupation')
print(person)