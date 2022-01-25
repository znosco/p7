import csv
import itertools as it
import time
import psutil


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


class Analyses:
    def __init__(self, number_share=0, gain=0, time_spend=0, memory=0):
        self.number_share = number_share
        self.gain = gain
        self.time_spend = time_spend
        self.memory = memory


list_shares = []
with open("dataset1.csv", newline="") as share_file:
    share_file = csv.DictReader(share_file)
    for row in share_file:
        if float(row["benefit"]) > 0 and float(row["prices"]) > 0:
            share = Share(row["shares"], float(row["prices"]), float(row["benefit"]))
            list_shares.append(share)

investor1 = Investor("toto", 500, 500, [])


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


# analyse bruteforce.py
n = 0
analyses_list = []
for n in range(24):
    begin = time.time()
    list_shares = sorted(list_shares, key=lambda x: x.benefit, reverse=True)
    list_shares_cut = list_shares[0 : n + 2]
    shares_in_box = investment(list_shares_cut, investor1.investment)
    analyses = Analyses()
    analyses.gain = profitability(shares_in_box)
    analyses.number_share = len(list_shares_cut)
    end = time.time()
    duration = end - begin
    analyses.time_spend = duration
    analyses.memory = psutil.virtual_memory().percent
    analyses_list.append(analyses)
    print()
    print("analyses du programme bruteforce")
    print("nombre d'actions: ", analyses.number_share)
    print("durée: ", analyses.time_spend)

header = ["number_share", "gain", "time_spend", "memory"]
units = ["no unit", "euros", "seconds", "%"]

with open("analyses_forcebrute.csv", "w") as fichier_csv:
    var = csv.writer(fichier_csv, delimiter=",")
    var.writerow(header)
    var.writerow(units)
    for item in analyses_list:
        var.writerow([item.number_share, item.gain, item.time_spend, item.memory])

print()
print("résumer des analyses du programme forcebrute")
for item in analyses_list:
    print("nombre d'actions: ", item.number_share)
    print("durée: ", item.time_spend)
    print("mémoire utilisée: ", item.memory, "%/n")


def take_best_shares(list_shares_cut, money_spend):
    money = money_spend
    for i in range(len(list_shares_cut)):
        if money - list_shares_cut[i].price > 0:
            shares_in_box.append(list_shares_cut[i])
            money -= list_shares_cut[i].price
        else:
            break
    return 200 + money


n = 0
analyses_list = []
for n in range(10):
    begin = time.time()
    list_shares = sorted(list_shares, key=lambda x: x.benefit, reverse=True)
    list_shares_cut = list_shares[0:100]
    shares_in_box = []
    money_left = take_best_shares(list_shares_cut, 100 + 20 * n)
    first_shares_number = len(shares_in_box)
    shares_following = list_shares[first_shares_number : first_shares_number + 18]
    shares_in_box_following = investment(shares_following, money_left)
    shares_in_box += shares_in_box_following
    end = time.time()
    analyses = Analyses()
    analyses.gain = profitability(shares_in_box)
    analyses.number_share = first_shares_number + 17
    duration = end - begin
    analyses.time_spend = duration
    analyses.memory = psutil.virtual_memory().percent
    analyses_list.append(analyses)

with open("analyses_optimized.csv", "w") as fichier_csv:
    var = csv.writer(fichier_csv, delimiter=",")
    var.writerow(header)
    var.writerow(units)
    for item in analyses_list:
        var.writerow([item.number_share, item.gain, item.time_spend, item.memory])

print()
print("résumer des analyses du programme optimized")
for item in analyses_list:
    print("nombre d'actions: ", item.number_share)
    print("durée: ", item.time_spend)
    print("mémoire utilisée: ", item.memory, "%/n")
