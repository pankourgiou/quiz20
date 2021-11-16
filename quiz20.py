import random

class QA:
  def __init__(self, question, correctAnswer, otherAnswers):
    self.question = question
    self.corrAnsw = correctAnswer
    self.otherAnsw = otherAnswers

qaList = [QA("Who wrote the book Klara and the sun?", "Kazuo Ishiguro", ["Karl Marx", "Klimt"]),
QA("Who wrote the book Valis?", "Phillip K. Dick", ["Kazuo Ishiguro", "Karl Marx", "Tolstoy"]),
QA("Who wrote the book In search of Lost time?", "Marcel Proust", ["Tolstoy", "Fyodor Dostoyevsky", "Nikolai Gogol"]),
QA("Who wrote the book Tribulation of a chinaman in China?", "Jules Vern", ["Marcel Proust", "Philip K. Dick"]),
QA("Who wrote the book The girl with the dragon tatoo?", "Stieg Larsson", ["J.R.R. Tolkien", "Alber Kamy", "Arne Dahl", "Jules Vern"])]

corrCount = 0
random.shuffle(qaList)
for qaItem in qaList:
  print(qaItem.question)
  print("Possible answers are:")
  possible = qaItem.otherAnsw + [qaItem.corrAnsw] # square brackets turn correct answer into list for concatenating with other list
  random.shuffle(possible)
  count = 0 # list indexes start at 0 in python
  while count < len(possible):
    print(str(count+1) + ": " + possible[count])
    count += 1
  print("Please enter the number of your answer:")
  userAnsw = input()
  while not userAnsw.isdigit():
    print("That was not a number. Please enter the number of your answer:")
    userAnsw = input()
  userAnsw = int(userAnsw)
  while not (userAnsw > 0 and userAnsw <= len(possible)):
    print("That number doesn't correspond to any answer. Please enter the number of your answer:")
    userAnsw = input()
  if possible[userAnsw-1] == qaItem.corrAnsw:
    print("Your answer was correct.")
    corrCount += 1
  else:
    print("Your answer was wrong.")
    print("Correct answer was: " + qaItem.corrAnsw)
  print("")

print("You answered " + str(corrCount) + " of " + str(len(qaList)) + " questions correctly.")
