import random
import json

# 1-Openning the JSON file
with open ("3_data/data.json", "r", encoding="utf-8") as f:
    agent_data = json.load(f)
    print(f"A-agent_data: {agent_data}\n")
    
# 2-Checking if the file is a list (of dicts)
if isinstance(agent_data, list):
    print("B-agent_data is a List\n")
else:
    print("B-agent_data is not List\n")    

# 3-Picking randomly 3 dicts that will be sent to the LLM
agent_pick = random.sample(agent_data,3)
print(f"C-Here is the List of 3 Dicts by Random: {agent_pick}\n")

# 4-Cleaning for the LLM: Looping over the List to exclude the pair ("wordId": "id")
llm_agent_data = list()  # the new list as list accumulator
for item in agent_pick:  # outer loop: one item = one dict
    new_dicts = dict()   # the new dicts as dict accumulator for each item
    
    for key, value in item.items():  # inner loop: one key/value of each item
        if key != "wordId":          # removing the pair ("wordId": "id")
            new_dicts[key] = value   # fill the small dict

    llm_agent_data.append(new_dicts)        # add the finished dict to the list
print(f"D-The List of Dicts without the id pairs: {llm_agent_data}\n")

# 5-Confirming that llm_agent_data remained a list in the end
if isinstance(llm_agent_data, list):
    print("E-llm_agent_data is a List\n")
else:
    print("E-llm_agent_data is not List\n")   

