'''
Enter xlsx name, sheetNameeet name, and your csv file name
'''
import csv
import xlrd
def converter(ex_name='random name', sh_name='Sheet1', csv_name='untitled'):
    '''
    takes in xlsx and converts in csv
    '''
    try:
        work_book = xlrd.open_workbook(ex_name)
    except:
        print('File name incorrect')
    try:
        sheet_name = work_book.sheet_by_name(sh_name)
    except:
        print('sheetNameeet name error')
    my_csv = open(csv_name, 'w')
    write_book = csv.writer(my_csv, quoting=csv.QUOTE_ALL)

    for row in range(sheet_name.nrows):
        write_book.writerow(sheet_name.row_values(row))
    my_csv.close()
