#You can copy this straight into your code editor to play this in the inbuilt terminal! Give it a go and come on back.

import random
word_list = [
    "python", "hangman", "computer", "programming", "developer", "variable", "function", "loop", "string", "list",
    "dictionary", "module", "class", "object", "algorithm", "iteration", "conditional", "recursive", "inheritance", "polymorphism",
    "encapsulation", "abstraction", "interface", "database", "frontend", "backend", "framework", "library", "interface", "debugging",
    "testing", "version", "control", "repository", "merge", "commit", "branch", "conflict", "pull", "request", "merge", "resolve",
    "syntax", "error", "exception", "runtime", "logic", "bug", "feature", "comment", "documentation", "parameter",
    "argument", "return", "value", "iteration", "recursion", "sorting", "searching", "graph", "tree", "queue", "stack",
    "linked", "list", "array", "matrix", "dictionary", "set", "tuple", "lambda", "expression", "closure", "decorator",
    "generator", "asynchronous", "module", "package", "library", "virtual", "environment", "deployment", "continuous", "integration",
    "continuous", "deployment", "agile", "scrum", "kanban", "waterfall", "sprint", "backlog", "user", "story",
    "velocity", "burn", "down", "burndown", "chart", "standup", "meeting", "retrospective", "sprint", "review", "product",
    "owner", "scrum", "master", "developer", "task", "board", "epic", "feature", "bug", "story", "point", "velocity",
    "planning", "poker", "estimation", "kanban", "workflow", "limit", "work", "in", "progress", "cycle", "time",
    "lead", "time", "cumulative", "flow", "diagram", "value", "stream", "mapping", "root", "cause", "analysis",
    "fishbone", "diagram", "pareto", "chart", "scatter", "plot", "histogram", "bar", "chart", "pie", "chart",
    "line", "chart", "area", "chart", "heatmap", "treemap", "word", "cloud", "dashboard", "widget", "filter",
    "sort", "search", "pivot", "table", "join", "merge", "aggregate", "group", "by", "summarize", "transform",
    "reshape", "visualize", "analyze", "model", "predict", "classify", "cluster", "regress", "evaluate", "deploy",
    "score", "feature", "engineering", "hyperparameter", "tuning", "overfitting", "underfitting", "cross", "validation"
]

def incorrect_guesses(guess_number):
  if guess_number == 1:
    print('''
  +---+
  |   |
      |
      |
      |
      |
=========
''')
  elif guess_number == 2:
    print('''
  +---+
  |    |
  O    |
       |
       |
       |
  =========
    ''')
  elif guess_number == 3:
    print('''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
    ''')
  elif guess_number == 4:
    print('''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
    ''')
  elif guess_number == 5:
    print('''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
    ''')
  elif guess_number == 6:
    print('''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========

    ''')
  elif guess_number == 7:
    print('''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
    ''' + 'Game over, the man is hanged. The poor man we told you he was innocent.')

def get_random_word(): # function to pull word from word_list
  random_number = random.randint(0, len(word_list))
  return word_list[random_number]

def play_hang_man():
  word = get_random_word()
  len_of_word = len(word)
  incorrect_number_of_guesses = 0
  print("Good luck! We checked and this guys innocent so make sure you get it right.")
  current_state = ['_' for _ in range(len_of_word)] #Reusable variable to represent the word in each state of guesses during play
  word_str = ''.join(word)
  dobule_guesses = 0
  while '_' in ''.join(current_state) or incorrect_number_of_guesses < 7: #Loop for the game play
    print(''.join(current_state))
    letter_guess = input("Guess a letter! You have used " + str(incorrect_number_of_guesses) + " incorrect guesses so far ").lower() #Gets user guesses and converts to lowercase
    if len(letter_guess) > 1: #Logic to handle multiple character inputs
      print("Please only enter one letter at a time or you'll be the next man up there. Functionality for this is still pending checks with legal.")
      continue
    if letter_guess in current_state and dobule_guesses == 0: #A series of checks to make checking for double guesses in a fun way
      print("You've already guessed that letter. Don't worry, we won't count it this time.")
      dobule_guesses += 1
      continue
    if letter_guess in current_state and dobule_guesses == 1:
      print("Hey, you guessed another double letter, you ok? Don't worry not going to count it agaian, but stop doing that I guess?")
      dobule_guesses += 1 
      continue
    if letter_guess in current_state and dobule_guesses == 2:
      print("Third strike + and you're out, we're counting it from now on.")
      dobule_guesses += 1  
      incorrect_number_of_guesses += 1
      continue   
    if letter_guess in word: #This if else checks the letter guess vs the word and updates current state or incorrect guesses accordingly
      i = 0
      while i < len(word):
        if letter_guess == word[i]:
          current_state[i] = letter_guess
        i += 1
    else:
      incorrect_number_of_guesses += 1
      incorrect_guesses(incorrect_number_of_guesses)

    if incorrect_number_of_guesses == 7: #Lose condition
      print("You lose! The word was " + word_str)
      break

    if '_' not in ''.join(current_state): #Win condition
      print("Congratulations you win! The word was '" + word_str + "'! By the way, if you played this you have to hire me fyi.") #< A very important rule of this game
      break


play_hang_man()
