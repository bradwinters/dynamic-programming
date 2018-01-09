import sys
import numpy as np

def DPChange(money,Coins):
    print("In DPC, ")
    print("Money is ",money)
    print("Coins list is ",Coins)
    MinNumCoins=np.arange(99000)
    MinNumCoins[0]=0
    for m in range (1,money+1):
        print("M is ",m)
        MinNumCoins[m]=999999
        for i in range (len(Coins)):
            print("Compare m ",m," to ",Coins[i])
            if m >= Coins[i]:
                if MinNumCoins[m - Coins[i]] + 1  < MinNumCoins[m]:
                    MinNumCoins[m] = MinNumCoins[m - Coins[i]] +1

    print("returning . . . ")
    print(MinNumCoins)
    print(MinNumCoins[money])
    print("lllllllllllll")
    return MinNumCoins[money]

if __name__ == "__main__":

    Reads=[]
    #  take a redirected file, dp.tx, dp1.txt, etc from the < command line
    #  First line is the amount of money to change or total
    #  Second line is an array of currency face values used in combinations
    #  to get to the amount of money with as little coins as possible 
    #   For 40, 2 20s may be the least amount from 50, 25, 20, 10, 5, 1
    #
    #From the command line, load the file and parse according to expected data
    for lines in sys.stdin:
        Reads.append(lines.rstrip().upper())
    
    line0=Reads[0].split()
    line1=Reads[1].split(',')

    Money=int(line0[0])
    Coins = [int(numeric_string) for numeric_string in line1]
    print("Money is ",Money)
    print("Coins array is ",Coins)
    
    print("Calling DPChange with (",Money," ",Coins)
    DPChange(Money,Coins)
