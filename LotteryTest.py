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
import sys 

sys.setrecursionlimit(1500)


choices_b = int(input("Beginning number " )) #First Number to Choose from
choices_l = int(input("Last Number ")) # Second Number (in this case 49)
numberofcomb = int(input("Number of numbers in a winning combination ")) 
Lottery_payout = int(input("Winning Amount ")) 
Simulations = int(input(" Simulations for Efficancy Testing ")) # Amount of simulations to test expected cost

total_combinations = (math.factorial(choices_l)) / ((math.factorial(numberofcomb) * (math.factorial(choices_l - numberofcomb))))



price_total = Lottery_payout * (1/total_combinations)
price_per = price_total / numberofcomb







        

guess_storage = []
count = 1
key_store = (random.sample(range(choices_b,choices_l + 1 ), numberofcomb ))
sorted_key = sorted(key_store)

def test(storage):
    global count 
    global guess_storage
    global key_store
 
    guess = random.sample(range(choices_b,choices_l + 1 ), numberofcomb )
    sorted_guess = sorted(guess)
    print(f'this is the guess {guess}, the count {count},\nthe key is {key_store},\nthe current guess storage is {guess_storage}')

    sorted_key = sorted(key_store)
    
     
       
        
    if sorted_guess != sorted_key:
        if sorted_guess not in guess_storage:
                guess_storage.append(sorted_guess)
                count += 1
                test(guess_storage)
        else:
            pass
    return (count)

 

for x in range(1,Simulations + 1 ):

    cost =  price_total  #adjust for winning odds 
    count = test(guess_storage)
           
    cost_sum = count * cost
         
    profit = (Lottery_payout - cost_sum)
        # print(f' this is the current count {count}, cost_sum {cost_sum}')
        
        
    if profit > cost:
        print (f' you paid {cost_sum} and made {profit}')
          
    elif profit < cost:
        print (f' you paid {cost_sum} and lost {profit}')
            
    else:
        print (f' you paid {cost_sum} and broke even')
            
    print (f' total profit is {profit}')
    
print (f"There is a total of {total_combinations} combinations, the efficient pricing per number is {price_per},\n a {numberofcomb} digit combination should cost {price_total} \n " )

  