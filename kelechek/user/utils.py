# users/utils.py

from datetime import date
import pytesseract
from PIL import Image


def verify_user(user):
    passport_photo = user.passport_photo

    # Checking if the passport is expired
    if passport_photo.expiration_date < date.today():
        return False, "Your passport has expired. Please upload new passport photos."

    # Extracting text from passport pages
    img1 = Image.open(passport_photo.passport_page_1.path)
    text1 = pytesseract.image_to_string(img1)
    img2 = Image.open(passport_photo.passport_page_2.path)
    text2 = pytesseract.image_to_string(img2)

    # Extract full name and INN from the text
    extracted_full_name = extract_full_name_from_text(text1)

    # Extract INN from the text
    extracted_inn = extract_inn_from_text(text2)

    if extracted_full_name == user.full_name and extracted_inn == user.inn:
        user.is_verified = True
        user.save()
        return True, "Verification successful."

    return False, "Verification failed. The information does not match."


def extract_full_name_from_text(text):
    # TO DO Implement logic to extract full name from the text
    return "Extracted Full Name"


def extract_inn_from_text(text):
    # TO DO Implement logic to extract INN from the text
    return "Extracted INN"
