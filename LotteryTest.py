# lottery game where number choices are between 1-49; your given a combination of 6 numbers to find
# your allowed up to 6 numbers for your inital purchase price, and a marginal increase per number 
# find the expected cost per marginal number (past six ), and the expected cost for the first six 
#allow the parameters of the game to be adjusted
import math
import random
import sys 
import matplotlib.pyplot as plt
from itertools import count
from matplotlib.animation import FuncAnimation

sys.setrecursionlimit(10 ** 6)


choices_b = int(input("Beginning number " )) #First Number to Choose from
choices_l = int(input("Last Number ")) # Second Number (in this case 49)
numberofcomb = int(input("Number of numbers in a winning combination ")) 
Lottery_payout = int(input("Winning Amount ")) 
Simulations = int(input("Simulations for Efficancy Testing ")) # Amount of simulations to test expected cost
cost = int(input("Cost Per Ticket ")) # Cost per ticket to test efficancy 

total_combinations = (math.factorial(choices_l)) / ((math.factorial(numberofcomb) * (math.factorial(choices_l - numberofcomb))))



price_total = Lottery_payout * (1/total_combinations)
price_per = price_total / numberofcomb







        




def test(guess_storage):

  
    global key_store
    global sorted_key
 
    guess = random.sample(range(choices_b,choices_l + 1 ), numberofcomb )
    sorted_guess = sorted(guess)
    print(f'this is the guess {guess},\nthe key is {key_store},\nthe guess storage {guess_storage}')

     
       
        
    if sorted_guess != sorted_key:
        if sorted_guess not in guess_storage:
                guess_storage.append(sorted_guess)
                print (f'the current guess storage is {guess_storage}')
                test(guess_storage)
                
        else:
            test(guess_storage)
        
    
    
    if sorted_guess == sorted_key:
        print (f'the guess is {guess}')
        print (len(guess_storage) + 1)
        return len(guess_storage) + 1 
        
    return len(guess_storage ) + 1 
  

total_profit = 0
 
profit_vis = []
time_vis = []
counter = count()

for x in range(1,Simulations + 1 ):

    
    
    
    key_store = (random.sample(range(choices_b,choices_l + 1 ), numberofcomb ))
    sorted_key = sorted(key_store)
    
   
   
           
    
    cost_sum = test([]) * cost
    
         
    profit = (Lottery_payout - cost_sum)
        # print(f' this is the current count {count}, cost_sum {cost_sum}')
        

    time_vis.append(next(counter))
    profit_vis.append(profit)
    plt.plot(time_vis, profit_vis)
       
    plt.xlabel(" Time in Intervals of 1")
    plt.ylabel("Profit in Intervals of 1")
    
    total_profit += profit 
    average_cost = total_profit / Simulations 
        
        
    if profit > cost:
        print (f' you paid {cost_sum} and made {profit}')
          
    elif profit < cost:
        print (f' you paid {cost_sum} and lost {profit}')
            
    else:
        print (f' you paid {cost_sum} and broke even')
            
    print (f' total profit is {profit}')
    
    
    



# def Visual(data):
#       global profit 
# #     time_vis.append(next(counter))
#       profit_vis.append(profit)
# #     plt.plot(time_vis, profit_vis)
#       print (profit_vis)
# # Visualize = FuncAnimation(plt.gcf(), Visual, interval = 1000)
    
    
# Visual(profit)
    
print (f"There is a total of {total_combinations} combinations, the efficient pricing per number is {price_per},\n a {numberofcomb} digit combination should cost {price_total}, on {Simulations} simulations your total profit is {total_profit}, with an average cost of {average_cost}" )
