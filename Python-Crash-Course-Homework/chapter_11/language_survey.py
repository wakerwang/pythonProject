# coding:utf-8
from survey import AnonymousSurvey

question = "What language did you first learn to speak?"

my_survey = AnonymousSurvey(question)

my_survey.show_question()

print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language:")
    if response.lower() == 'q':
        break
    my_survey.store_response(response)

print("-----------")
my_survey.show_results()

