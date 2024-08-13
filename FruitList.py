import os

# options = ["Add Fruit",
#            "Remove Fruit",
#            "Show List",
#            "Clear List",
#            "Exit"]

FILENAME = "FruitList.txt"
bRunning = True


# region Privates

def OpenFileToRead():
    if os.path.exists(FILENAME):
        return open(FILENAME, "r")
    else:
        open(FILENAME, "w")
        return OpenFileToRead()


def OpenFileToWrite():
    return open(FILENAME, "w")


def OpenFileToAppend():
    return open(FILENAME, "a")


def ReadList():
    with OpenFileToRead() as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            print(i, line, end="")

    print()


def CleanFile():
    with OpenFileToWrite() as file:
        pass


# endregion


def AddFruit(value: str):
    if value == "":
        return
    # adds a new line if there is none
    if not value.endswith("\n"):
        value += "\n"

    with OpenFileToAppend() as file:
        file.writelines(value)
        print("Item added to the list!! \n")


def AddFruits(values: list):
    if len(values) <= 0:
        return

    [AddFruit(f) for f in values]


def ReplaceFruit(OldValue: str, NewValue: str, outList: list):
    fList = GetFruitList()
    try:
        index = fList.index(OldValue)
        fList[index] = NewValue
        CleanFile()
        AddFruits(fList)

        if len(outList) > 0:
            outList.clear()

        outList.extend(fList)
        return True
    except ValueError:
        return False


def RemoveFruit(value: str):
    try:
        with OpenFileToRead() as file:
            lines = file.readlines()

        with OpenFileToWrite() as file:
            for line in lines:
                if value not in line:
                    file.writelines(line)

    except FileNotFoundError:
        print("File Not Found")


def GetFruitList():
    with OpenFileToRead() as file:
        fList = file.readlines()
    return fList


def HasItemInTheList(item: str):
    items = GetFruitList()
    if len(items) == 0:
        return False
    try:
        item += "\n"
        index = items.index(item)
        if index >= 0:
            return True
    except ValueError:
        return False
    
def ModifyFruitList(newItems: list):
    CleanFile()
    AddFruits(newItems)
