import json
	
# Data to be written
State_Capital ={
"Bihar": "Patna","Goa": "Panaji","Chattisghar": "Naya Raipur","Madhya Pradesh": "Bhopal","West Bengal" : "Kolkata","Maharastra" : "Mumbai","Gujrat" : "Gandhinagar"
}
#  Writing it in the JSONs file
with open("C:\\Users\\INTEL\\OneDrive\\Desktop\\Python\\assignments\\a6.q2.state_capital.json","w") as file:
    json_object = json.dump(State_Capital,file)