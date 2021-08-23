# lottery game where number choices are between 1-49; your given a combination of 6 numbers to find
# your allowed up to 6 numbers for your inital purchase price, and a marginal increase per number 
# find the expected cost per marginal number (past six ), and the expected cost for the first six 
# allow the parameters of the game to be adjusted
# this game is conditioned on memorization of previous guesses - efficient prices are not currently adjusted for such 
import math
import random
import sys 
import matplotlib.pyplot as plt

from matplotlib.animation import FuncAnimation

sys.setrecursionlimit(10 ** 6)


choices_b = int(input("Beginning number " )) #First Number to Choose from
choices_l = int(input("Last Number ")) # Second Number (in this case 49)
numberofcomb = int(input("Number of numbers in a winning combination ")) 
Lottery_payout = int(input("Winning Amount ")) 
Simulations = int(input("Simulations for Efficancy Testing ")) # Amount of simulations to test expected cost
Average_simulation = int(input("Number of Simulations taken per for total profit ")) # Keeps track of total profit per average simulation
cost = float(input("Cost Per Ticket ")) # Cost per ticket to test efficancy 
memory_cost = str(input("Would you like to not pool? T/F ")) # Adjusts price for multi guessing cost



total_combinations = (math.factorial(choices_l)) / ((math.factorial(numberofcomb) * (math.factorial(choices_l - numberofcomb))))






def test(guess_storage):

  
    global key_store
    global sorted_key
 
    guess = random.sample(range(choices_b,choices_l + 1 ), numberofcomb )
    sorted_guess = sorted(guess)
    print(f'this is the guess {guess},\nthe key is {key_store},\nthe guess storage {guess_storage}')

     
    if sorted_guess == sorted_key:
        print (f'the guess is {guess}')
        print (len(guess_storage) + 1)
        return len(guess_storage) + 1
       
        
    if sorted_guess != sorted_key:
        
        if memory_cost == "T": #currenty bugged runs regardless of bool value
                guess_storage.append(sorted_guess)
                print(f'the current guess storage is {guess_storage} (memmoryless)')
                test(guess_storage)
                
        if sorted_guess not in guess_storage:
                guess_storage.append(sorted_guess)
                print (f'the current guess storage is {guess_storage}')
                test(guess_storage)
                
        
                
        
        
    
    
   
        
    return len(guess_storage ) + 1 
  


 
profit_vis = []
time_vis = []
simulation_count = 0
profit_static = []


total_profit = 0
price_total = Lottery_payout * (1/total_combinations) 
price_per = price_total / numberofcomb
#condmemory_price = Lottery_payout * (1/total_combinations - simulation_count)




for x in range(1,Simulations + 1 ):
   
   
    simulation_count += 1
    
    
    
    key_store = (random.sample(range(choices_b,choices_l + 1 ), numberofcomb ))
    sorted_key = sorted(key_store)
    
   
   
    
    
    cost_sum = test([]) * cost
    
         
    profit = (Lottery_payout - cost_sum)
        # print(f' this is the current count {count}, cost_sum {cost_sum}')
    
    total_profit += profit 
    
    
    average_costcurrent = total_profit / x
    
    
    
    
    
    
    
    profit_vis.append(total_profit)
        
    
        
    profit_static.append(average_costcurrent)
    
    
    
   # to make a live graph you would have to store data through a csv file and then funnel it through a funcanimation from matplot *** 
   
    Average_profitline, = plt.plot(profit_static, label =" Average Profit")
    Total_profitline, =  plt.plot(profit_vis, label = "Total Profit")
    
 
    plt.legend([Average_profitline, Total_profitline], ['Average Profit', 'Total Profit'])
    
 
    
    plt.xlabel("Simulations ")
    plt.ylabel("Total Profit per simulation ")
    

    
        
 
        
    if profit > cost:
        print (f' you paid {cost_sum} and made {profit}')
          
    elif profit < cost:
        print (f' you paid {cost_sum} and lost {profit}')
            
    else:
        print (f' you paid {cost_sum} and broke even')
            
    print (f' total profit is {profit}')
    
    
    

average_cost = total_profit / Simulations

# 
print (f"There is a total of {total_combinations} combinations, the efficient pricing per number is {price_per},\n a {numberofcomb} digit combination should cost {price_total}, on {Simulations} simulations your total profit is {total_profit}, with an average cost/profit of {average_cost}" )
