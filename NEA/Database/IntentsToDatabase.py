from NEA.Database.AppDatabase import db
from NEA.Database.DatabaseIDQueues import pattern_ID, response_ID, context_ID
def addData(tags,patterns,responses,context):
    pID = pattern_ID.getID()
    rID = response_ID.getID()
    cID = context_ID.getID()
    if tags == []:
        return
    else:
        db.insert('TaskIntents',(tags.pop(),pID,rID,cID))
        addDataArray('Pattern',pID,patterns.pop())
        addDataArray('Response',rID,responses.pop())
        addDataArray('Context',cID,context.pop())
        addData(tags,patterns,responses,context)

def addDataArray(table,ID,data):
    if data == []:
        return
    else:
        db.insert(table,(ID,data.pop()))
        addDataArray(table,ID,data)

tags = ['task', 'homework', 'homework_subject', 'homework_content', 'homework_confirm', 'options', 'noanswer', 'thanks', 'goodbye', 'feeling', 'greeting', 'greeting_response']
patterns = [['I want to add a task', 'new task', 'remind of this task please', 'Can you remind me for my meeting coming up?', 'add extra curricular', 'add task'], ['I want to add some homework', 'new homework', 'add hw', 'Can you store my homework?', 'add homework'], ['Maths', 'English', 'Science', 'Biology', 'Chemistry', 'Physics', 'Geography', 'History', 'RPE', 'Computer Science', 'CS', 'DT', 'PE', 'Music', 'Art', 'Drama', 'Politics', 'Economics', 'Spanish', 'French', 'Chinese', 'German', 'Latin', 'Greek'], ['Exercise', 'Test', 'Questions', '1 2 3 4 5 6 7 8 9 10', 'write an essay'], ['Next Tuesday', 'This Thursday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', '12/4/19'], ['What things can you help me with?', 'How you can be helpful?', 'What help you provide?', 'What do u do', 'What can you do?', 'How you could help me?'], [], ["You're a lifesaver", 'ty', 'Thx', 'Thanks for helping me', 'Awesome, thanks', "That's helpful", 'Thank you', 'Thanks'], ['cya', 'ttyl', 'bye have a nice day', 'Goodbye', 'See you later', 'Bye'], ['are you ok?', 'how r u doing?', 'how are you?'], ['Hi', 'Good Morning', 'How are you doing', 'Good day', 'Hello', 'Hola', 'Hey', 'Is anyone there?', 'hi how are you', 'Hi'], ['How about you?', 'How are you', 'Are you doing well?', 'How are you doing?', 'You alright?', 'How are you feeling']]
responses = [["name, details, date & time and let me know if it's a weekly thing pls", 'sure can you give me its name specific contents and when it is, oh also is it reoccuring everyweek?'], ['Cool, which subject?', 'Oke, subject?', 'Okay, which subject?', 'Subject?'], ['Okay! What was set?', 'Homework details pls', 'What was the homework?', 'Let me know what the homework is pls'], ["Ok, when's it due for?", 'Due date?'], ["Nice, I've recorded it!", 'Thanks its all set', "I've added it, I'll remind you when its due soon!"], ['I can help u with remembering what goes on in ur daily life: storing homework, extra curricular, oh I can also get the weather and lunch menu too!', 'I mean I help you manage your daily life, so u can use me as a homework diary or reminder I guess for any activities you do. I can also help w weather and lunch timetable :)'], ['Not sure I understand', 'Please give me more info', 'Tell me what that means?', "Don't really understand what that means...", 'Erm are you there?', "Sorry, can't understand you"], ['np', 'No problem', "You're welcome", "It's alright"], ['Talk to you later', 'Good luck at school', 'Have a nice day', 'See you!'], ["I'm good", 'a bit tired tbh', 'alright thanks', "I'm doing pretty good"], ['Hey', 'Hi, how are you doing?', "Hey what's up?", 'Hello, thanks for asking'], ["Yeah I'm not doing too bad thanks", "I'm feeling pretty good", "I'm alright I guess", "I'm good"]]
context = [[''], ['homework_suject'], ['homework_content'], ['homework_confirm'], [''], [''], [''], [''], [''], [''], [''], ['greeting']]

addData(tags,patterns,responses,context)
db.exit()
