from pathlib import Path
import datetime
import json
import os

date = datetime.date.today()

def case_data(case_number, crime_type: str):
    Path(f"case[{case_number}]_Data[{date}]").mkdir(exist_ok=True, parents=True)