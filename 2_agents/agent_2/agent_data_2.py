import random
import json

# 1-Openning the JSON file
with open ("3_data/data.json", "r", encoding="utf-8") as f:
    agent_data = json.load(f)
    
# 2-Checking if the file is a list (of dicts)
if isinstance(agent_data, list):
    print("agent_data is a list")
else:
    print("agent_data is not list")    

# 3-Picking randomly 3 dicts that will be sent to the LLM
agent_pick = random.sample(agent_data,3)
print(agent_pick)

# ffff Cleaning
#agent_pick = list()
#for item in agent_data:
#    agent_pick.append(item)

#print (agent_pick)    




# 4-Checking if the elements inside the list are truly dicts
#if isinstance(agent_pick, list):
#    print("agent_data is a list")

# 5-Looping over the chosen dict to create a smaller dict

# The item/pair we want to exclude everytime ("wordId": "id")