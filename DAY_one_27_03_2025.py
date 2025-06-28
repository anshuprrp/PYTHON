print("Anshu kumar\n")
# print("Anshu kumar")
import pyttsx3

engine = pyttsx3.init()

engine.setProperty('rate', 150)  
engine.setProperty('volume', 0.9) 


engine.say(''' tell me the carecte of good programmer 

A good programmer possesses a combination of technical skills and personal qualities that enable them to write efficient, maintainable, and high-quality code. Here are the key characteristics:
1. Strong Problem-Solving Skills
    • Ability to break down complex problems into smaller, manageable parts. 
    • Thinks logically and finds the most efficient solution. 
2. Good Knowledge of Algorithms & Data Structures
    • Understands sorting, searching, recursion, and dynamic programming. 
    • Uses the right data structures (arrays, lists, trees, graphs, etc.) for efficiency. 
3. Writes Clean & Readable Code
    • Uses meaningful variable and function names. 
    • Follows proper indentation and formatting. 
    • Avoids unnecessary complexity in the code. 
4. Strong Debugging & Testing Skills
    • Uses debugging tools and techniques effectively. 
    • Writes unit tests to ensure code correctness. 
    • Identifies and fixes bugs efficiently. 
5. Quick Learning Ability
    • Adapts to new programming languages and technologies. 
    • Stays updated with the latest industry trends. 
6. Good Communication Skills
    • Explains technical concepts clearly to team members. 
    • Writes proper documentation for the code. 
7. Patience & Persistence
    • Doesn't give up easily when facing coding challenges. 
    • Keeps improving the code until it is optimized and error-free. 
8. Follows Best Practices & Coding Standards
    • Uses version control (e.g., Git) for code management. 
    • Writes modular and reusable code. 
    • Follows SOLID principles and design patterns. 
9. Teamwork & Collaboration
    • Works well with other developers, testers, and designers. 
    • Participates in code reviews and accepts feedback positively. 
10. Passion for Coding
    • Enjoys learning new programming concepts. 
    • Contributes to open-source projects or personal projects. 
A good programmer is not just about writing code but also about thinking critically, learning continuously, and working well in a team. Would you like tips on improving your programming skills? 😊

''')


engine.runAndWait()