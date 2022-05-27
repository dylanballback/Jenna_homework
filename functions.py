import colors

def checkword(guess, answer):
  # Checks the guess against the answer 
  results = []

  for i, letter in enumerate(guess):
    if answer[i] == guess[i]:
      results.append(colors.GREEN)
    elif letter in answer:
      results.append(colors.YELLOW)
    else:
      results.append(colors.PLAIN + colors.UNDERLINE)
    results[i] = results[i] + guess[i]

  return (colors.PLAIN + " ").join(results)

def guessinput():
  # Gets user input and checks it's the right length
  guess = input(colors.PLAIN + "Enter your 5 Letter Guess:\n")

  while len(guess) != 5:
    guess = input(colors.PLAIN + "Sorry your guess isn't 5 Letters, please try again\n" + "Enter your 5 Letter Guess:\n")
  return guess.upper()
