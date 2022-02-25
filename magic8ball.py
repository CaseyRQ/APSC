#!/usr/bin/env python3
import random

def magicball(): 
        question = (input("Ask a yes or no question. To quit, type quit:\n"))
        answers = [
            "Yes", 
            "No",
            "Maybe",
            "Very doubtful",
            "Ask again later",
            "Definetly",
            "Cannot predict now",
            "Most likely"]
        if question.lower() == "quit":
            print ("Goodbye.")
        else:
            question != "How" or "Why"
            print(random.choice(answers))
   
        
magicball()