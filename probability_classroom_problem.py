import math 

def birthday_problem(n):
  if n > 365:
    return 1.0 # Pigeonhole principle : must be at least one birthday
    numerator = math.factorial(365) # creating the factorial of 365
    denominator = math.factorial(365 - n) * (365 ** n)
    prob_no_shared = numerator/denominator # calculation the probabilities of no shared birthdays
    prob_shared = 1 - prob_no_shared# subtracting the probability of no shared birthdays from total probability (1)
    return prob_no_shared

for n in range (5,51,5):
  print(f"For a classroom of {n} people, there is a probability: {birthday_problem(n):.4f} of a shared birthday." )
 # print(f"{n} people: {birthday_problem(n):.4f} probability of shared birthday")
  
    
  
