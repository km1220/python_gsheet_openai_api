from dotenv import load_dotenv
from _utils import _text2Arr
import os
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
amount_data_generate = os.getenv("AMOUNT_DATA_GENERATE")
if amount_data_generate == "" or amount_data_generate == None or amount_data_generate.isnumeric() != False or amount_data_generate > 500 or amount_data_generate < 1:
    amount_data_generate = 5


def getNewData(_wsheet, category, example):
    maxRows = len(_wsheet.col_values(1))
    prompt = f"""Get only {amount_data_generate} results similar with below examples
- Categories: {category}
- Instagram story catchy headlines
- LinkedIn post
- YouTube video script

Examples:
{example}

Result|Source site: --- | ---
"""
    print(prompt)

    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.8,
            max_tokens=1000,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        result_choice = response["choices"][0]
        arr_result = _text2Arr(result_choice["text"])
        for n, each in enumerate(arr_result):
            print(n, each)
            _wsheet.update_cell(maxRows + n + 1, 1, each)
            # wsheet.cell(row=n, column=1).value = each
    except:
        print('getting new data :  Error!')


def getQuestionResults(_wsheet, question_text, start_at="SHEET_START", end_at="SHEET_END", overwrite=False):
    maxRows = len(_wsheet.col_values(1))
    startRow = 1 if start_at == "SHEET_START" else start_at
    endRow = maxRows if end_at == "SHEET_END" else end_at

    template_prompt = f"""Question:
{question_text}

Brief and clear answer with numbering:
"""

    try:
        # for i in range(1, 2):
        # for i in range(oldMaxRows + 1, maxRows+1):
        # for i in range(1, maxRows+1):
        for i in range(startRow, endRow + 1):
            _each = _wsheet.cell(i, 1).value
            if _each == None:
                continue
            if overwrite == False and _wsheet.cell(i, 3).value != None:
                continue

            prompt = f"{_each}\n\n" + template_prompt
            print(prompt)

            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=prompt,
                temperature=0.5,
                max_tokens=250,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0
            )
            result_choice = response["choices"][0]
            # print(result_choice)
            print(i, ": ", _each, "\n================================================================================\n")

            arr_result = _text2Arr(result_choice["text"])
            for n, each in enumerate(arr_result):
                print(each)
                _wsheet.update_cell(i, 3 + n, each)
            print(
                "--------------------------------------------------------------------------------------------\n")
    except:
        print('getting question result :  Error!')
