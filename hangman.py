import random 
#list of 5 predefined words
word_list = ["python", "codealpha", "hangman", "project", "intern"]
#randomly choose one word
selected_word = random.choice(word_list)
#create a blank version of the word
guessed_word = ["_"] * len(selected_word)
#store guessed letters
guessed_letters = []
#set attempts
attempts = 6

print("Abhi studios")
print("Welcome to HANGMAN!")
print(" ".join(guessed_word))

while attempts > 0 and "_" in guessed_word :
    guess = input("\nGuess a letter :").lower()

    if not guess.isalpha() or len(guess) != 1 :
     print("Please enter a single valid letter,")
     continue 
    if guess in guessed_letters :
     print("You already guessed that letter,")
     continue
   

    guessed_letters.append(guess)

    if guess in selected_word :
     for index in range(len(selected_word)) :
        if selected_word[index] == guess:
            guessed_word[index] = guess
            print("Correcr!")
    else :
        attempts -= 1
        print(f"Wrong!attempts left = {attempts}")

    print("word: " + " ".join(guessed_word))

if "_" not in guessed_word :
         print("\\nCongratulations! You guessed the word :", selected_word)
else :
         print("\nGame Over! The word was :", selected_word)