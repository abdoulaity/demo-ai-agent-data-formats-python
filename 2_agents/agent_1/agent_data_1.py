import random
import json

# 1-Openning the JSON file
with open ("3_data/data.json", "r", encoding="utf-8") as f:
    agent_data = json.load(f)

# 2-Checking if the file is a list (of dicts)
if isinstance (agent_data, list):
    print("A-agent_data is a list\n")
else:
    print("A-agent_data is not a list\n")   

# 3-Picking randomly one dict that will be sent to the LLM
agent_pick = random.choice(agent_data)
print(f"B-The Random choice is: {agent_pick}\n") 

# 4-Checking if the elements inside the list are truly dicts
if isinstance (agent_pick, dict):
    print("C-agent_pick is a dict\n")
else:
    print("C-agent_pick is not a dict\n")

# 5-Looping over the chosen dict to create a smaller dict for the LLM
llm_agent_data = dict()
for key, value in agent_pick.items():
    # The item/pair we want to exclude each time ("wordId": "id")
    if key != "wordId":
        llm_agent_data[key] = value

print(f"D-llm_agent_data is a smaller dict: {llm_agent_data}\n")    
    