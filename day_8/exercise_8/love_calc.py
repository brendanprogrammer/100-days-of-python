'''
Love Calculator
💪 This is a difficult challenge! 💪 

You are going to write a function called calculate_love_score() that tests the compatibility between two names.  To work out the love score between two people: 

1. Take both people's names and check for the number of times the letters in the word TRUE occurs.   
2. Then check for the number of times the letters in the word LOVE occurs.   
3. Then combine these numbers to make a 2 digit number and print it out. 

e.g.

name1 = "Angela Yu" name2 = "Jack Bauer"

T occurs 0 times 

R occurs 1 time 

U occurs 2 times 

E occurs 2 times 

Total = 5 

L occurs 1 time 

O occurs 0 times 

V occurs 0 times 

E occurs 2 times 

Total = 3 

Love Score = 53

Example Input:
calculate_love_score("Kanye West", "Kim Kardashian")

Example Output: 42
'''

def calculate_love_score(name1, name2):
    # Combine the names to make one string
    combined_names = name1 + name2
    
    # Count the occurrences of each character in the strings 'TRUE' and 'LOVE'
    true_score = 0
    love_score = 0
    
    for letter in 'TRUE':
        true_score += combined_names.lower().count(letter.lower())
        
    for letter in 'LOVE':
        love_score += combined_names.lower().count(letter.lower())
    
    # Combine the scores into a two-digit number
    love_score = str(true_score) + str(love_score)
    
    # Print the result
    print(love_score)

# Call the function with hardcoded values
calculate_love_score("Kanye West", "Kim Kardashian")
