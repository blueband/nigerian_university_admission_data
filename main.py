import random
from oleveldata import StudentOlevelRecord, OtherData
from jambdata import JambData
from selection_criteria import convertGrade
from utility_file import score2Grade, getSortedResult, stRanking
from data_interface import get_columnName
from excel_utility import creatSubjecteHeader, getUserdata, writeFilename


def main(num_row, Programme=None, cutoff_mark=None):
    filename = writeFilename(Programme)
    head_column = get_columnName()
    creatSubjecteHeader(head_column, filename)  # Building column of the 
    final_records = dict()
    counter = 0
    while counter < num_row:
        Olevel_records = StudentOlevelRecord(Programme)
        Olevel_records = Olevel_records._addScore2subject()
        jambRecords = JambData(Olevel_records[0], Olevel_records[1], Programme, cutoff_mark)       # Unique Identity supplied here
        jambdata = jambRecords._addScore2subject()
        partial_data = OtherData()
        o_data = partial_data.dataBucket()
        final_records[Olevel_records[0]] = (Olevel_records[1], Olevel_records[2], \
        jambdata[1], jambdata[2], jambdata[3], jambdata[4], jambdata[5], jambdata[6], jambdata[7], o_data)
        counter += 1
    # SortedResult = getSortedResult(final_records)
    # studentFinalRanking = stRanking(final_records, SortedResult)
    getUserdata(final_records, filename)



main(1, 'Computer Engineering', 63)