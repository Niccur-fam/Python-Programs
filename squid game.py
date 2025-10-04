import random

quiz_questions =[
    {
        "question": "Whats the output of print(2 ** 3)?",
        "options": ["5", "6", "8", "9"],
        "answer": "8"
            
    },
    
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["func", "def", "function", "define"],
        "answer": "def"
    },
    
    {
        "question": "What data type is the result of 3 / 2 in Python 3?",
        "options": ["int", "float", "str", "bool"],
        "answer": "float"
    },
    
    
    {
        "question": "Which of the following is a mutable data type in Python?",
        "options": ["tuple", "list", "string", "int"],
        "answer": "list"
    },
    
    
    {
        "question": "What does the len() function do in Python?",
        "options": ["Returns the length of an object", "Converts a value to an integer", "Prints output to the console", "Creates a new list"],
        "answer": "Returns the length of an object"
        
    },
    
]
    
jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why did the Python developer go broke? Because he couldn't 'tuple' his money!",
    "Why did the computer show up at work late? It had a hard drive!",
    "I would tell you a UDP joke... but you might not get it.",
    
    
]

def run_quiz():
    print("\n Welcome to the Python & Fun Quiz! \n")
    score = 0
    
    for idx, q in enumerate(quiz_questions, 1):
        print(f"Q{idx }: {q['question']}")
        for i, option in enumerate(q['options'],1):
            print(f"  {i}. {option}")
        
        try:
         choice=int(input("Your answer (1-4):"))
         if q['options'][choice - 1] == q['answer']:
                print("✅ Correct!\n")
                score += 1
        
        
         else:
            print(f"Wrong! The correct answer is: {q['answer']}\n")
        
        except (ValueError, IndexError):
            print("⚠️ Invalid choice. Moving to next question.\n")

    print(f"🏁 Quiz complete! Your score: {score} out of {len(quiz_questions)} 🏆")
        
def tell_joke():
            print("\n here's a joke for you:\n")
            print(random.choice(jokes))
            print()
        
def main():
            while True:
                print("\n What would you like to do? \n")
                print("1. Take the Quiz")
                print("2. Hear a Joke")
                print("3. Exit")
                
                choice = input("Enter your choice (1-3): ")
                if choice == '1':
                    run_quiz()
                elif choice == '2':
                    tell_joke()
                elif choice == '3':
                    print("Thanks for playing! Goodbye!")
                    break
                
                else:
                    print("⚠️ Invalid choice. Please try again.")
                    
                   
                   
                   
                   
if __name__ == "__main__":
  main()
                
            
        
        
        
        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
