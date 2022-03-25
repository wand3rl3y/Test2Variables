import random

lucky_number = random.randint(1,100)
fortune_number = random.randint(1,3)
fortune_text = ""

if fortune_number == 1:
  fortune_text = "A beautiful, smart, and loving person   will be coming into your life"
if fortune_number == 2:
  fortune_text ="A fresh start will put you on your way."
if fortune_number == 3:
  fortune_text = "A faithful friend is a strong defense"

print(f"{fortune_text} Luck number is: {lucky_number}")

