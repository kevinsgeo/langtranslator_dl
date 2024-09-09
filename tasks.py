from models import TranslationModel
from transformers import T5Tokenizer, T5ForConditionalGeneration

tokenizer = T5Tokenizer.from_pretrained("t5-small", model_max_length=512)   
translator = T5ForConditionalGeneration.from_pretrained("t5-small")

def store_translation(translation):
    model = TranslationModel(text=translation.text, initial_lang=translation.initial_lang, final_lang=translation.final_lang)
    model.save()
    return model.id 

# run translation
def run_translation(translation_id:int):
    model = TranslationModel.get_by_id(translation_id)
    prefix = f"translate {model.initial_lang} to {model.final_lang}: {model.text}"
    input_ids = tokenizer(prefix, return_tensors="pt").input_ids

    outputs = translator.generate(input_ids, max_new_tokens=512)
    translation = tokenizer.decode(outputs[0], skip_special_tokens=True)

    model.translation = translation
    model.save()

# retrieve translation
def find_translation(translation_id:int):
    model = TranslationModel.get_by_id(translation_id)

    translation = model.translation
    if translation is None:
        translation = "Translation is still processing..."

    return translation


