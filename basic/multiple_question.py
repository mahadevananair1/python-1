from question import question

question_prompt = [
    "Penis size that woman love?\n(a) 7\n(b) 9\n(c) 10\n\n",
    "What is Python?\n(a) A Weed\n(b) Programming Language\n(c) Term to call a dick-head\n\n",
    "World most famous pornstar?\n(a) Mia Khalifa\n(b) Sunny Leone\n(c) Rachel Starr\n\n"


]

questions =[
    question(question_prompt[0], "b"),
    question(question_prompt[1], "b"),
    question(question_prompt[2], "b")
] 

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1 
        elif answer.isupper() == True == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")
run_test(questions)