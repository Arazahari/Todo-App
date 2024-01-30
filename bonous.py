import json
with open('questions.json','r') as file:
    content = file.read()


data = json.loads(content)
print(data)

score = 0
for question in data:
    print(question['question_text'])
    for index, alternative in enumerate(question['alternatives']):
        print(index+1,"-",alternative)
    user_choice = int(input('Enter your answer: '))
    question["user_choice"] = user_choice


for index, question in enumerate(data) :
    if question["user_choice"] == question["correct answer"]:
        score += 1
        result = 'correct answer'
    else:
        result = 'wrong answer'
    message = f"{result} {index+1} - Your answer:{question['user_choice']}, correct answer is :{question['correct answer']}"
    print(message)
print('Your score:',score,"/",len(data))