import pandas as pd

#def calcRsi(period):



def calcMAE(dataFeed, period, increase):
    valuesMAE = [0]
    for i, val in dataFeed.iterrows():
        previousIndex = i-1
        open = val["o"]
        close = val["c"]
        if direction(increase,open,close):
            valuesMAE.append(funcMAE(close, valuesMAE[previousIndex], period))
        else:
            valuesMAE.append(funcMAE(0, valuesMAE[previousIndex], period))
    return valuesMAE

def calcSMA(dataFeed, period):
    storedValues={"gains":[], "loss":[]}
    averageGains = []
    averageLoss = []
    for i, val in dataFeed.iterrows():
        open = val["o"]
        close = val["c"]
        change = close - open
        if i<period-i:
            if change<=0 :
                storedValues["loss"].append(abs(change))
            else:
                storedValues["gains"].append(change)
        elif i==period-1:
            averageGains.append(sum(storedValues["gains"])/period)
            averageLoss.append(sum(storedValues["loss"])/period)
        elif i>period-1:
            avg = (averageGains[i-period]*13+(change if change>0 else 0))/14
            averageGains.append(avg)
            avg = (averageLoss[i-period]*13+(abs(change) if change<=0 else 0 ))/14
            averageLoss.append(avg)
    return averageLoss, averageGains


def calcRSI(tup):
    avgLoss = tup[0]
    avgGains = tup[1]
    print(avgGains)
    rsiValues = []
    for i,val in enumerate(avgLoss):
        rs = avgGains[i]/val
        rsi = 100 - 100/(1+rs)
        rsiValues.append(rsi)

def direction(increase, open, close):
    if increase:
        if close>=open:
            return True
        else :
            return False
    else:
        if open>close:
            return True
        else:
            return False


def funcMAE(price,priorMAEVal,period):
    A = 2%(1+period)
    mae = price*A + priorMAEVal*(1-A)
    return mae

