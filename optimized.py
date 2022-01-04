import csv
import itertools as it
import time

begin = time.time()
class Share:
    def __init__(self,name,price,benefit):
        self.name = name
        self.price = price
        self.benefit = benefit

class Investor:
  def __init__(self, name, investment, money_left, bought_shares):
        self.name = name
        self.investment = investment
        self.money_left = money_left
        self.bought_shares = bought_shares

list_shares = []
with open('dataset1.csv', newline='') as share_file:
    share_file = csv.DictReader(share_file)
    for row in share_file:
        if float(row['benefit']) > 0 and float(row['prices']) < 100:
            share = Share(row['shares'], float(row['prices']), float(row['benefit']))
            list_shares.append(share)
print("longueur:",len(list_shares))

investor1 = Investor("toto",400,400,[])  
investor2 = Investor("titi",500,500,[])  
list_investors = [investor1,investor2]

list_shares = sorted(list_shares, key=lambda x: x.benefit, reverse=True)
list_shares = list_shares[0:20]

for item in list_shares:
    print (item.benefit)
"""
def investment(investor):
    for share in list_shares:
        if share in investor.bought_shares:
            pass
        elif share.price > investor.money_left:
            pass
        else:
            investor.bought_shares.append(share)
            investor.money_left -= share.price

for investisor in list_investors:
    investment(investisor)
    for item in investisor.bought_shares:
        #print(investisor.bought_shares)
        print(profitability(investisor.bought_shares))

#profitability(investisor.bought_shares)
"""

def profitability(bought_shares):
    all_benefit = 0
    for item in bought_shares:
        benefit = item.benefit*item.price/100
        all_benefit += benefit
    return all_benefit


def investment(list_shares,investment):
    all_benefit = 0
    shares_in_box = []
    for i in range(1,len(list_shares)+1):
        for combinations in it.combinations(list_shares,i):
            if sum(map(lambda item: item.price,combinations)) <= investment:
                profits = profitability(combinations)
                if profits > all_benefit:
                    all_benefit = profits
                    shares_in_box = combinations
                
    return shares_in_box

a = investment(list_shares,investor2.investment)
print(len(a))
print(profitability(a))
for i in range(len(a)):
    print(a[i].name)

end = time.time()
duration = end - begin

sum = 0
for item in a:
    sum += item.price

print("somme = ", sum)    
print("duration=",duration)








            








    


