from dataclasses import dataclass
import random
import json

# 1-Openning the JSON file
with open("3_data/data_full.json", "r", encoding="utf-8") as f:
    agent_data = json.load(f)
    print(f"A-agent_data: {agent_data}\n")
    
# 2-Checking the object type of the new data (agent_data == data_full.json)
object_type = type(agent_data)
print(f"B-agent_data that holds the new dataset is a: {object_type} (of 3 Dicts and 1 List: Dict -> Dict, then List -> Dict)\n")