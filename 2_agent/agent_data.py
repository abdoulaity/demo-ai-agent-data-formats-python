import random
import json

with open ("3_data/data.json") as f:
    agent_data = json.load(f)

if isinstance (agent_data, list):
    print("It's a list")

agent_pick = random.choice(agent_data)
print(agent_pick)    

