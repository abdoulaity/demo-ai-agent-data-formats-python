import random
import json

# 1-Openning the JSON file
with open ("3_data/data.json", "r", encoding="utf-8") as f:
    agent_data = json.load(f)
     

# 4-Cleaning for the LLM: Looping over the List to exclude the pair ("wordId": "id")
agent_data = list()  # the new list as list accumulator

for item in agent_data:  # outer loop: one item = one dict
    # TEST 1
    print (f"TEST 1: {agent_data}\n")
    new_dicts = dict()   # the new dicts as dic accumulator for each item

    for key, value in item.items():  # inner loop: one key/value of each item
        if key != "wordId":          # removing the pair ("wordId": "id")
            new_dicts[key] = value   # fill the small dict

    agent_data.append(new_dicts)        # add the finished dict to the list

print(f"3-The List of Dicts without the id pairs: {agent_data}\n")

isinstance(agent_data, list)

