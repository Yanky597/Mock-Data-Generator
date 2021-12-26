
import random

def getValuesFromFile(fileName):
    file = open(fileName)
    data = list(file.read().split("\n"))
    file.close()
    return data


def CreatesStartEndTimes():
    getDates = getValuesFromFile("txtFiles/dates.txt")
    sortedDate = sorted(getDates)
    splitDates = []
    justSortedDates = []
    times = []
    timeDateFormat = []
    for i in sortedDate:
        i.split()
        a = i.split(" ")
        splitDates.append(a)
    for i in splitDates:
        justSortedDates.append(i[0])
        times.append(i[1])
    sortedTimes = sorted(times)
    # writeToSortedDates = open("txtFiles/sortedDatesWithAddedTimes.txt", "w")
    for i in range(len(justSortedDates)):
        seconds = sortedTimes[i][6:]
        minutes = int(sortedTimes[i][3:5])
        hours = int(sortedTimes[i][0:2])
        day = int(justSortedDates[i][8:])
        month = justSortedDates[i][5:7]
        year = justSortedDates[i][:4]
        addTime = random.randint(1, 60)
        # print("ORIGINAL TIME = ", minutes)
        minutes += addTime

        if (minutes >= 60):
            minutes = minutes % 60
            hours += 1
            if (hours >= 24):
                hours = hours % 24
                day += 1

        if (minutes < 10):
            minutes = '0' + str(minutes)
        if (day < 10):
            day = '0' + str(day)
        if (hours < 10):
            hours = '0' + str(hours)

        # print("ADD TIME = ", addTime)
        # writeToSortedDates.write(f"{justSortedDates[i]} {sortedTimes[i]} | {year}-{month}-{day} {hours}:{minutes}:{seconds}\n")

        # print(justSortedDates[i], sortedTimes[i])
        # print(f"{justSortedDates[i]} {sortedTimes[i]} | {year}-{month}-{day} {hours}:{minutes}:{seconds}\n")
    # writeToSortedDates.close()


if __name__ == '__main__':
    #CreatesStartEndTimes()
    customerIDS = getValuesFromFile("txtFiles/listOfMyCustomerPKs.txt")[:1000]
    getTimes = getValuesFromFile("txtFiles/sortedDatesWithAddedTimes.txt")
    startTime = [i.split("|")[0] for i in getTimes]
    endTime = [i.split("|")[1] for i in getTimes]
    print("INSERT INTO SESSIONS VALUES")
    # counter = 0
    for i in range(1000):
        # for j in range(random.randint(0, 30)):
        session = random.randint(0, len(getTimes) - 1)
        print(f"({i}, '{customerIDS[random.randint(0, len(customerIDS)-1)]}', '{startTime[session].strip()}', '{endTime[session].strip()}', NULL)")
        # counter += 1





