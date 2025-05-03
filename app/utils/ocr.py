import pytesseract
import cv2

def extract_text_from_image(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)
    return text

def validate_document_text(text):
    import re
    cpf_match = re.search(r'(\d{3}\.\d{3}\.\d{3}-\d{2})', text)
    name_match = re.search(r'Nome[:\s]+([A-Z ]+)', text, re.IGNORECASE)
    return {
        "cpf": cpf_match.group(1) if cpf_match else None,
        "name": name_match.group(1).strip() if name_match else None
    }