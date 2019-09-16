import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pandas.core.series import Series
from itertools import count
from numpy import NaN
from os import listdir
from enum import Enum
from os.path import isfile, join

class Increment(Enum):
    MAJOR = 1
    MINOR = 2
    BUILD = 3

class DiffAnalyzer:
    old = 'old'
    new = 'new'
    old_v = ''
    new_v = ''
    nb_diffs = 0
    nb_diffParam = 0
    nb_notSubst_diffParam = 0
    nb_Subst_diffParam = 0
    nb_diffSign = 0
    nb_notSubst_diffSign = 0
    nb_Subst_diffSign = 0
    nb_diffIntType = 0
    nb_notSubst_diffIntType = 0
    nb_Subst_diffIntType = 0
    nb_diffInt = 0
    nb_notSubst_diffInt = 0
    nb_Subst_diffInt = 0
    nb_diffCompType = 0
    nb_notSubst_diffCompType = 0
    nb_Subst_diffCompType = 0
    nb_diffCompInst = 0
    nb_notSubst_diffCompInst = 0
    nb_Subst_diffCompInst = 0
    nb_diffCompClass = 0
    nb_notSubst_diffCompClass = 0
    nb_Subst_diffCompClass = 0
    nb_diffAttr = 0
    nb_notSubst_diffAttr = 0
    nb_Subst_diffAttr = 0
    nb_diffCompRole = 0
    nb_notSubst_diffCompRole = 0
    nb_Subst_diffCompRole = 0
    nb_diffAssm = 0
    nb_notSubst_diffAssm = 0
    nb_Subst_diffAssm = 0
    nb_diffConfig = 0
    nb_notSubst_diffConfig = 0
    nb_Subst_diffConfig = 0
    nb_diffSpec = 0
    nb_notSubst_diffSpec = 0
    nb_Subst_diffSpec = 0

    def __init__(self,df,name):
        self.nb_diffs = df[old].count()
        print('nb diffs = ' + str(self.nb_diffs))
        if self.nb_diffs > 0:
            self.nb_diffParam = len(df[(df[obj].str.contains('dedal.impl.Parameter'))])
            self.nb_notSubst_diffParam = len(df[(df[obj].str.contains('dedal.impl.Parameter')) & (df[subst] == False)])
            self.nb_Subst_diffParam = len(df[(df[obj].str.contains('dedal.impl.Parameter')) & (df[subst] == True)])
            self.nb_diffSign = len(df[(df[obj].str.contains('dedal.impl.Signature'))])
            self.nb_notSubst_diffSign = len(df[(df[obj].str.contains('dedal.impl.Signature')) & (df[subst] == False)])
            self.nb_Subst_diffSign = len(df[(df[obj].str.contains('dedal.impl.Signature')) & (df[subst] == True)])
            self.nb_diffIntType = len(df[(df[obj].str.contains('dedal.impl.InterfaceType'))])
            self.nb_notSubst_diffIntType = len(df[(df[obj].str.contains('dedal.impl.InterfaceType')) & (df[subst] == False)])
            self.nb_Subst_diffIntType = len(df[(df[obj].str.contains('dedal.impl.InterfaceType')) & (df[subst] == True)])
            self.nb_diffInt = len(df[(df[obj].str.contains('dedal.impl.Interface'))])
            self.nb_notSubst_diffInt = len(df[(df[obj].str.contains('dedal.impl.Interface')) & (df[subst] == False)])
            self.nb_Subst_diffInt = len(df[(df[obj].str.contains('dedal.impl.Interface')) & (df[subst] == True)])
            self.nb_diffCompType = len(df[(df[obj].str.contains('dedal.impl.CompType'))])
            self.nb_notSubst_diffCompType = len(df[(df[obj].str.contains('dedal.impl.CompType')) & (df[subst] == False)])
            self.nb_Subst_diffCompType = len(df[(df[obj].str.contains('dedal.impl.CompType')) & (df[subst] == True)])
            self.nb_diffCompInst = len(df[(df[obj].str.contains('dedal.impl.CompInst'))])
            self.nb_notSubst_diffCompInst = len(df[(df[obj].str.contains('dedal.impl.CompInst')) & (df[subst] == False)])
            self.nb_Subst_diffCompInst = len(df[(df[obj].str.contains('dedal.impl.CompInst')) & (df[subst] == True)])
            self.nb_diffCompClass = len(df[(df[obj].str.contains('dedal.impl.CompClass'))])
            self.nb_notSubst_diffCompClass = len(df[(df[obj].str.contains('dedal.impl.CompClass')) & (df[subst] == False)])
            self.nb_Subst_diffCompClass = len(df[(df[obj].str.contains('dedal.impl.CompClass')) & (df[subst] == True)])
            self.nb_diffAttr = len(df[(df[obj].str.contains('dedal.impl.Attribute'))])
            self.nb_notSubst_diffAttr = len(df[(df[obj].str.contains('dedal.impl.Attribute')) & (df[subst] == False)])
            self.nb_Subst_diffAttr = len(df[(df[obj].str.contains('dedal.impl.Attribute')) & (df[subst] == True)])
            self.nb_diffCompRole = len(df[(df[obj].str.contains('dedal.impl.CompRole'))])
            self.nb_notSubst_diffCompRole = len(df[(df[obj].str.contains('dedal.impl.CompRole')) & (df[subst] == False)])
            self.nb_Subst_diffCompRole = len(df[(df[obj].str.contains('dedal.impl.CompRole')) & (df[subst] == True)])
            self.nb_diffAssm = len(df[(df[obj].str.contains('dedal.impl.Assembly'))])
            self.nb_notSubst_diffAssm = len(df[(df[obj].str.contains('dedal.impl.Assembly')) & (df[subst] == False)])
            self.nb_Subst_diffAssm = len(df[(df[obj].str.contains('dedal.impl.Assembly')) & (df[subst] == True)])
            self.nb_diffConfig = len(df[(df[obj].str.contains('dedal.impl.Configuration'))])
            self.nb_notSubst_diffConfig = len(df[(df[obj].str.contains('dedal.impl.Configuration')) & (df[subst] == False)])
            self.nb_Subst_diffConfig = len(df[(df[obj].str.contains('dedal.impl.Configuration')) & (df[subst] == True)])
            self.nb_diffSpec = len(df[(df[obj].str.contains('dedal.impl.Specification'))])
            self.nb_notSubst_diffSpec = len(df[(df[obj].str.contains('dedal.impl.Specification')) & (df[subst] == False)])
            self.nb_Subst_diffSpec = len(df[(df[obj].str.contains('dedal.impl.Specification')) & (df[subst] == True)])
            self.old_v = df[old].values.tolist()[0]
            self.new_v = df[new].values.tolist()[0]
        else:
            self.old_v = name.split("---")[0]
            self.new_v = name.split("---")[1].split(".csv")[0]

    def shouldBeSubstitutable(self):
        str = "broadleaf-"
        if self.new_v[len(str)+1:][0] == self.old_v[len(str)+1:][0]:
            return True
        return False

    def isSubstitutable(self):
        if self.nb_notSubst_diffSpec > 0:
            return False
        if self.nb_notSubst_diffConfig > 0:
            return False
        if self.nb_notSubst_diffAssm > 0:
            return False
        if self.nb_notSubst_diffCompRole > 0:
            return False
        if self.nb_notSubst_diffCompType > 0:
            return False
        if self.nb_notSubst_diffCompClass > 0:
            return False
        if self.nb_notSubst_diffCompInst > 0:
            return False
        if self.nb_notSubst_diffInt > 0:
            return False
        if self.nb_notSubst_diffIntType > 0:
            return False
        if self.nb_notSubst_diffSign > 0:
            return False
        if self.nb_notSubst_diffParam > 0:
            return False
        if self.nb_notSubst_diffAttr > 0:
            return False
        return True

    def proposeIncrement(self):
        if self.nb_diffs == 0:
            return Increment.BUILD
        if self.isSubstitutable():
            return Increment.MINOR
        return Increment.MAJOR

    def print(self):
        print("nb_diffParam = " + str(self.nb_diffParam))
        print("nb_notSubst_diffParam = " + str(self.nb_notSubst_diffParam))
        print("nb_Subst_diffParam = " + str(self.nb_Subst_diffParam))
        print("nb_diffSign = " + str(self.nb_diffSign))
        print("nb_notSubst_diffSign = " + str(self.nb_notSubst_diffSign))
        print("nb_Subst_diffSign = " + str(self.nb_Subst_diffSign))
        print("nb_diffIntType = " + str(self.nb_diffIntType))
        print("nb_notSubst_diffIntType = " + str(self.nb_notSubst_diffIntType))
        print("nb_Subst_diffIntType = " + str(self.nb_Subst_diffIntType))
        print("nb_diffInt = " + str(self.nb_diffInt))
        print("nb_notSubst_diffInt = " + str(self.nb_notSubst_diffInt))
        print("nb_Subst_diffInt = " + str(self.nb_Subst_diffInt))
        print("nb_diffCompClass = " + str(self.nb_diffCompClass))
        print("nb_notSubst_diffCompClass = " + str(self.nb_notSubst_diffCompClass))
        print("nb_Subst_diffCompClass = " + str(self.nb_Subst_diffCompClass))
        print("nb_diffCompType = " + str(self.nb_diffCompType))
        print("nb_notSubst_diffCompType = " + str(self.nb_notSubst_diffCompType))
        print("nb_Subst_diffCompType = " + str(self.nb_Subst_diffCompType))
        print("nb_diffCompRole = " + str(self.nb_diffCompRole))
        print("nb_notSubst_diffCompRole = " + str(self.nb_notSubst_diffCompRole))
        print("nb_Subst_diffCompRole = " + str(self.nb_Subst_diffCompRole))
        print("nb_diffCompInst = " + str(self.nb_diffCompInst))
        print("nb_notSubst_diffCompInst = " + str(self.nb_notSubst_diffCompInst))
        print("nb_Subst_diffCompInst = " + str(self.nb_Subst_diffCompInst))
        print("nb_diffAttr = " + str(self.nb_diffAttr))
        print("nb_notSubst_diffAttr = " + str(self.nb_notSubst_diffAttr))
        print("nb_Subst_diffAttr = " + str(self.nb_Subst_diffAttr))
        print("nb_diffAssm = " + str(self.nb_diffAssm))
        print("nb_notSubst_diffAssm = " + str(self.nb_notSubst_diffAssm))
        print("nb_Subst_diffAssm = " + str(self.nb_Subst_diffAssm))
        print("nb_diffConfig = " + str(self.nb_diffConfig))
        print("nb_notSubst_diffConfig = " + str(self.nb_notSubst_diffConfig))
        print("nb_Subst_diffConfig = " + str(self.nb_Subst_diffConfig))
        print("nb_diffSpec = " + str(self.nb_diffSpec))
        print("nb_notSubst_diffSpec = " + str(self.nb_notSubst_diffSpec))
        print("nb_Subst_diffSpec = " + str(self.nb_Subst_diffSpec))

