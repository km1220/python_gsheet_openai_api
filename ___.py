from _utils import _text2Arr
# from _openai import getNewData, getQuestionResults
# from _gspread import readSheet
# ============================================================================================================================

import gspread
from oauth2client.service_account import ServiceAccountCredentials
# ============================================================================================================================

import os
from dotenv import load_dotenv

load_dotenv()
env = {
    "credential_file_name": os.getenv("GOOGLE_SHEET_CREDENTIAL_FILE_NAME"),
    "gsheet_name": os.getenv("GOOGLE_SHEET_NAME"),
    "question_path": os.getenv("QUESTION_PATH"),
    "data_path": os.getenv("DATA_PATH")
}
# ============================================================================================================================

gc = gspread.service_account(filename=env["credential_file_name"])
_gsheet = gc.open(env["gsheet_name"])
# # gsheet = gc.open_by_url("https://docs.google.com/spreadsheets/d/1qK2Ls1uGh7IekOXyKjQmjRJmD7lYyPHRggqW-eNYiqY/")
# # gsheet = gc.open_by_key("1L7cYfMVPIiYPkTYe1bDwKPGfhAJXp8HCeg34Bh7VYl0")
# ============================================================================================================================


global _questions
global _all_data
_questions = """"""
_all_data = {}
# ============================================================================================================================


def getAllQuestions():
    global _questions
    file = open(os.getcwd() + env["question_path"])  # "/question/list.txt"
    arrLines = _text2Arr(file.read())
    _questions = "".join([line + "\n" for line in arrLines])
    return


def getAllDataJSON():
    global _all_data
    data_path = os.getcwd() + env["data_path"]  # "/data"
    files = os.listdir(data_path)
    # print(data_path, files, "\n")

    for (root, dirs, files) in os.walk(data_path):
        for each_name in files:
            if '.txt' in each_name:
                with open(data_path + "\\" + each_name) as txtFile:
                    # result multiline-text with strip()
                    arrLines = _text2Arr(txtFile.read())
                    strResultExamples = "".join(
                        [line + "\n" for line in arrLines])
                    # file name
                    category = os.path.splitext(each_name)[0]
                    # all json data
                    _all_data = {
                        **_all_data,
                        **{category: strResultExamples}
                    }
    return


def deleteAllSheets():
    # delete worksheets
    for key, val in _all_data.items():
        try:
            _gsheet.del_worksheet(worksheet=_gsheet.worksheet(key))
        except:
            continue
    return



# ============================================================================================================================
getAllQuestions()
getAllDataJSON()
# deleteAllSheets()

# for key, val in _all_data.items():
#     # # --------------------------------------------------------------------------------------------------------------
#     wsheet = readSheet(_gsheet, key)
#     getNewData(wsheet, key, val)
#     getQuestionResults(wsheet, _questions, start_at=1, end_at=2, overwrite=True)
#     # # --------------------------------------------------------------------------------------------------------------
