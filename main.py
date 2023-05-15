# This is a sample Python script.
import Preprocessing.CSV_Combining as Cc

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Press the green button in the gutter to run the script.
# Make sure there are only needed txt files in the path

if __name__ == '__main__':
    # set the path where the CSV files are located
    # preprocessing
    # write the path of txt file:
    path = input("Plz input the path of the txt files\n")
    cap = input("Plz input the separate parameter\n")
    Cc.combine(path, cap)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
