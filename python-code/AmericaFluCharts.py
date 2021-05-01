import matplotlib.pyplot as plt


def week2month(weekly, monthly, count):
    """
    :param weekly: list of all flu cases per week
    :param monthly: list of all flu cases per month
    :param count: number of weeks in the month that is being totaled
    :return: updated weekly and monthly
    """
    n = 0
    cases = 0
    while n <= count:
        cases += weekly.pop(0)
        n += 1

    monthly.append(cases)
    return weekly, monthly


def get2020():
    weekly = []
    monthly = []

    with open('america2020.csv', 'r') as data:  ### CHANGE THE FILE ###
        for line in data:
            for word in line.split():
                if word.isdigit():
                    weekly.append(int(word))

    weekly, monthly = week2month(weekly, monthly, 4)  # october 2020
    weekly, monthly = week2month(weekly, monthly, 3)  # november 2020
    weekly, monthly = week2month(weekly, monthly, 4)  # december 2020
    weekly, monthly = week2month(weekly, monthly, 3)  # january 2021
    weekly, monthly = week2month(weekly, monthly, 3)  # february 2021
    weekly, monthly = week2month(weekly, monthly, 3)  # march 2021
    # print('final weekly', weekly)
    # print('final monthly', monthly)

    return monthly


def get2019():
    weekly = []
    monthly = []

    with open('america2019.csv', 'r') as data:  ### CHANGE THE CSV FILE ###
        for line in data:
            for word in line.split():
                if word.isdigit():
                    weekly.append(int(word))

    weekly, monthly = week2month(weekly, monthly, 4)  # october 2019
    weekly, monthly = week2month(weekly, monthly, 3)  # november 2019
    weekly, monthly = week2month(weekly, monthly, 3)  # december 2019
    weekly, monthly = week2month(weekly, monthly, 4)  # january 2020
    weekly, monthly = week2month(weekly, monthly, 3)  # february 2020
    weekly, monthly = week2month(weekly, monthly, 3)  # march 2020
    # print('final weekly', weekly)
    # print('final monthly', monthly)

    return monthly


def main():
    flu2020 = get2020()
    flu2019 = get2019()
    print(flu2020)
    print(flu2019)

    flu2019 = [3538, 14780, 50526, 101242, 88851, 37282]
    flu2020 = [305, 319, 575, 361, 216, 149]

    fig, ax = plt.subplots()
    ax.plot(['Oct', 'Nov', 'Dec', 'Jan', 'Feb', 'Mar'], flu2019)

    ax.set(xlabel='Month', ylabel='Flu Cases', title='America 2019 Flu Cases') ### CHANGE THE TITLE ###
    ax.grid()

    fig.savefig("test.png")
    plt.show()

    fig, ax = plt.subplots()
    ax.plot(['Oct', 'Nov', 'Dec', 'Jan', 'Feb', 'Mar'], flu2020)

    ax.set(xlabel='Month', ylabel='Flu Cases', title='America 2020 Flu Cases') ### CHANGE THE TITLE ###
    ax.grid()

    fig.savefig("test.png")
    plt.show()

main()