if __name__ == '__main__':
    path = './csv/'
    old = 'old'
    new = 'new'
    obj = 'obj'
    subst = 'subst'
    tot_diffs = 0
    tot_diffParam = 0
    tot_diffSign = 0
    tot_diffIntType = 0
    tot_diffInt = 0
    tot_diffCompType = 0
    tot_diffCompInst = 0
    tot_diffCompClass = 0
    tot_diffAttr = 0
    tot_diffCompRole = 0
    tot_diffAssm = 0
    tot_diffConfig = 0
    tot_diffSpec = 0
    tot_arch = 0
    tot_subs_arch = 0

    tous_mes_objets = []

    for file in listdir(path):
        file2 = path + file
        print(file2)
        df = pd.read_csv(file2, sep=';')
        tous_mes_objets.append(DiffAnalyzer(df, file))

    df = []

    for obj in tous_mes_objets:
        dico = {"old" : obj.old_v,
                "new" : obj.new_v,
                "shoulBeSubstitutable" : obj.shouldBeSubstitutable(),
                "isSubstitutable" : obj.isSubstitutable(),
                "proposedIncrement" : obj.proposeIncrement()
                }
        df.append(dico)

    df = pd.DataFrame(df)
    df = df.sort_values(by=old).reset_index(drop=True)
    df.to_csv('./result.csv', sep=',')
    print(df)