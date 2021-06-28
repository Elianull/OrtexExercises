import csv
with open('2017.csv', encoding='utf8') as file:
    read = csv.DictReader(file, delimiter=",")
    count = {}
    for row in read:
        exc = row['exchange']
        if exc in count.keys():
            count[exc] += 1
        else:
            count[exc] = 1
    print("\nThe exchange with the most transactions on file is", max(count, key=count.get))  # Output key with maximum value

    file.seek(0)
    read = csv.DictReader(file, delimiter=",")
    count = {}
    for row in read:
        companyName = row['companyName']
        date = int(row['tradedate'])
        if (date >= 20170800 and date < 20170900):  # Check if date is in August 2017
            if companyName in count.keys():
                count[companyName] += row['valueEUR']
            else:
                count[companyName] = row['valueEUR']
    print("\nThe company name with the highest combined valueEUR in August of 2017 is ", max(count, key=count.get))  # Output key with maximum value

    file.seek(0)
    read = csv.DictReader(file, delimiter=",")
    count = [0]*12
    total = 0
    for row in read:
        if (int(row['tradeSignificance']) == 3):  # Check trade significance
            total += 1
            date = int(row['tradedate'])
            if (date < 20170200):  # Get month
                count[0] += 1
            elif(date < 20170300):
                count[1] += 1
            elif(date < 20170400):
                count[2] += 1
            elif(date < 20170500):
                count[3] += 1
            elif(date < 20170600):
                count[4] += 1
            elif(date < 20170700):
                count[5] += 1
            elif(date < 20170800):
                count[6] += 1
            elif(date < 20170900):
                count[7] += 1
            elif(date < 20171000):
                count[8] += 1
            elif(date < 20171100):
                count[9] += 1
            elif(date < 20171200):
                count[10] += 1
            else:
                count[11] += 1
    print("\nFor 2017, only considering transactions with tradeSignificance 3, what is the percentage of transactions per month?")
    print('Jan, {}%'.format(round(count[0]/total*100, 2)))  # Output formatted response with rounded value
    print('Feb, {}%'.format(round(count[1]/total*100, 2)))
    print('Mar, {}%'.format(round(count[2]/total*100, 2)))
    print('Apr, {}%'.format(round(count[3]/total*100, 2)))
    print('May, {}%'.format(round(count[4]/total*100, 2)))
    print('Jun, {}%'.format(round(count[5]/total*100, 2)))
    print('Jul, {}%'.format(round(count[6]/total*100, 2)))
    print('Aug, {}%'.format(round(count[7]/total*100, 2)))
    print('Sep, {}%'.format(round(count[8]/total*100, 2)))
    print('Oct, {}%'.format(round(count[9]/total*100, 2)))
    print('Nov, {}%'.format(round(count[10]/total*100, 2)))
    print('Dec, {}%'.format(round(count[11]/total*100, 2)))
