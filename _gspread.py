from gspread_formatting import *
from _utils import _incChr

def readSheet(_gsheet, sheet_name="Sheet1"):
	wsheet = sheet_name
	isSheetExist = False
	for each_sheet in _gsheet.worksheets():
		if each_sheet.title == sheet_name:
			wsheet = _gsheet.worksheet(sheet_name)
			isSheetExist = True
			break
	if isSheetExist == False:
		wsheet = _gsheet.add_worksheet(sheet_name, 1000, 100)
		# set columns width			only when creating new sheet 
		set_column_width(wsheet, 'A', 500)
		endColLetter = _incChr('C', 5)
		set_column_width(wsheet, f'C:{endColLetter}', 300)
	
	return wsheet