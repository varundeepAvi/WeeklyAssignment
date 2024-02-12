# -*- coding: utf-8 -*-
"""WeeklyAssign2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZoxWo55sQpCQktHwfivHZy6iIM6rR95h
"""

import random

game_rules = ''' There are 2 Question sections in this game
1. Section A is of MCQ , correct ans will get Score 1 whereas wrong ans
   has negative marking of 0.25
2. Section B is of One Word Substition.
   There is not negative marking in One Word Substitution

   "Best of Luck"
'''
mcq_quiz = {}
ows_quiz = {}
class Question:
   def __init__(self, number ,q_type ,statement, options = None , answer = None ):
     self.number = number
     self.q_type = q_type
     self.statement = statement
     self.options = options
     self.answer = answer

def parse_question(line):
   parts = line.strip().split('|')
   number =parts[0]
   q_type = parts[1]
   statement =  parts[2]
   if  q_type == 'mcq':
      options = parts[3:7]
      answers = parts[7].strip('#')
      return Question(number, q_type, statement, options, answers)
   elif q_type =='one word':
      answers = parts[3].strip('#')
      return Question(number, q_type, statement, answer = answers)



def read_questions_from_file(filename):
    questions = []
    with open(filename, 'r') as file:
       for line  in file:
         if '|'  in line:
               question = parse_question(line)
               questions.append(question)

    return questions



def create_quiz(questions):
   global mcq_quiz
   global ows_quiz

   for question in questions:
      if question.q_type == 'mcq':
       mcq_quiz[question.number] = question
      else :
       ows_quiz[question.number] = question





def ask_question(question):
  print(question.statement)
  if question.q_type == 'mcq':
     print("Options:")

     for i , option  in enumerate(question.options, start = 97):
        print(f'{chr(i)}.{option}')

  user_answer =input("Your Answer: ").strip().lower()
  return user_answer == question.answer.lower()


def main():

   print("Quiz Game :")
   print("Game Rules:-")
   print("Thr")

   filename = '/content/textfile.txt'
   questions = read_questions_from_file(filename)

   create_quiz(questions)
   random_questions_mcq = list(mcq_quiz.values())
   random_questions_ows = list(ows_quiz.values())

   random.shuffle(random_questions_mcq)
   random.shuffle(random_questions_ows)


   total_questions_mcq = len(random_questions_mcq)
   total_questions_ows = len(random_questions_ows)

   print(game_rules)
   correct_answers_mcq = 0
   i = 1
   for question in random_questions_mcq:
      print(f'{i}.')
      i += 1

      if  ask_question(question):
       print("Original Ans is ", question.answer)
       print("Correct")
       correct_answers_mcq += 1
      else :
        print("Original Ans is ", question.answer)
        print("Incorrect.")
      print()

   correct_answers_ows = 0
   i =1
   for question in random_questions_ows:
      print(f'{i}.')
      i += 1

      if  ask_question(question):
       print("Correct Ans is ", question.answer)

       print("Correct")
       correct_answers_ows += 1
      else :
       print("Correct Ans is ", question.answer)

       print("Incorrect.")
      print()

   total_score= 0
   print("Score Card:- ")
   print(   "Your Marks list  in MCQ ")
   print("     Your Correct Answers : ", correct_answers_mcq)
   print("     Your Incorrect Answers :  ", 15- correct_answers_mcq)
   total_score = correct_answers_mcq - (15- correct_answers_mcq) * 0.25
   print(   "Marks in MCQ after Negative Marking Reduction is: ", total_score )

   print(" Your Marks in One Word Substitution: ", correct_answers_ows)
   total_score =  total_score + correct_answers_ows
   print("Total Score is : ", total_score)





   print(  f'You Scored{ total_score} out of {len(questions)}.')


if __name__ == "__main__":
    main()

