import random
from utility_file import score2Grade
from subject_misc import programme, prioritization
# pogramme = {'computer science': [78, 365], 'computer Engineering': [85, 250], 'Library and Information Science': [72, 400]}

# prioritization = {'Computer Engineering' : 6, 'Computer Science': 5, 'Library and Information Science' : 3 }

def convertGrade(olevelresult):
    subGrade = []
    for subject in olevelresult:
        print('what do we have here : ',subject)
        if type(subject) == 'int':pass
        else:
            if subject[0].startswith == 'Jamb_' or len(subject) != 2:continue
            else:
                grade = score2Grade(subject[1])
                subGrade.append((subject[0], grade))
    return subGrade


