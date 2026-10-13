import random
import json

# 1-Openning the JSON file
with open ("3_data/data.json", "r", encoding="utf-8") as f:
    agent_data = json.load(f)
    
# 2-Checking if the file is a list (of dicts)
if isinstance(agent_data, list):
    print("1-agent_data is a List\n")
else:
    print("1-agent_data is not List\n")    

# 3-Picking randomly 3 dicts that will be sent to the LLM
agent_pick = random.sample(agent_data,3)
print(f"2-Here is the List of 3 Dicts by Random: {agent_pick}\n")

# 4-Cleaning for the LLM: Looping over the List to exclude the pair ("wordId": "id")
llm_agent_data = list()  # the new list as list accumulator

for item in agent_pick:  # outer loop: one item = one dict
    new_dicts = dict()   # the new dicts as dic accumulator for each item

    for key, value in item.items():  # inner loop: one key/value of each item
        if key != "wordId":          # removing the pair ("wordId": "id")
            new_dicts[key] = value   # fill the small dict

    llm_agent_data.append(new_dicts)        # add the finished dict to the list

print(f"3-The List of Dicts without the id pairs: {llm_agent_data}\n")

isinstance(llm_agent_data, list)

