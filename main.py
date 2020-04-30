from oleveldata import StudentOlevelRecord, OtherData
from jambdata import JambData
from utility_file import score2Grade, stRanking
from data_interface import get_columnName
from excel_utility import creatSubjecteHeader, getUserdata, writeFilename
import timeit


def main(*args):
    filename = writeFilename(args[1])
    head_column = get_columnName()
    creatSubjecteHeader(head_column, filename)  # Building column of the 
    listobj = []
    counter = 0
    while counter < args[0]:
        Olevel_records = StudentOlevelRecord(args[1])
        Olevel_records = Olevel_records._addScore2subject()
        jambRecords = JambData(Olevel_records[0], Olevel_records[1], args[1], args[2])       # Unique Identity supplied here
        jambdata = jambRecords._addScore2subject()
        partial_data = OtherData()
        o_data = partial_data.dataBucket()
        listobj.append({Olevel_records[0] : (Olevel_records[1], Olevel_records[2], Olevel_records[3], \
        jambdata[1], jambdata[2], jambdata[3], jambdata[4], jambdata[5], jambdata[6], jambdata[7], o_data)})
        counter += 1
    

    getUserdata(listobj, filename, args[3])
    
    

    # print(stRanking(listobj))

    # studentFinalRanking = stRanking(listobj, SortedResult)
    # print('this is ranking data', studentFinalRanking)




# Testing execution time when number candidate to generate is many
# if __name__ =='__main__':
#      import timeit
#      runtimer = timeit.Timer("main(10000, 'Computer engineering', 67, 320)", 'from __main__ import main')
#      print('the code run for : ', runtimer.timeit(number=1), 'millisecods')  

#   This main entry  to run the programme
main(1, 'Computer engineering', 67, 320)