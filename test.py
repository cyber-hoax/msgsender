import requests
import pandas as pd

# Api compnay url
url = "https://www.fast2sms.com/dev/bulkV2"



# excel sheet location
filedata = pd.read_excel('C:\\Users\\rauna\Downloads\\datas.xlsx')


# put the column name which data you want example i took number column data
numbers= filedata['number'].values.tolist()


# put your message  in message section 
payloads = {
            'message': 'hello world sb bardhiya hai ',
            'language' : 'english',
            'route': 'v3',
            'numbers': numbers,
}


# note if it doesn't work xldr error trhen use engine = openpyxl


headers = {
    'authorization': "IWqXhvA1Jf4BbPadkG0xgntzmjEDcMZ8Y7Vpe5iSURN2CysKHFCSeKvWpPgjDxYQsB0GUT64JL9mRhEq",
    'Content-Type': "application/x-www-form-urlencoded",
    'Cache-Control': "no-cache",
    }

response = requests.request("POST", url, data=payloads, headers=headers)

print(response.text)
