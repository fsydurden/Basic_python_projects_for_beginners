import random

name = "Coder"
question = "Is this a shitty code"
answer = ""
random_number = random.randint(1,9)
#print(random_number)

if random_number == 1:
  answer = "Yes - definitel"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
else:
  print("shutttt upppp you nigaaaa")



if question == "":
  print("ask something you little shit!")
else:
  if name == "":
    print(f"Question: {question}?")
    print(f"Magic 8-Balls answer: {answer}")
  else:
    print(f"{name} asks: {question}?")
    print(f"Magic 8-Balls answer: {answer}")
