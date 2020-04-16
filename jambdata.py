from utility_file import _getRandomScore, score2Grade, gradeToNumeric
import random

class JambData:
    from subject_misc import core_science_subject, core_Subject, elective_subject

    def __init__(self, studentID, olevelScore, Programme, cutoff_mark):
        self.studentID = studentID
        self.cutoff_mark = cutoff_mark
        self.Programme = Programme
        self.olevelScore = olevelScore 
        self.studentSubject = []
        self._getsubjectComb()

    def _getsubjectComb(self):
        num_sub = len(JambData.elective_subject)
        if self.Programme.lower() == 'Computer Science'.lower():
            self.studentSubject.extend(JambData.core_Subject)
            self.studentSubject.extend(JambData.core_science_subject)
            if num_sub == 5:
                num_sub = num_sub - 1
                randomSubject = random.randint(0, num_sub)
                randomSubject = JambData.elective_subject[randomSubject]
                self.studentSubject.append(randomSubject)
            else:
                randomSubject = random.randint(0, num_sub)
                randomSubject = JambData.elective_subject[randomSubject]
                self.studentSubject.append(randomSubject)
        elif self.Programme.lower() == 'Computer Engineering'.lower():
            self.studentSubject.extend(JambData.core_Subject)
            self.studentSubject.extend(JambData.core_science_subject)
            for subject in JambData.elective_subject:
                if subject.lower() != 'chemistry':continue
                else:
                    self.studentSubject.append(subject.lower())

        

    def _addScore2subject(self):
        pstUtmeScrObj = PostUtme(self.Programme, self.cutoff_mark,self.studentID)
        pstUtmeScr = ('PostUtme Score :',pstUtmeScrObj.getPostUtmeScore())
        OlevelAggrScore = ('OlevelAggr Score :', pstUtmeScrObj.olevelAggregate(self.olevelScore))
        subjectScore = dict()
        for subject in self.studentSubject:
            subjectScore['utme_' + subject.replace(' ', '_').lower()] = _getRandomScore(subject) # This little hack was done in order to distinguished between olevel and Jamb subject
        jambAccScore = ('JambAggr Score :',pstUtmeScrObj.calcJambaggregate(subjectScore))
        finalweight = ('Final St Aggregate :', pstUtmeScrObj.finalPorate())
        stAdmistatus = ('Qualified for Admsission : ', pstUtmeScrObj.admitStaus())
        
        return (self.studentID, subjectScore, self.Programme, OlevelAggrScore, pstUtmeScr, jambAccScore, finalweight, stAdmistatus)


class PostUtme():
    def __init__(self, programme, cutoff_mark, uniquID=None ):
        self.uniquId = uniquID
        self.programme = programme
        self.Jscore_accumulator = 0
        self.Olscore_accumulator = 0
        self.postUtme_weight = 0
        self.studentWeight = 0
        self.cutoff_mark = cutoff_mark


    def getPostUtmeScore(self):
        ramdomize = random.randint(1,101)
        self.postUtme_weight = int(ramdomize * 0.3)
        return self.postUtme_weight

    def calcJambaggregate(self,jSubjectData):
        # Jscore_accumulator = 0
        for jsubject, jscore in jSubjectData.items():
            self.Jscore_accumulator += jscore
        self.Jscore_accumulator = int(self.Jscore_accumulator / 8)
        return self.Jscore_accumulator

    def olevelAggregate(self, olevelsubdata):
        Olscore_accumulator = 0
        for olsubject, olscore in olevelsubdata.items():
            Olscore_accumulator += gradeToNumeric(score2Grade(olscore), False)
        self.Olscore_accumulator = int(Olscore_accumulator)
        return self.Olscore_accumulator


    def finalPorate(self):
        self.studentWeight = self.Olscore_accumulator + self.Jscore_accumulator + self.postUtme_weight
        return self.studentWeight


    def admitStaus(self):
        if self.studentWeight >= self.cutoff_mark:
            return True
        else:
            return False
