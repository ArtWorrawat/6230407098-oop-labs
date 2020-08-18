guess = 2
answer = "kku"
while guess >= 0:
  word = input("Enter a word:")
  if word == answer:
    print("Congrats that you can guess the secret word correctly")
    break
  else:
    print("Incorrect! You have %d guesses left" %guess)
    guess -= 1
if guess == -1:
  print("Thanks for trying, but the secret word is actually", answer)
