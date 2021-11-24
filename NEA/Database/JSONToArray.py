import json
intents_file = open("../Chatbot/intents1.json").read()
intents = json.loads(intents_file)

tags = []
patterns = []
responses = []
context = []
for intent in intents['intents']:
    tags.append(intent['tag'])
    patterns.append(intent['patterns'])
    responses.append(intent['responses'])
    context.append(intent['context'])

print(tags)
print(patterns)
print(responses)
print(context)
