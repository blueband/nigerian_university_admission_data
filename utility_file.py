import random

def isOverQuota(studentAgg, programmeQuota, studentranking):
    if True:
        return True
    else:
        return False


def gradeToNumeric(grade, utme=True):
    # This function convert given grade to its equivalent weighted value with consideration to whether student take POST UTME exams or not
    grade = str(grade.upper().strip())
    if utme:
        if grade == 'A':return 10
        elif grade == 'B2':return 9
        elif grade == 'B3':return 8
        elif grade == 'C4':return 7
        elif grade == 'C5':return 6
        elif grade == 'C6': return 5
        else:
            return 0
    else:
        if grade == 'A1':return 4
        elif grade == 'B2':return 3.6
        elif grade == 'B3':return 3.4
        elif grade == 'C4':return 2.8
        elif grade == 'C5':return 2.6
        elif grade == 'C6': return 2.2
        else:
            return 0




def score2Grade(score):
    if score in range(0, 45):
        return 'F'
    elif score in range(45, 50):
        return 'E'
    elif score in range(50,55):
        return 'C6'
    elif score in range(55,60):
        return 'C5'
    elif score in range(60, 70):
        return 'C4'
    elif score in range(70, 75):
        return "B3"
    elif score in range(75, 80):
        return 'B2'
    elif score in range(80, 101):
        return 'A1'
    else:
        return False

        

def jambScoreWiethed(jambscore):
    # This convert Jamb Score to itsequivalent weight
    jambweight = int(jambscore) / 8

    return jambweight




def _getRandomScore(subject):
        lowerscore = 45
        upperscore = 100
        getScore = random.randint(lowerscore, upperscore)
        return getScore



def firstChoiceStatus():
    randomize = random.randint(0, 2)
    if randomize == 2:
        return randomize -1
    else:
        return randomize

def getSortedResult(total_student_data):
    # This function extract all candidate total \
    #  aggregate and return list sorted score
    
    num_student = len(total_student_data)
    counter = 0
    sortedResult = []
    for studentID, data in total_student_data.items():
        sortedResult.append(data[7][1])
        
    return ('List of Score', sorted(sortedResult, reverse=True))

def stRanking(stdata, sortedResult):
    # this function return position of a candidate
    studentOverallRank = dict()
    for key, value in stdata.items():
        data = value[7][1]
        studentOverallRank[key] = sortedResult[1].index(data) + 1
    return studentOverallRank

