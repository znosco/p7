import csv
import itertools as it
import time

begin = time.time()


class Share:
    def __init__(self, name, price, benefit):
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
with open("partie1.csv", newline="") as share_file:
    share_file = csv.DictReader(share_file)
    for row in share_file:
        share = Share(row["shares"], float(row["prices"]), float(row["benefit"]))
        list_shares.append(share)

investor1 = Investor("toto", 400, 400, [])
investor2 = Investor("titi", 500, 500, [])
list_investors = [investor1, investor2]

list_shares = sorted(list_shares, key=lambda x: x.benefit, reverse=True)
for item in list_shares:
    print(item.benefit)


def profitability(bought_shares):
    all_benefit = 0
    for item in bought_shares:
        benefit = item.benefit * item.price / 100
        all_benefit += benefit
    return all_benefit


def investment(list_shares, investment):
    all_benefit = 0
    shares_in_box = []
    for i in range(1, len(list_shares) + 1):
        for combinations in it.combinations(list_shares, i):
            if sum(map(lambda item: item.price, combinations)) <= investment:
                profits = profitability(combinations)
                if profits > all_benefit:
                    all_benefit = profits
                    shares_in_box = combinations

    return shares_in_box


shares_in_box = investment(list_shares, investor2.investment)
end = time.time()
duration = end - begin
print("duration=", duration)
sum_price = 0
for item in shares_in_box:
    sum_price += item.price
sum_benefit = profitability(shares_in_box)
end = time.time()
duration = end - begin
print("somme dépensée = ", sum_price, "bénéfice = ", sum_benefit)
print("duration=", duration)
for item in shares_in_box:
    print(item.name)
file_save = open("bruteforce.txt", "w")
file_save.write(f"résultats pour le fichier: partie1.csv \n")
file_save.write(f"somme dépensée = {sum_price} bénéfice = {sum_benefit}\n")
file_save.write("actions achetées: \n")
for share in shares_in_box:
    file_save.write(f"{share.name}\n")
file_save.close()
