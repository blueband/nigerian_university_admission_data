from excel_utility import creatSubjecteHeader

o_level_subject = ['COMMERCE','  FINANCIAL','ACCOUNTING',	'CHRISTIAN RELICGIOUS STUDIES', 'ECONOMICS','GEOGRAPHY', 'GOVERNMENT', 'ISLAMIC STUDIES', 	'LITERATURE IN ENGLISH','CIVIC EDUCATION','ENGLISH LANGUAGE','FRENCH', 	'HAUSA', 'IGBO','YORUBA','FURTHER MATHEMATICS',	'GENERAL MATHEMATICS','AGRICULTURAL SCIENCE', 'BIOLOGY', 'CHEMISTRY', 'PHYSICS', 'HEALTH EDUCATION', 'TECHNICAL DRAWING', 'FOODS AND NUTRITION', 'VISUAL ART']
other_column = ['jamb_english', 'jamb_mathematics', 'jamb_further_mathematics', 'jamb_chemistry', 'jamb_physics','number_of_exam_seating', 'postutme_score', 'student_aggregate_ranking' 'first_choice', 'programme_applied_for', 'catchement_area', 'gender', 'is_quota_exceeded', 'programme_alloted']
def headFormatter(subjetList):
    subjetList = subjetList
    subjectBucket = []
    for subject in subjetList:
        subjectBucket.append(subject.lower().strip())

    return subjectBucket





other_header = headFormatter(other_column)
o_level_subject.extend(other_header)
subjectsBuckect = headFormatter(o_level_subject)
creatSubjecteHeader(subjectsBuckect)

print('i got here')