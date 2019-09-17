from enum import Enum
import pandas as pd

class Increment(Enum):
    MAJOR = 1
    MINOR = 2
    BUILD = 3

class DiffAnalyzer:
    old = 'old'
    new = 'new'
    old_v = ''
    new_v = ''
    obj = 'obj'
    subst = 'subst'
    kind = 'diff_kind'
    nb_diffs_ADD = 0
    nb_diffs_DEL = 0
    nb_diffs_CHG = 0
    nb_diffs = 0
    nb_diffParam_ADD = 0
    nb_diffParam_DEL = 0
    nb_diffParam_CHG = 0
    nb_diffParam = 0
    nb_notSubst_diffParam = 0
    nb_Subst_diffParam = 0
    nb_diffSign_ADD = 0
    nb_diffSign_DEL = 0
    nb_diffSign_CHG = 0
    nb_diffSign = 0
    nb_notSubst_diffSign = 0
    nb_Subst_diffSign = 0
    nb_diffIntType_ADD = 0
    nb_diffIntType_DEL = 0
    nb_diffIntType_CHG = 0
    nb_diffIntType = 0
    nb_notSubst_diffIntType = 0
    nb_Subst_diffIntType = 0
    nb_diffInt_ADD = 0
    nb_diffInt_DEL = 0
    nb_diffInt_CHG = 0
    nb_diffInt = 0
    nb_notSubst_diffInt = 0
    nb_Subst_diffInt = 0
    nb_diffCompType_ADD = 0
    nb_diffCompType_DEL = 0
    nb_diffCompType_CHG = 0
    nb_diffCompType = 0
    nb_notSubst_diffCompType = 0
    nb_Subst_diffCompType = 0
    nb_diffCompInst_ADD = 0
    nb_diffCompInst_DEL = 0
    nb_diffCompInst_CHG = 0
    nb_diffCompInst = 0
    nb_notSubst_diffCompInst = 0
    nb_Subst_diffCompInst = 0
    nb_diffCompClass_ADD = 0
    nb_diffCompClass_DEL = 0
    nb_diffCompClass_CHG = 0
    nb_diffCompClass = 0
    nb_notSubst_diffCompClass = 0
    nb_Subst_diffCompClass = 0
    nb_diffAttr_ADD = 0
    nb_diffAttr_DEL = 0
    nb_diffAttr_CHG = 0
    nb_diffAttr = 0
    nb_notSubst_diffAttr = 0
    nb_Subst_diffAttr = 0
    nb_diffCompRole_ADD = 0
    nb_diffCompRole_DEL = 0
    nb_diffCompRole_CHG = 0
    nb_diffCompRole = 0
    nb_notSubst_diffCompRole = 0
    nb_Subst_diffCompRole = 0
    nb_diffAssm_ADD = 0
    nb_diffAssm_DEL = 0
    nb_diffAssm_CHG = 0
    nb_diffAssm = 0
    nb_notSubst_diffAssm = 0
    nb_Subst_diffAssm = 0
    nb_diffConfig_ADD = 0
    nb_diffConfig_DEL = 0
    nb_diffConfig_CHG = 0
    nb_diffConfig = 0
    nb_notSubst_diffConfig = 0
    nb_Subst_diffConfig = 0
    nb_diffSpec_ADD = 0
    nb_diffSpec_DEL = 0
    nb_diffSpec_CHG = 0
    nb_diffSpec = 0
    nb_notSubst_diffSpec = 0
    nb_Subst_diffSpec = 0

    def __init__(self,df,name):
        old = 'old'
        new = 'new'
        obj = 'obj'
        subst = 'subst'
        kind = 'diff_kind'
        self.df_diffs = df
        self.nb_diffs = df[old].count()
        self.nb_diffs_ADD = len(df[(df[kind] == 'ADD')])
        self.nb_diffs_DEL = len(df[(df[kind] == 'DELETE')])
        self.nb_diffs_CHG = len(df[(df[kind] == 'CHANGE')])
        # print('nb diffs = ' + str(self.nb_diffs))
        if self.nb_diffs > 0:
            self.nb_diffParam = len(df[(df[obj].str.contains('dedal.impl.Parameter'))])
            self.nb_notSubst_diffParam = len(df[(df[obj].str.contains('dedal.impl.Parameter')) & (df[subst] == False)])
            self.nb_Subst_diffParam = len(df[(df[obj].str.contains('dedal.impl.Parameter')) & (df[subst] == True)])
            self.nb_diffParam_ADD = len(df[(df[obj].str.contains('dedal.impl.Parameter')) & (df[kind] == 'ADD')])
            self.nb_diffParam_DEL = len(df[(df[obj].str.contains('dedal.impl.Parameter')) & (df[kind] == 'DELETE')])
            self.nb_diffParam_CHG = len(df[(df[obj].str.contains('dedal.impl.Parameter')) & (df[kind] == 'CHANGE')])
            self.nb_diffSign = len(df[(df[obj].str.contains('dedal.impl.Signature'))])
            self.nb_notSubst_diffSign = len(df[(df[obj].str.contains('dedal.impl.Signature')) & (df[subst] == False)])
            self.nb_Subst_diffSign = len(df[(df[obj].str.contains('dedal.impl.Signature')) & (df[subst] == True)])
            self.nb_diffSign_ADD = len(df[(df[obj].str.contains('dedal.impl.Signature')) & (df[kind] == 'ADD')])
            self.nb_diffSign_DEL = len(df[(df[obj].str.contains('dedal.impl.Signature')) & (df[kind] == 'DELETE')])
            self.nb_diffSign_CHG = len(df[(df[obj].str.contains('dedal.impl.Signature')) & (df[kind] == 'CHANGE')])
            self.nb_diffIntType = len(df[(df[obj].str.contains('dedal.impl.InterfaceType'))])
            self.nb_notSubst_diffIntType = len(df[(df[obj].str.contains('dedal.impl.InterfaceType')) & (df[subst] == False)])
            self.nb_Subst_diffIntType = len(df[(df[obj].str.contains('dedal.impl.InterfaceType')) & (df[subst] == True)])
            self.nb_diffIntType_ADD = len(df[(df[obj].str.contains('dedal.impl.InterfaceType')) & (df[kind] == 'ADD')])
            self.nb_diffIntType_DEL = len(df[(df[obj].str.contains('dedal.impl.InterfaceType')) & (df[kind] == 'DELETE')])
            self.nb_diffIntType_CHG = len(df[(df[obj].str.contains('dedal.impl.InterfaceType')) & (df[kind] == 'CHANGE')])
            self.nb_diffInt = len(df[(df[obj].str.contains('dedal.impl.Interface'))])
            self.nb_notSubst_diffInt = len(df[(df[obj].str.contains('dedal.impl.Interface')) & (df[subst] == False)])
            self.nb_Subst_diffInt = len(df[(df[obj].str.contains('dedal.impl.Interface')) & (df[subst] == True)])
            self.nb_diffInt_ADD = len(df[(df[obj].str.contains('dedal.impl.Interface')) & (df[kind] == 'ADD')])
            self.nb_diffInt_DEL = len(df[(df[obj].str.contains('dedal.impl.Interface')) & (df[kind] == 'DELETE')])
            self.nb_diffInt_CHG = len(df[(df[obj].str.contains('dedal.impl.Interface')) & (df[kind] == 'CHANGE')])
            self.nb_diffCompType = len(df[(df[obj].str.contains('dedal.impl.CompType'))])
            self.nb_notSubst_diffCompType = len(df[(df[obj].str.contains('dedal.impl.CompType')) & (df[subst] == False)])
            self.nb_Subst_diffCompType = len(df[(df[obj].str.contains('dedal.impl.CompType')) & (df[subst] == True)])
            self.nb_diffCompType_ADD = len(df[(df[obj].str.contains('dedal.impl.CompType')) & (df[kind] == 'ADD')])
            self.nb_diffCompType_DEL = len(df[(df[obj].str.contains('dedal.impl.CompType')) & (df[kind] == 'DELETE')])
            self.nb_diffCompType_CHG = len(df[(df[obj].str.contains('dedal.impl.CompType')) & (df[kind] == 'CHANGE')])
            self.nb_diffCompInst = len(df[(df[obj].str.contains('dedal.impl.CompInst'))])
            self.nb_notSubst_diffCompInst = len(df[(df[obj].str.contains('dedal.impl.CompInst')) & (df[subst] == False)])
            self.nb_Subst_diffCompInst = len(df[(df[obj].str.contains('dedal.impl.CompInst')) & (df[subst] == True)])
            self.nb_diffCompInst_ADD = len(df[(df[obj].str.contains('dedal.impl.CompInst')) & (df[kind] == 'ADD')])
            self.nb_diffCompInst_DEL = len(df[(df[obj].str.contains('dedal.impl.CompInst')) & (df[kind] == 'DELETE')])
            self.nb_diffCompInst_CHG = len(df[(df[obj].str.contains('dedal.impl.CompInst')) & (df[kind] == 'CHANGE')])
            self.nb_diffCompClass = len(df[(df[obj].str.contains('dedal.impl.CompClass'))])
            self.nb_notSubst_diffCompClass = len(df[(df[obj].str.contains('dedal.impl.CompClass')) & (df[subst] == False)])
            self.nb_Subst_diffCompClass = len(df[(df[obj].str.contains('dedal.impl.CompClass')) & (df[subst] == True)])
            self.nb_diffCompClass_ADD = len(df[(df[obj].str.contains('dedal.impl.CompClass')) & (df[kind] == 'ADD')])
            self.nb_diffCompClass_DEL = len(df[(df[obj].str.contains('dedal.impl.CompClass')) & (df[kind] == 'DELETE')])
            self.nb_diffCompClass_CHG = len(df[(df[obj].str.contains('dedal.impl.CompClass')) & (df[kind] == 'CHANGE')])
            self.nb_diffAttr = len(df[(df[obj].str.contains('dedal.impl.Attribute'))])
            self.nb_notSubst_diffAttr = len(df[(df[obj].str.contains('dedal.impl.Attribute')) & (df[subst] == False)])
            self.nb_Subst_diffAttr = len(df[(df[obj].str.contains('dedal.impl.Attribute')) & (df[subst] == True)])
            self.nb_diffAttr_ADD = len(df[(df[obj].str.contains('dedal.impl.Attribute')) & (df[kind] == 'ADD')])
            self.nb_diffAttr_DEL = len(df[(df[obj].str.contains('dedal.impl.Attribute')) & (df[kind] == 'DELETE')])
            self.nb_diffAttr_CHG = len(df[(df[obj].str.contains('dedal.impl.Attribute')) & (df[kind] == 'CHANGE')])
            self.nb_diffCompRole = len(df[(df[obj].str.contains('dedal.impl.CompRole'))])
            self.nb_notSubst_diffCompRole = len(df[(df[obj].str.contains('dedal.impl.CompRole')) & (df[subst] == False)])
            self.nb_Subst_diffCompRole = len(df[(df[obj].str.contains('dedal.impl.CompRole')) & (df[subst] == True)])
            self.nb_diffCompRole_ADD = len(df[(df[obj].str.contains('dedal.impl.CompRole')) & (df[kind] == 'ADD')])
            self.nb_diffCompRole_DEL = len(df[(df[obj].str.contains('dedal.impl.CompRole')) & (df[kind] == 'DELETE')])
            self.nb_diffCompRole_CHG = len(df[(df[obj].str.contains('dedal.impl.CompRole')) & (df[kind] == 'CHANGE')])
            self.nb_diffAssm = len(df[(df[obj].str.contains('dedal.impl.Assembly'))])
            self.nb_notSubst_diffAssm = len(df[(df[obj].str.contains('dedal.impl.Assembly')) & (df[subst] == False)])
            self.nb_Subst_diffAssm = len(df[(df[obj].str.contains('dedal.impl.Assembly')) & (df[subst] == True)])
            self.nb_diffAssm_ADD = len(df[(df[obj].str.contains('dedal.impl.Assembly')) & (df[kind] == 'ADD')])
            self.nb_diffAssm_DEL = len(df[(df[obj].str.contains('dedal.impl.Assembly')) & (df[kind] == 'DELETE')])
            self.nb_diffAssm_CHG = len(df[(df[obj].str.contains('dedal.impl.Assembly')) & (df[kind] == 'CHANGE')])
            self.nb_diffConfig = len(df[(df[obj].str.contains('dedal.impl.Configuration'))])
            self.nb_notSubst_diffConfig = len(df[(df[obj].str.contains('dedal.impl.Configuration')) & (df[subst] == False)])
            self.nb_Subst_diffConfig = len(df[(df[obj].str.contains('dedal.impl.Configuration')) & (df[subst] == True)])
            self.nb_diffConfig_ADD = len(df[(df[obj].str.contains('dedal.impl.Configuration')) & (df[kind] == 'ADD')])
            self.nb_diffConfig_DEL = len(df[(df[obj].str.contains('dedal.impl.Configuration')) & (df[kind] == 'DELETE')])
            self.nb_diffConfig_CHG = len(df[(df[obj].str.contains('dedal.impl.Configuration')) & (df[kind] == 'CHANGE')])
            self.nb_diffSpec = len(df[(df[obj].str.contains('dedal.impl.Specification'))])
            self.nb_notSubst_diffSpec = len(df[(df[obj].str.contains('dedal.impl.Specification')) & (df[subst] == False)])
            self.nb_Subst_diffSpec = len(df[(df[obj].str.contains('dedal.impl.Specification')) & (df[subst] == True)])
            self.nb_diffSpec_ADD = len(df[(df[obj].str.contains('dedal.impl.Specification')) & (df[kind] == 'ADD')])
            self.nb_diffSpec_DEL = len(df[(df[obj].str.contains('dedal.impl.Specification')) & (df[kind] == 'DELETE')])
            self.nb_diffSpec_CHG = len(df[(df[obj].str.contains('dedal.impl.Specification')) & (df[kind] == 'CHANGE')])
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

    def actualIncrement(self):
        str = "broadleaf-"
        if self.new_v[len(str)+1:].split(".")[0] != self.old_v[len(str)+1:].split(".")[0]:
            return Increment.MAJOR
        if self.new_v[len(str)+1:].split(".")[1] != self.old_v[len(str)+1:].split(".")[1]:
            return Increment.MINOR
        return Increment.BUILD

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

    def isSubjectToErosion(self):
        if self.shouldBeSubstitutable() & len(self.df_diffs[(self.df_diffs[self.kind] == 'DELETE') & (self.df_diffs[self.subst] == False)])>0:
            return True
        return False

    def isSubjectToDrift(self):
        if ((self.actualIncrement()==Increment.BUILD and self.proposeIncrement()==Increment.MINOR) or \
                (self.actualIncrement()==Increment.MINOR and self.proposeIncrement()==Increment.MAJOR and \
                 len(self.df_diffs[(self.df_diffs[self.kind] == 'DELETE')])==0)):
            return True
        return False

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

