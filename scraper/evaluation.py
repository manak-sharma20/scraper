import pdfplumber
import re


def extract_vendor_details(pdf_path):

    data = {
        "vendors": [],
        "l1_vendor": "",
        "quoted_price": ""
    }

    full_text = ""

    with pdfplumber.open(pdf_path) as pdf:

        for page in pdf.pages:

            text = page.extract_text()

            if text:
                full_text += text + "\n"

    vendor_matches = re.findall(
        r"Vendor\s*Name[:\-]?\s*(.*)",
        full_text,
        re.IGNORECASE
    )

    if vendor_matches:
        data["vendors"] = vendor_matches

    return data