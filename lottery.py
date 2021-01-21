import random
import sys
import numpy as np
#import `pyplot` from `matplotlib`
import matplotlib as mpl
mpl.use('tkagg')
import matplotlib.pyplot as plt



def computer_random():
    """let the computer create a list of 6 unique random integers from 1 to 37"""
    ci = random.sample(range(1,37), 6)
    return ci
    
def user_random():
    """let the user create a list of 6 unique random integers from 1 to 37"""
    print ("Enter 6 unique random integers from 1 to 50:")
    ui = []
    while len(ui) < 6:
        print (len(ui) + 1),
        try:
            i = int(input("--> "))
            print ("value",i)
            # check if i is unique and has a value from 1 to 50
            # and is an integer, otherwise don't append
            # if (i not in ui) and (1 <= i <= 50):
            ui.append(i)
        except:
            print ("Enter an integer number!")
    return ui

def match_lists(list1, list2):
    """to find the number of matching items in each list use sets"""
    set1 = set(list1)
    set2 = set(list2)
    # set3 contains all items comon to set1 and set2
    set3 = set1.intersection(set2)
    # return number of matching items
    return len(set3)
    
    
    
# the user picks the 6 winning numbers
user_list  = user_random()
#user_list = computer_random()
print ("Winning numbers:", user_list)

# set up counters for 3 to 6 matches
match3 = 0
match3List = []
match4 = 0
match4List = []
match5 = 0
match5List = []
match6 = 0
match6List = []

print()

# the computer picks the numbers for each ticket sold
# tickets_sold = 500
tickets_sold = 5000
print ("Go get a coffee :)  ...")
tickets = []
paid = tickets_sold*3
#quick = False True
quick = False
appendedBins  = [0] * 7
# retriesMax = 10000
retriesMax = 10
for k in range(tickets_sold):
    allow_max_match_count = 0
    #D print ("Calc ticket ...{0}".format(k))
    if quick:
        comp_list = computer_random()
        tickets.append(comp_list)
    else:
        shouldRun=True
        retries=0
        while shouldRun:
            # print("1")
            found=False
            comp_list = computer_random()
            #D print("Tickets len {0}".format(len(tickets)))
            for t in tickets:
                ####    print("comp_list:{0} VS t:{1}".format(comp_list,t))
                # print("tick")
                m = match_lists(comp_list, t)
                # print("tock")
                # print("Matches {0}".format(m))
                if m>allow_max_match_count and retries < retriesMax :
                    #D print(">try again")
                    found = True
                    retries+=1
                    break

                if m>allow_max_match_count and retries >= retriesMax :
                    allow_max_match_count+=1
                    # appendedBins[0]+=1
                    #D print("change to try {0}".format(allow_max_match_count))
                    if allow_max_match_count>=6:
                        allow_max_match_count=6
                    found = True
                    retries=0
                    break

            #D print("Done with tickets Found? {0}".format(found))       
            if found == False:
                shouldRun = False
                #D print("..adding..")
                appendedBins[allow_max_match_count]+=1
                tickets.append(comp_list)
    
    print(chr(27) + "[2J")
    print('\033c')
    print('\x1bc')
    print("=====> Tickets len {0} <=======".format(len(tickets)))
    print(appendedBins)
    matches = match_lists(comp_list, user_list)
    if matches == 3:
        match3List.append(comp_list)
        match3 += 1
    elif matches == 4:
        match4List.append(comp_list)
        match4 += 1
    elif matches == 5:
        match5List.append(comp_list)
        match5 += 1
    elif matches == 6:
        match6List.append(comp_list)    
        match6 += 1

    print ("Winning numbers:", user_list)
    print("3 > {0}".format(match3))
    print("4 > {0}".format(match4))
    print("5 > {0}".format(match5))
    print("6 > {0}".format(match6))

    won = match3*10+match4*100+match5*5000+match6*50000
    
    print("Out of {0}/{1} tickets".format(len(tickets),tickets_sold))
    print("You paid           {0}".format(paid))
    print("You Won So far     {0}".format(won))
    print("Revenue           {0}".format(won-paid))
    print()
    print()
    # print("=====___=======")
    # optional progress indicator
    #if k % 10 == 0:
    #    print (">"),
    
print(); print()

with open('tickets.txt', 'w') as f:
    for t in tickets:
        print("{0}".format(t), file=f)

print ("-------------3------------------")
if match3>0:
    print(match3List)

print ("-------------4------------------")
if match4>0:
    print(match4List)

print ("-------------5------------------")
if match5>0:
    print(match5List)

print ("-------------6------------------")
if match6>0:
    print(match6List)


print ("Winning numbers:", user_list)

print ("Out of %d tickets sold the computer found these matches:" % tickets_sold)
print("You paid {0}".format(paid))
print("You Won {0}".format(match3*10+match4*100+match5*5000+match6*50000))
print("Revenue {0}".format(won-paid))
"""
3 matching numbers = $10
4 matching numbers = $100
5 matching numbers = $5,000
6 matching numbers = $500,000
"""
print("3 matches = {0} which is $10*{0}={1} ".format(match3,match3*10))
print("4 matches = {0} which is $100*{0}={1} ".format(match4,match4*100))
print("5 matches = {0} which is $5000*{0}={1} ".format(match5,match5*5000))
print("6 matches = {0} which is $500000*{0}={1} ".format(match6,match6*500000))




buckets = [0] * 37
for t in tickets:
    for n in t:
       buckets [n]+=1

# Initialize the plot
fig = plt.figure(figsize=(15,15))
ax1 = fig.add_subplot(121)
print(appendedBins)
# appendedBins
# rects2 = ax1.bar(list(range(0,37)),buckets)
rects2 = ax1.bar(list(range(0,7)),appendedBins)
def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax1.text(rect.get_x() + rect.get_width()/2., 1.01*height,
                '%d' % int(height),
                ha='center', va='bottom')

autolabel(rects2)
# Show the plot
plt.show()