def export_result(tous_mes_objets):
    df = []
    for obj in tous_mes_objets:
        dico = {"old": obj.old_v,
                "new": obj.new_v,
                "nbDiffs_ADD": obj.nb_diffs_ADD,
                "nbDiffs_DEL": obj.nb_diffs_DEL,
                "nbDiffs_CHG": obj.nb_diffs_CHG,
                "nbDiffs": obj.nb_diffs,
                "nb_diffParam_ADD": obj.nb_diffParam_ADD,
                "nb_diffParam_DEL": obj.nb_diffParam_DEL,
                "nb_diffParam_CHG": obj.nb_diffParam_CHG,
                "nb_diffParam": obj.nb_diffParam,
                "nb_notSubst_diffParam": obj.nb_notSubst_diffParam,
                "nb_Subst_diffParam": obj.nb_Subst_diffParam,
                "nb_diffSign_ADD": obj.nb_diffSign_ADD,
                "nb_diffSign_DEL": obj.nb_diffSign_DEL,
                "nb_diffSign_CHG": obj.nb_diffSign_CHG,
                "nb_diffSign": obj.nb_diffSign,
                "nb_notSubst_diffSign": obj.nb_notSubst_diffSign,
                "nb_Subst_diffSign": obj.nb_Subst_diffSign,
                "nb_diffIntType_ADD": obj.nb_diffIntType_ADD,
                "nb_diffIntType_DEL": obj.nb_diffIntType_DEL,
                "nb_diffIntType_CHG": obj.nb_diffIntType_CHG,
                "nb_diffIntType": obj.nb_diffIntType,
                "nb_notSubst_diffIntType": obj.nb_notSubst_diffIntType,
                "nb_Subst_diffIntType": obj.nb_Subst_diffIntType,
                "nb_diffInt_ADD": obj.nb_diffInt_ADD,
                "nb_diffInt_DEL": obj.nb_diffInt_DEL,
                "nb_diffInt_CHG": obj.nb_diffInt_CHG,
                "nb_diffInt": obj.nb_diffInt,
                "nb_notSubst_diffInt": obj.nb_notSubst_diffInt,
                "nb_Subst_diffInt": obj.nb_Subst_diffInt,
                "nb_diffCompType_ADD": obj.nb_diffCompType_ADD,
                "nb_diffCompType_DEL": obj.nb_diffCompType_DEL,
                "nb_diffCompType_CHG": obj.nb_diffCompType_CHG,
                "nb_diffCompType": obj.nb_diffCompType,
                "nb_notSubst_diffCompType": obj.nb_notSubst_diffCompType,
                "nb_Subst_diffCompType": obj.nb_Subst_diffCompType,
                "nb_diffCompInst_ADD": obj.nb_diffCompInst_ADD,
                "nb_diffCompInst_DEL": obj.nb_diffCompInst_DEL,
                "nb_diffCompInst_CHG": obj.nb_diffCompInst_CHG,
                "nb_diffCompInst": obj.nb_diffCompInst,
                "nb_notSubst_diffCompInst": obj.nb_notSubst_diffCompInst,
                "nb_Subst_diffCompInst": obj.nb_Subst_diffCompInst,
                "nb_diffCompClass_ADD": obj.nb_diffCompClass_ADD,
                "nb_diffCompClass_DEL": obj.nb_diffCompClass_DEL,
                "nb_diffCompClass_CHG": obj.nb_diffCompClass_CHG,
                "nb_diffCompClass": obj.nb_diffCompClass,
                "nb_notSubst_diffCompClass": obj.nb_notSubst_diffCompClass,
                "nb_Subst_diffCompClass": obj.nb_Subst_diffCompClass,
                "nb_diffAttr_ADD": obj.nb_diffAttr_ADD,
                "nb_diffAttr_DEL": obj.nb_diffAttr_DEL,
                "nb_diffAttr_CHG": obj.nb_diffAttr_CHG,
                "nb_diffAttr": obj.nb_diffAttr,
                "nb_notSubst_diffAttr": obj.nb_notSubst_diffAttr,
                "nb_Subst_diffAttr": obj.nb_Subst_diffAttr,
                "nb_diffCompRole_ADD": obj.nb_diffCompRole_ADD,
                "nb_diffCompRole_DEL": obj.nb_diffCompRole_DEL,
                "nb_diffCompRole_CHG": obj.nb_diffCompRole_CHG,
                "nb_diffCompRole": obj.nb_diffCompRole,
                "nb_notSubst_diffCompRole": obj.nb_notSubst_diffCompRole,
                "nb_Subst_diffCompRole": obj.nb_Subst_diffCompRole,
                "nb_diffAssm_ADD": obj.nb_diffAssm_ADD,
                "nb_diffAssm_DEL": obj.nb_diffAssm_DEL,
                "nb_diffAssm_CHG": obj.nb_diffAssm_CHG,
                "nb_diffAssm": obj.nb_diffAssm,
                "nb_notSubst_diffAssm": obj.nb_notSubst_diffAssm,
                "nb_Subst_diffAssm": obj.nb_Subst_diffAssm,
                "nb_diffConfig_ADD": obj.nb_diffConfig_ADD,
                "nb_diffConfig_DEL": obj.nb_diffConfig_DEL,
                "nb_diffConfig_CHG": obj.nb_diffConfig_CHG,
                "nb_diffConfig": obj.nb_diffConfig,
                "nb_notSubst_diffConfig": obj.nb_notSubst_diffConfig,
                "nb_Subst_diffConfig": obj.nb_Subst_diffConfig,
                "nb_diffSpec_ADD": obj.nb_diffSpec_ADD,
                "nb_diffSpec_DEL": obj.nb_diffSpec_DEL,
                "nb_diffSpec_CHG": obj.nb_diffSpec_CHG,
                "nb_diffSpec": obj.nb_diffSpec,
                "nb_notSubst_diffSpec": obj.nb_notSubst_diffSpec,
                "nb_Subst_diffSpec": obj.nb_Subst_diffSpec,
                "shoulBeSubstitutable": obj.shouldBeSubstitutable(),
                "isSubstitutable": obj.isSubstitutable(),
                "actualIncrement": obj.actualIncrement(),
                "proposedIncrement": obj.proposeIncrement(),
                "isSubjectToErosion": obj.isSubjectToErosion(),
                "isSubjectToDrift": obj.isSubjectToDrift()
                }
        df.append(dico)
    df = pd.DataFrame(df)
    df = df.sort_values(by=obj.old).reset_index(drop=True)
    df.to_csv('./result.csv', sep=',')
    return df