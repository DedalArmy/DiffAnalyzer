import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pandas.core.series import Series
from itertools import count
from numpy import NaN
from os import listdir
from os.path import isfile, join

from DiffAnalyzer import DiffAnalyzer, export_result, Increment

if __name__ == '__main__':
    path = './csv2/'
    old = 'old'
    new = 'new'
    old_v = ''
    new_v = ''
    obj = 'obj'
    subst = 'subst'
    kind = 'diff_kind'

    tous_mes_objets = []

    for file in listdir(path):
        file2 = path + file
        print(file2)
        df = pd.read_csv(file2, sep=';')
        tous_mes_objets.append(DiffAnalyzer(df, file))

    df = export_result(tous_mes_objets)
    print(df)

    nb_diff_arch = len(df.values)
    good_increment = df[(df['actualIncrement'] == df['proposedIncrement'])]
    nb_good_increment = len(good_increment)
    semi_wrong_increment = df[(df['isSubstitutable'] == df['shoulBeSubstitutable']) & (df['actualIncrement'] != df['proposedIncrement'])]
    nb_semi_wrong_increment = len(semi_wrong_increment)
    wrong_increment = df[(df['isSubstitutable'] != df['shoulBeSubstitutable']) & (df['actualIncrement'] != df['proposedIncrement'])]
    nb_wrong_increment = len(wrong_increment)
    # print(good_increment)
    # print(semi_wrong_increment)
    # print(wrong_increment)

    labels = 'Right version increment', 'Inaccurate \nversion increment', 'Wrong version increment'
    sizes = [nb_good_increment, nb_semi_wrong_increment, nb_wrong_increment]
    colors = ['lightskyblue', 'gold', 'lightcoral']
    explode = (0.1, 0.1, 0.1)

    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.2f%%', shadow=True, startangle=90, labeldistance=1)

    plt.axis('equal')

    plt.savefig('version_increments.png')
    plt.show()

    erosion_only = df[(df['isSubjectToErosion'] == True) & (df['isSubjectToDrift'] == False)]
    nb_erosion_only = len(erosion_only)
    drift_only = df[(df['isSubjectToDrift'] == True) & (df['isSubjectToErosion'] == False)]
    nb_drift_only = len(drift_only)
    erosion_and_drift = df[(df['isSubjectToErosion'] == True) & (df['isSubjectToDrift'] == True)]
    nb_erosion_and_drift = len(erosion_and_drift)
    no_erosion_nor_drift = df[(df['isSubjectToErosion'] == False) & (df['isSubjectToDrift'] == False)]
    nb_no_erosion_nor_drift = len(no_erosion_nor_drift)
    print(erosion_only)
    print(drift_only)
    print(erosion_and_drift)
    print(no_erosion_nor_drift)



    labels = 'probable erosion', 'probable drift', 'probable erosion and drift','no erosion nor dift'
    sizes = [nb_erosion_only, nb_drift_only, nb_erosion_and_drift,nb_no_erosion_nor_drift]
    colors = ['lightskyblue', 'gold', 'lightcoral', 'yellowgreen']
    explode = (0.1, 0.1, 0.1, 0.1)

    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.2f%%', shadow=True, startangle=90, labeldistance=1)

    plt.axis('equal')

    plt.savefig('erosion_drift.png')
    plt.show()