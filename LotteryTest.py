#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 04:25:02 2021

@author: clarencechang
"""

# lottery game where number choices are between 1-49; your given a combination of 6 numbers to find
# your allowed up to 6 numbers for your inital purchase price, and a marginal increase per number 
# find the expected cost per marginal number (past six ), and the expected cost for the first six 
#allow the parameters of the game to be adjusted
import math
import random



choices_b = int(input("Beginning number " )) #First Number to Choose from
choices_l = int(input("Last Number ")) # Second Number (in this case 49)
numberofcomb = int(input("Number of numbers in a winning combination ")) 
Lottery_payout = int(input("Winning Amount ")) 
Simulations = int(input(" Simulations for Efficancy Testing")) # Amount of simulations to test expected cost

total_combinations = (math.factorial(choices_l)) / ((math.factorial(numberofcomb) * (math.factorial(choices_l - numberofcomb))))



price_total = Lottery_payout * (1/total_combinations)
price_per = price_total / numberofcomb

print (f"There is a total of {total_combinations} combinations, the efficient pricing per number is {price_per},\n a {numberofcomb} digit combination should cost {price_total}" )





        



# total_profits = 0
# cost =  price_total 

# for x in range(1,Simulations + 1 ):
#     count = 0
  
#     guess = []
#     guess_storage = []
#     key_store = random.sample(range(choices_b,choices_l + 1 ), numberofcomb )
 
 
  
    
#     while guess != key_store:
#         guess = random.sample(range(choices_b,choices_l + 1 ), numberofcomb )
#         if guess not in guess_storage:
#             count += 1
#             guess_storage.append(guess)
            

       
   
#     cost_sum = count * cost
 
#     profit = (Lottery_payout - cost_sum)
#     print(f' this is the current count {count}, cost_sum {cost_sum}')
    

#     if profit > cost:
#         print (f' the winning combination is {guess}, you paid {cost_sum} and made {profit}')
#         total_profits += profit
#     elif profit < cost:
#         print (f' the winning combination is {guess}, you paid {cost_sum} and lost {profit}')
#         total_profits += profit
#     else:
#         print (f' the winning combination is {guess}, you paid {cost_sum} and broke even')
        
#     print (f' total profit is {total_profits}')

# print (total_profits / Simulations) 
  