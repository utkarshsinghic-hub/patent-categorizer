import pandas as pd
from io import BytesIO


def create_template():

    data = {
        "Publication Number": [],
        "Title": [],
        "Abstract": [],
        "Description": [],
        "Claims": []
    }

    df = pd.DataFrame(data)

    output = BytesIO()

    with pd.ExcelWriter(
        output,
        engine="openpyxl"
    ) as writer:

        df.to_excel(
            writer,
            index=False,
            sheet_name="Patents"
        )

    output.seek(0)

    return output
