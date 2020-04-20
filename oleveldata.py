import  time
import random
from utility_file import _getRandomScore, firstChoiceStatus, genderStatus

class StudentOlevelRecord():
    '''This Class generate Random O-level WAEC Result
     
    '''
    from subject_misc import engineering_core_sub, local_language, elective, Compulsory_subject, \
        Art_subject, General_subject, science_elective_subject, \
             science_subject
    
    def __init__(self, Programme):
        self.first_choice = ('First Choice Status :'.replace(' ', '_').lower(),firstChoiceStatus())
        self.gender = genderStatus()
        self.Programme = Programme
        self.studentID = self.uniqueID()
        self._student_olevel_subject = []
        self.get_subjet(self.Programme)

    def uniqueID(self):
        # This Fuction generate aunique identifer for each instantiate object/Student
        prefix = ''
        postfix = ''
        count = 0
        while count < 6:
            for k in range(random.randint(65, 90), random.randint(65, 90)):
                prefix +=chr(k)
                count += 1
        
        count = 0
        while count < 6:
            for k in range(random.randint(1,100), random.randint(1,100)):
                postfix += str(k)
                count += 1
        stdId = prefix[3:9] + postfix[8:14]
        return stdId


    def get_subjet(self, Programme):
        # This function build O level subject from available core, manfatory, elective subjects
        language_option = self.get_random_elective_subject(StudentOlevelRecord.local_language)
        if Programme.lower() == 'Computer Science'.lower():
            science_elective = self.get_random_elective_subject(StudentOlevelRecord.science_elective_subject)
            self._student_olevel_subject = StudentOlevelRecord.science_subject + StudentOlevelRecord.Compulsory_subject
            self._student_olevel_subject.append(science_elective)
            self._student_olevel_subject.append(language_option)

        elif Programme.lower() == 'Computer Engineering'.lower():
            self._student_olevel_subject = StudentOlevelRecord.science_subject \
            + StudentOlevelRecord.Compulsory_subject \
            + StudentOlevelRecord.engineering_core_sub
            
        elif Programme.lower() == 'Art'.lower() :
            pass
        

    def get_random_elective_subject(self,listSubject):
        numsub = len(listSubject)
        randomize = random.randint(0, numsub)

        if randomize == numsub:
            randomize -= randomize
            return listSubject[randomize].replace(' ', '_').lower()
        else:
            return listSubject[randomize].replace(' ', '_').lower()

    

    def _addScore2subject(self):
        subjectScore = dict()
        for subject in self._student_olevel_subject:
            subjectScore[subject.replace(' ', '_').lower()] = _getRandomScore(subject) 
        return (self.studentID, subjectScore, self.first_choice, self.gender)







class OtherData():
    def __init__(self):
        self.catchement_state = ['kwara', 'kogi', 'niger', 'plateua', 'nasarawa', 'benue']
        self.lessAdvEdu = ['sokoto', 'kano', 'borno', 'adamawa', 'kebbi', 'bauchi']      


    def getRanState(self):
        # Generated data is of turple format (1, 27, 2), where index 0 = gender, index 1 = state_of_origin, while index 2 = age
        randomize = random.randint(1,10) - 1
        all_state = self.catchement_state + self.lessAdvEdu 
        return all_state[randomize]

    def getGender(self):
        status = random.randint(1,2) -1 # We need boolean value, where Male =1, Female = 0
        return status


    def getAge(self):
        return random.randint(16,27)


    def CatchmentArea(self, state):
        if state.lower() in  self.catchement_state:
            return 6
        elif state.lower() in self.lessAdvEdu:
            return 2
        else:
            return 1
    
    def dataBucket(self):
        stGender = self.getGender()
        stAge = self.getAge()
        state = self.getRanState()
        stCatchmentArea = self.CatchmentArea(state)
        return (stGender, stCatchmentArea, stAge)


