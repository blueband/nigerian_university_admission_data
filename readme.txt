############ Motivation (April 2020) #######################
Every code line has one story behind the codecraft magic wand. And this scripts had gotten an intersting story.
"The global pandemic of COVID-19 brought in it wake, a change in virtually all human sphere of social interaction.
I am in the process of carrying out Final year project (B Sc.) degree in my university. My project need lot of  university /
applicant data for machine learning project. However, all institution in Nigeria is closed, include my univerity, 
hence i can not access appropriate data during this lockdown, but I need to continue to work on my project. So this script is an attempted to generate
"simulated" admission data that can fit into my Machine learning project."

########### What it Does #########################
This Python script generate simulated admission data for a candidate that appyly for a specific programme,
It allocate Olevel Result, UTME result, POST UTME.
It calculate weighted score each candidate olevel, utme and post-utme and find the totat aggregate score.
It equally determine admission status of student based on calculated parameter for screen

########## How to Instal/Use the Script ###################
Copy entire files in to specific folder, ensure there is not space within
"file path"

1. Open file named "main.py"

from the function called main()
suply the following parameter
Example:
main(number_of_Student, Programme, cutoff_mark)

The function take three paramter of the following type
a.  number_of_Student (int), this detrmine the number of student records that will be generate
b.  programme (string); this is the university programme the candidate are applied to study,
    current, Computer science and Computer Engineering are fully supported
c. cutoff_mark (int), this a baseline score mark, a student must meet before an admission 
    can be offered to such candidate. 
    
The student score is prorate from combination of  core five Olevel subject score converted
to scale (30%), utme score (50%) and postutme(30%) and this checked against the cutoff_mark to
 determine each candiate eligibility for admission. 



########## Supported Programme ##############
As April 17, 2020, Computer Science and Computer engineering based on 
Kwara State Univeritym Malete addmission requirement, are supported, 
more programme will be add later.

################ Output File ###########
Simulated Data will be save into an excel document with same name as programme in the same root where the script is executed


Explanation of Column in the geberated excel file
'stunid'                        : Unique Identification each student, it was aoto-generated
 'sex'                          : gender
'catchement_area'               : applicant catchemnet area status
'state'                         : applicant State of origin
'student_age'                   : applicant Age
'utme_physic'                   : UTME subject
'utme_use_of_english'           : UTME subject
'utme_mathematic'               : UTME subject
'utme_biology'                  : UTME subject
'utme_chemistry'                : UTME subject
'utme_agricultural_science'     : UTME subject
'utme_economics'                : UTME subject
'utme_geography'                : UTME subject
'physics'                       : Olevel subject
'chemistry'                     : Olevel subject
'further_mathematics'           : Olevel subject
'biology'                       : Olevel subject
'agricultural_science'          : Olevel subject
'civic_education'               : Olevel subject
'christian_religion_knowledge'  : Olevel subject
'islamic_studies'       : Olevel subject
'geography'             : Olevel subject
'visual_art'            : Olevel subject
'history'               : Olevel subject
'economics'             : Olevel subject
'goverment'             : Olevel subject
'history'               : Olevel subject
'commerce'              : Olevel subject
'arabic'                : Olevel subject
'general_mathematic'    : Olevel subject
'english_language'  : Olevel subject
'phyical_education' : Olevel subject
'fisheries'         : Olevel subject
'animal_husbandry'  : Olevel subject
'health_education'  : Olevel subject
'yoruba'    : Olevel subject
'igbo'      : Olevel subject
'hausa'     : Olevel subject
'prefered_programme': The desired programme that an applicant wishes to study.
'offered_programme': The actual programme the univerity offered an applicant, this might be different from prefered_programme due to over subscription(over quota)
'olevel_aggr_score' : combination of five core olevel subject multiply by 2/3  20%
'utme_aggr_score', : combination of four UTME score is divide by 8 to convert to 50%
'postutme_aggr_score' : random score is generate and convert to 30%
'total_aggregate_score', applicant total score (olevel_aggr_score, utme_aggr_score, postutme_aggr_score)
'admission_status'  : True indicated student meet the cutoff_mark baseline, while False, indicate unadmission
'student_ranking'   : indicate applicant position compare to other applicant