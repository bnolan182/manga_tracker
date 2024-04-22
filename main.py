import gspread
from google.oauth2.service_account import Credentials

scopes = [
    "https://www.googleapis.com/auth/spreadsheets"
]

creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
client = gspread.authorize(creds)

sheet_id = "1kOwxCVxosP8gFZpjg8wh1DDHSjhRXku8DeXSA9W3DX8"
sheet = client.open_by_key(sheet_id)

# Test connection to sheet
values_list = sheet.sheet1.row_values(1)
print(values_list)