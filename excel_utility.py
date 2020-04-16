import openpyxl as exel
import os
dir_src = os.path.dirname(__file__)

working_file = dir_src + '\\' + 'studentRecord.xlsx'
def create_workbook():
    # A copy of workbook and one single worksheet is produce to the calling functions

    wkbook = exel.Workbook()
    wsheet = wkbook.active
    return wkbook, wsheet

def creatSubjecteHeader(subjectList):
    wkbook, current_sheet = create_workbook()
    num_columns = len(subjectList)

    initial_column = 0
    while initial_column < num_columns:
        current_sheet.cell(row=1, column=initial_column+1).value = subjectList[initial_column]
        initial_column += 1
    wkbook.save(working_file)

    
def retrievedColhead():
    wkbook = exel.load_workbook(working_file)
    wksheet = wkbook.active

    for row in wksheet.iter_rows(min_row=1, max_row=1,values_only=True):
        return (row, wksheet, wkbook)


def getColnum(colobj, wksheet):
    for cellrows in wksheet.iter_rows():
        for cellrow in cellrows:
            if cellrow.value == colobj:
                return cellrow.column
            

def getUserdata(*args):
    cols, wksheet, wkbook = retrievedColhead()
    num_student = len(args[0])
    data = args[0]
    for col in cols:
        count = 0
        while count < num_student:
            current_key = list(data)[count]
            for user, value in data.items():
                if user != current_key:continue
                else:
                    writeOutData2excel(count+1, user, value, cols, wksheet)
                    count += 1

    
    wkbook.save(working_file)
    # print('i got here after saving your data in the excel file')
    


def writeOutData2excel(*args):
    num_row = args[0] + 1
    key = args[1]
    value = args[2]
    cols    = args[3]
    wksheet = args[4]    
    olevel_sub = value[0]
    first_choice_status = value[1][1]
    jamb_sub = value[2]
    prefered_programme = value[3]
    olevelAggrScore = value[4][1]
    posutmeAggrscore = value[5][1]
    utmeAggr_Score = value[6][1]
    final_score = value[7][1]
    admissiom_status = value[8][1]
    st_age = value[9][2]
    catchemment_status = value[9][0]

    for col in cols:
        if col == 'stunid':
            colId = getColnum(col, wksheet)
            wksheet.cell(row=num_row, column=colId).value = key
        elif col in list(olevel_sub):
            for sub, scr in olevel_sub.items():
                if col == sub:
                    colId = getColnum(col, wksheet)
                    wksheet.cell(row=num_row, column=colId).value = scr
            
        elif col in list(jamb_sub):
            for sub, scr in jamb_sub.items():
                if col == sub:
                    colId = getColnum(col, wksheet)
                    wksheet.cell(row=num_row, column=colId).value = scr
        elif col == 'catchement_area':
            colId = getColnum(col, wksheet)
            wksheet.cell(row=num_row, column=colId).value = catchemment_status
        elif col == 'prefered_programme':
            colId = getColnum(col, wksheet)
            wksheet.cell(row=num_row, column=colId).value = prefered_programme
        elif col == 'offered_programme':
            pass
        elif col == 'oleve_aggr_score':
            colId = getColnum(col, wksheet)
            wksheet.cell(row=num_row, column=colId).value = olevelAggrScore
        elif col == 'utme_aggr_score':
            colId = getColnum(col, wksheet)
            wksheet.cell(row=num_row, column=colId).value = utmeAggr_Score
        elif col == 'postutme_aggr_score':
            colId = getColnum(col, wksheet)
            wksheet.cell(row=num_row, column=colId).value = posutmeAggrscore
        elif col == 'total_aggregate_score':
            colId = getColnum(col, wksheet)
            wksheet.cell(row=num_row, column=colId).value = final_score
        elif col == 'student_age':
            colId = getColnum(col, wksheet)
            wksheet.cell(row=num_row, column=colId).value = st_age
        elif col == 'admission_status':
            colId = getColnum(col, wksheet)
            wksheet.cell(row=num_row, column=colId).value = admissiom_status
        


# writeOutData2excel('k')