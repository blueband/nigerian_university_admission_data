from subject_misc import *

def get_row(dataobject):
    return len(dataobject)


def utmeSub(subjectlist):
    subjects = []
    for sub in subjectlist:
        sub.strip()
        subjects.append('utme_' + sub.replace(' ', '_').lower())
    return subjects

def olevelSub(subjectlist):
    subjects = []
    for sub in subjectlist:
        sub.strip()
        subjects.append(sub.replace(' ', '_').lower())
    return subjects

def get_columnName():
    column_data = []
    
    # General Data
    column_data.append('StunID'.lower())
    column_data.append('sex'.lower())
    column_data.append('catchement_area'.lower())
    column_data.append('state'.lower())
    column_data.append('Student Age'.replace(' ', '_').lower())

    # UTME Subject
    column_data.extend(utmeSub(core_science_subject))
    column_data.extend(utmeSub(core_Subject))
    column_data.extend(utmeSub(elective_subject))
    
    # OLEVEL Subject
    column_data.extend(olevelSub(science_subject))
    column_data.extend(olevelSub(engineering_core_sub))
    column_data.extend(olevelSub(science_elective_subject))
    column_data.extend(olevelSub(General_subject))
    column_data.extend(olevelSub(Art_subject))
    column_data.extend(olevelSub(Compulsory_subject))
    column_data.extend(olevelSub(elective))
    column_data.extend(olevelSub(local_language))

    # Selection Data

    column_data.append('Prefered Programme'.replace(' ', '_').lower())
    column_data.append('Offered Programme'.replace(' ', '_').lower())
    column_data.append('Olevel aggr score'.replace(' ', '_').lower())
    column_data.append('utme aggr score'.replace(' ', '_').lower())
    column_data.append('POSTUTME aggr score'.replace(' ', '_').lower())
    column_data.append('total aggregate Score'.replace(' ', '_').lower())
    column_data.append('Admission Status'.replace(' ', '_').lower())
    column_data.append('Student Ranking'.replace(' ', '_').lower())


    
    return column_data