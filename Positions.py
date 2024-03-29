import random


def getValuesFromFile(fileName):
    file = open(fileName)
    data = list(file.read().split("\n"))
    file.close()
    return data


# FORMAT : Pos_ID, Pos_Name, Pos_Starting_Salary, Pos_Requirment, DepID

if __name__ == '__main__':

    getDepartmentNames = list(getValuesFromFile("txtFiles/DepartmentNames.txt"))
    getDepartmentIDS = list(getValuesFromFile("txtFiles/DepartmentIDS.txt"))
    amountOfDepIDS = getDepartmentIDS[:len(getDepartmentNames)]

    positionIDs = getValuesFromFile("txtFiles/PositionIDS.txt")
    positionNames = getValuesFromFile("txtFiles/PositionNames.txt")
    startingSalary = getValuesFromFile("txtFiles/PositionsStartingSalary.txt")
    WorkRequirement = getValuesFromFile("txtFiles/PositionRequirments.txt")
    requirement = ''
    # counter = 0
    # for i in positionIDs:
    #     print(counter, i)
    #     counter += 1

    '''
       0,Degree
       1,Work Experience
       2,Apprenticeship

       '''

    print("INSERT INTO POSITIONS VALUES")
    openFile = open("txtFiles/PositionID_Name_Salary.txt", "w")
    salary = 0

    for i in range(len(positionNames)):

        if positionNames[i][0] == 'D':
            requirement = WorkRequirement[0]
            salary = random.randint(6, len(startingSalary) - 1)
        elif positionNames[i][0] == 'W':
            requirement = WorkRequirement[1]
            salary = random.randint(3, 5)
        else:
            requirement = WorkRequirement[2]
            salary = random.randint(0, 2)

        openFile.write(f"{positionIDs[i]} | {positionNames[i][1:]} | {startingSalary[salary]}\n")

        print(f"('{positionIDs[i]}', "
              f"'{positionNames[i][1:]}', "
              f"{float(startingSalary[salary])},"
              f"'{requirement}', "
              f"'{amountOfDepIDS[random.randint(0, len(amountOfDepIDS) - 1)]}')", end='')

        if i != len(positionNames) - 1:
            print(",")

    openFile.close()