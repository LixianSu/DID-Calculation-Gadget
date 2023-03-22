# This is a sample Python script.
import Preprocessing.CSV_Combining as Cc

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Press the green button in the gutter to run the script.


if __name__ == '__main__':
    # set the path where the CSV files are located
    # preprocessing
    path = input('input the files path. (eg. path/to/csv/files)\n')
    Cc.txttocsv(path)
    Cc.combine(path)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
