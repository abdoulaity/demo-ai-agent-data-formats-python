import random
import json

# 1-Openning the JSON file
with open ("3_data/data.json") as f:
    agent_data = json.load(f)

# 2-Checking if the file is a list (of dicts)
if isinstance (agent_data, list):
    print("agent_data is a list")
else:
    print("agent_data is not a list")   

# 3-Picking randomly one dict inside that list
agent_pick = random.choice(agent_data)
print(f"The Random choice is: {agent_pick}") 

# 4-Checking if the elements inside the list are truly dicts
if isinstance (agent_pick, dict):
    print("agent_pick is a dict")
else:
    print("agent_pick is not a dict")

# 5-Looping over the chosen dict to create a smaller dict
new_agent_data = dict()
for key, value in agent_pick.items():
    # The item/pair we want to exclude everytime ("wordId": "id")
    if key != "wordId":
        new_agent_data[key] = value

print(f"new_agent_data is a smaller dict: {new_agent_data}")    
    