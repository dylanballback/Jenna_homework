from functions import checkword, guessinput
import random
import colors
import words

#hello
# Main Loop
if __name__ == '__main__':
  numguesses = []
  x = 0
  maxguesses = 5
  ans = random.choice(words.word_list)

  while x < maxguesses:
    usrguess = guessinput()
    output = checkword(usrguess, ans)
    numguesses.append(output + colors.PLAIN)
    print(colors.PLAIN + "\n".join(numguesses))
    
    if usrguess == ans:
      print(colors.PLAIN + "Congratulations You Won!\nThe word was: " + colors.GREEN + ans + colors.PLAIN)
      exit()
    x += 1
  print(colors.PLAIN + "Sorry you're out of guesses.\nThe answer was: " + colors.GREEN + ans + colors.PLAIN)