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

########## The script work by user submit the following data as parameter###################
1. number of user you wishes to generate
2. programme applying for by the student (computer science and engineering are supported at moment)
3, the cutoff_mark for such programme


########## Supported Programme ##############
As April 17, 2020, Computer Science and Computer engineering based on 
Kwara State Univeritym Malete addmission requirement, are supported, 
more programme will be add later

################ Output File ###########
Simulated Data will be save into an excel document with same name as programme in the same root where the script is executed


Explanation of Column in the geberated excel file
'stunid'                : Unique Identification each student, it was aoto-generated
 'sex'
'catchement_area'
'state', 
'student_age', 
'utme_physic', 
'utme_use_of_english', 
'utme_mathematic', 
'utme_biology', 
'utme_chemistry', 
'utme_agricultural_science', 
'utme_economics', 
'utme_geography', 
'physics', 
'chemistry', 
'further_mathematics', 
'biology', 
'agricultural_science', 
'civic_education', 
'christian_religion_knowledge', 
'islamic_studies', 
'geography', 
'visual_art', 
'history', 
'economics', 
'goverment', 
'history', 
'commerce', 
'arabic', 
'general_mathematic', 
'english_language', 
'phyical_education', 
'fisheries', 
'animal_husbandry', 
'health_education', 
'yoruba', 
'igbo', 
'hausa', 
'prefered_programme', 
'offered_programme', 
'olevel_aggr_score', 
'utme_aggr_score', 
'postutme_aggr_score', 
'total_aggregate_score', 
'admission_status'
'student_ranking'