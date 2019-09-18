import pandas as pd
import matplotlib.pyplot as plt
from os import listdir
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

    labels = 'Right version increment', 'Inaccurate version increment', 'Wrong version increment'
    sizes = [nb_good_increment, nb_semi_wrong_increment, nb_wrong_increment]
    colors = ['lightskyblue', 'gold', 'lightcoral']
    explode = (0.1, 0.1, 0.1)

    plt.figure(0)
    plt.pie(sizes, explode=explode, colors=colors,
            autopct='%1.2f%%', shadow=False, startangle=90, labeldistance=1)
    plt.title('')
    plt.legend( labels=labels, loc=3)

    plt.axis('equal')

    plt.savefig('version_increments.png', dpi=600)

    major_for_build_increment = df[(df['actualIncrement'] == Increment.MAJOR) & (df['proposedIncrement'] == Increment.BUILD)]
    nb_major_for_build_increment = len(major_for_build_increment)
    build_for_major_increment = df[(df['actualIncrement'] == Increment.BUILD) & (df['proposedIncrement'] == Increment.MAJOR)]
    nb_build_for_major_increment = len(build_for_major_increment)
    build_for_minor_increment = df[(df['actualIncrement'] == Increment.BUILD) & (df['proposedIncrement'] == Increment.MINOR)]
    nb_build_for_minor_increment = len(build_for_minor_increment)
    minor_for_build_increment = df[(df['actualIncrement'] == Increment.MINOR) & (df['proposedIncrement'] == Increment.BUILD)]
    nb_minor_for_build_increment = len(minor_for_build_increment)
    major_for_minor_increment = df[(df['actualIncrement'] == Increment.MAJOR) & (df['proposedIncrement'] == Increment.MINOR)]
    nb_major_for_minor_increment = len(major_for_minor_increment)
    minor_for_major_increment = df[(df['actualIncrement'] == Increment.MINOR) & (df['proposedIncrement'] == Increment.MAJOR)]
    nb_minor_for_major_increment = len(minor_for_major_increment)

    labels = []
    sizes = []
    colors = []
    explode = []

    if nb_major_for_build_increment > 0:
        labels.append('Major for build increment')
        sizes.append(nb_major_for_build_increment)
        colors.append('lightskyblue')
        explode.append(0.1)
    if nb_major_for_minor_increment > 0:
        labels.append('Major for minor increment')
        sizes.append(nb_major_for_minor_increment)
        colors.append('gold')
        explode.append(0.1)
    if nb_minor_for_build_increment > 0:
        labels.append('Minor for build increment')
        sizes.append(nb_minor_for_build_increment)
        colors.append('lightcoral')
        explode.append(0.1)
    if nb_minor_for_major_increment > 0:
        labels.append('Minor for major increment')
        sizes.append(nb_minor_for_major_increment)
        colors.append('yellowgreen')
        explode.append(0.1)
    if nb_build_for_minor_increment > 0:
        labels.append('Build for minor increment')
        sizes.append(nb_build_for_minor_increment)
        colors.append('peachpuff')
        explode.append(0.1)
    if nb_build_for_major_increment > 0:
        labels.append('Build for major increment')
        sizes.append(nb_build_for_major_increment)
        colors.append('mediumslateblue')
        explode.append(0.1)

    plt.figure(1)
    plt.pie(sizes, explode=explode, colors=colors,
            autopct='%1.2f%%', shadow=False, startangle=90, labeldistance=1)
    plt.title('')
    plt.legend( labels=labels, loc=3)

    plt.axis('equal')

    plt.savefig('version_increments_details.png', dpi=600)

    erosion_only = df[(df['isSubjectToErosion'] == True) & (df['isSubjectToDrift'] == False)]
    nb_erosion_only = len(erosion_only)
    drift_only = df[(df['isSubjectToDrift'] == True) & (df['isSubjectToErosion'] == False)]
    nb_drift_only = len(drift_only)
    erosion_and_drift = df[(df['isSubjectToErosion'] == True) & (df['isSubjectToDrift'] == True)]
    nb_erosion_and_drift = len(erosion_and_drift)
    no_erosion_nor_drift = df[(df['isSubjectToErosion'] == False) & (df['isSubjectToDrift'] == False)]
    nb_no_erosion_nor_drift = len(no_erosion_nor_drift)
    # print(erosion_only)
    # print(drift_only)
    # print(erosion_and_drift)
    # print(no_erosion_nor_drift)

    labels = 'Probable erosion', 'Probable drift', 'No erosion nor drift'
    sizes = [nb_erosion_only, nb_drift_only, nb_no_erosion_nor_drift]
    colors = ['lightskyblue', 'gold', 'lightcoral']
    explode = [0.1, 0.1, 0.1]

    if nb_erosion_and_drift>0:
        labels.append('probable erosion and drift')
        sizes.append(nb_erosion_and_drift)
        colors.append('yellowgreen')
        explode.append(0.1)

    plt.figure(2)
    plt.pie(sizes, explode=explode, colors=colors,
            autopct='%1.2f%%', shadow=False, startangle=90, labeldistance=1)
    plt.title('')
    plt.legend( labels=labels, loc=3)
    plt.axis('equal')

    plt.savefig('erosion_drift.png', dpi=600)
    plt.show()