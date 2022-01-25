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


list_shares = []
list_files = ["dataset1.csv", "dataset2.csv"]
begin = time.time()

for file in list_files:
    with open(file, newline="") as share_file:
        share_file = csv.DictReader(share_file)
        for row in share_file:
            if float(row["benefit"]) > 0 and float(row["prices"]) > 0:
                share = Share(
                    row["shares"], float(row["prices"]), float(row["benefit"])
                )
                list_shares.append(share)
    print("longueur:", len(list_shares))

    investor1 = Investor("toto", 400, 400, [])
    investor2 = Investor("titi", 500, 500, [])
    list_investors = [investor1, investor2]

    list_shares = sorted(list_shares, key=lambda x: x.benefit, reverse=True)
    list_shares = list_shares[0:100]

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

    shares_in_box = []

    def take_best_shares(list_shares, money_spend):
        money = money_spend
        for i in range(len(list_shares)):
            if money - list_shares[i].price > 0:
                shares_in_box.append(list_shares[i])
                money -= list_shares[i].price
            else:
                break
        return 200 + money

    money_left = take_best_shares(list_shares, 300)
    begin_list = len(shares_in_box)
    shares_following = list_shares[begin_list : begin_list + 18]
    shares_in_box_following = investment(shares_following, money_left)
    shares_in_box += shares_in_box_following
    sum_price = 0
    for item in shares_in_box:
        sum_price += item.price
    sum_benefit = profitability(shares_in_box)

    end = time.time()
    duration = end - begin

    print("mémoire utilisée: ", psutil.virtual_memory().percent)
    print("somme dépensée = ", sum_price, "bénéfice = ", sum_benefit)
    print("duration=", duration)
    for item in shares_in_box:
        print(item.name)
    if file == "dataset1.csv":
        file_save = open("optimized.txt", "w")
    file_save.write(f"résultats pour le fichier: {file} \n")
    file_save.write(f"somme dépensée = {sum_price} bénéfice = {sum_benefit}\n")
    file_save.write("actions achetées: \n")
    for share in shares_in_box:
        file_save.write(f"{share.name}\n")

file_save.close()
