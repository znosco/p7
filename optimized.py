import csv
import itertools as it
import time


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
choice = input("taper 1 ou 2 pour utiliser le fichier1 ou le fichier2")
choice =int(choice)
if choice ==1:
    file_choice = 'dataset1.csv'
if choice ==2:
    file_choice = 'dataset2.csv'
    
begin = time.time()
with open(file_choice, newline='') as share_file:
    share_file = csv.DictReader(share_file)
    for row in share_file:
        if float(row['benefit']) > 0 and float(row['prices']) < 100 and float(row['prices'])>0 :
            share = Share(row['shares'], float(row['prices']), float(row['benefit']))
            list_shares.append(share)
print("longueur:",len(list_shares))

investor1 = Investor("toto",400,400,[])  
investor2 = Investor("titi",500,500,[])  
list_investors = [investor1, investor2]

list_shares = sorted(list_shares, key=lambda x: x.benefit, reverse=True)
list_shares = list_shares[0:100]

print("premier action", list_shares[0].price,list_shares[0].benefit )

"""
for item in list_shares:
    print (item.benefit)

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
        print(investisor.bought_shares)
        print(profitability(investisor.bought_shares))

profitability(investisor.bought_shares)
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

shares_in_box =[]
def take_best_shares(list_shares,money_spend):
    money = money_spend
    for i in range(len(list_shares)):
        if money - list_shares[i].price> 0:
            shares_in_box.append(list_shares[i])
            money -= list_shares[i].price
    return 200 + money


money_left = take_best_shares(list_shares,300)
begin_list = len(shares_in_box)
shares_following = list_shares[begin_list-1:begin_list+14]
shares_in_box_following = investment(shares_following,money_left)
shares_in_box += shares_in_box_following


sum_price = 0
for item in shares_in_box:
    sum_price += item.price
sum_benefit = profitability(shares_in_box)
    
end = time.time()
duration = end - begin

print("somme dépensée = ", sum_price, "bénéfice = ",sum_benefit)    
print("duration=", duration)