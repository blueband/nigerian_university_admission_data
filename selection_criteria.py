import random
from subject_misc import programme_max_quota, prioritization
from oleveldata import StudentOlevelRecord

class OfferedProgramme(StudentOlevelRecord):
    '''This class look up appropriate programme for qualifying candidate
    it either recommeded the original programme or alternative
    '''
    def __init__(self,*args):
        ''' admi_status Boolean, student_ranking position, carrying capacity of
        the programmme
        '''
        super().__init__(args[0])
        self.adm_status = args[1]
        self.student_ranking = args[2]
        self.programme_quota = args[3]
        self.return_offered_programme()
    
    def getalterProgramme(self, *args):
        # This function use priority key to get the list of all alternative programme
        available_programme = []
        priorityKey = None
        for key, value in args[0].items():
            if key.lower() != self.Programme.lower():continue
            else:
                priorityKey = value
        
        for key, value in args[0].items():
            if value >= priorityKey:continue
            else:
                available_programme.append(key)
        return available_programme



    def getStatus(self, *args):
        if args[0] == True and args[1] <= args[2]:
            return True
        else:
            return False

    def return_offered_programme(self):
        # Return Recommeded alternative programme
        status = self.getStatus(self.adm_status, self.student_ranking, self.programme_quota)
        if status:
            return self.Programme
        else:
            list_prog = self.getalterProgramme(prioritization)
            recom_programme = self.getrandomElement(list_prog)
            return recom_programme
        

    def getrandomElement(self, elements):
        # Generate random alternative programme, need to modify to recommeded programe base on rules
        max_lenght = len(elements)
        randomize = random.randint(0, max_lenght)
        if randomize == max_lenght:
            randomize = randomize - 1
            return elements[randomize]
        else:
            return elements[randomize]
            
