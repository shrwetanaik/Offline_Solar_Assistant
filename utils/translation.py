from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate

# Load models—ensure to set trust_remote_code=True
en2mr_model = AutoModelForSeq2SeqLM.from_pretrained(
    "ai4bharat/indictrans2-en-indic-1B", trust_remote_code=True
)
en2mr_tokenizer = AutoTokenizer.from_pretrained(
    "ai4bharat/indictrans2-en-indic-1B", trust_remote_code=True
)

mr2en_model = AutoModelForSeq2SeqLM.from_pretrained(
    "ai4bharat/indictrans2-indic-en-1B", trust_remote_code=True
)
mr2en_tokenizer = AutoTokenizer.from_pretrained(
    "ai4bharat/indictrans2-indic-en-1B", trust_remote_code=True
)

# --- English to Marathi (expects input in English) ---

def to_marathi(english_text: str) -> str:
    """Translate English (Latn) → Marathi (Deva)."""
    tagged = "eng_Latn mar_Deva " + english_text
    inputs = en2mr_tokenizer(tagged, return_tensors="pt",max_length=256)
    output = en2mr_model.generate(**inputs)
    return en2mr_tokenizer.batch_decode(output, skip_special_tokens=True)[0]


# --- Marathi to English (expects input in Marathi Devanagari) ---
def to_english(marathi_text: str) -> str:
    """Translate Marathi (Deva) → English (Latn)."""
    tagged = "mar_Deva eng_Latn " + marathi_text
    inputs = mr2en_tokenizer(tagged, return_tensors="pt",max_length=512)
    output = mr2en_model.generate(**inputs)
    return mr2en_tokenizer.batch_decode(output, skip_special_tokens=True)[0]


# --- Roman Marathi to Devanagari ---
def roman_marathi_to_devanagari(text):
    return transliterate(text, sanscript.ITRANS, sanscript.DEVANAGARI)

# --- Roman Marathi to English ---
def roman_marathi_to_english(text):
    marathi_devanagari = roman_marathi_to_devanagari(text)
    return to_english(marathi_devanagari)

# --- English to Roman Marathi (Optional) ---
def marathi_to_roman(text):
    return transliterate(text, sanscript.DEVANAGARI, sanscript.ITRANS)

# ---- EXAMPLES ----

if __name__ == "__main__":
    # English to Marathi
    print("EN→MR:", to_marathi("Why is my solar inverter not turning on?"))

    # Marathi to English
    print("MR→EN:", to_english("माझा सोलर इन्व्हर्टर सुरू का होत नाही?"))

    # Roman Marathi to English
    print("Roman MR→EN:", roman_marathi_to_english("maja solar inverter suru ka hot nahi?"))

    # Marathi Devanagari to Roman script
    print("MR→Roman:", marathi_to_roman("माझा सोलर इन्व्हर्टर सुरू का होत नाही?"))
