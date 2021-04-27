import json
def load_event_data():
    file = open("data/event.json")
    data = json.load(file)
    return data
data = load_event_data()
print(data)