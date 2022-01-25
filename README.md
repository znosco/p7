# p7
>The goal of this project is to design programs capable of choosing the best shares from a list of shares.


## bruteforce.py 
>The idea is to consider all the possible combinations from a certain number of shares.
>The program produces the file bruteforce.txt

## optimized.py
>The idea is to take the best actions in order according to their performance and to ask ourselves in which case we have not selected the best.
>The program produces the file optimized.txt

## analyses.py
>I designed the analyses.py program which analyzes the 2 programs bruteforce.py and optimized.py.
>It analyzes the duration and ram memory consumption for the 2 programs according to the number of actions.
>The analyses.py program displays the results on the screen and saves them in 2 files: analyses_forcebrute.csv and
>analyses_optimized.csv


to create the virtual environment(window's users):
```sh
python -m venv env
pip install -r requirements.txt
```

for activate environment use activate.bat(window's users):
```sh
env/scripts/activate.bat
```
