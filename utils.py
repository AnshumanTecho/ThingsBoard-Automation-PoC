import pandas as pd
import os

def get_credentials_from_sheet(sheet_index=0, column_index=0):
    # This will point to C:\MyTestProject\ProjectFly\utils\pwd.xlsx
    project_root = os.path.dirname(os.path.abspath(__file__))
    excel_path = os.path.join(project_root, "utilys", "pwd.xlsx")
    df = pd.read_excel(excel_path, sheet_name=sheet_index)
    username = df.iloc[0, column_index]
    password = df.iloc[0, column_index + 1]
    return username, password