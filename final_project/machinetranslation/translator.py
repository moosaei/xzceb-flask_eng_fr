"Taranslator using IBM watson"
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version='2018-05-01',authenticator=authenticator)
language_translator.set_service_url(url)

def englishtofrench(englishtext):
    "Translat Englist to French"
    if englishtext=="":
        return ""
    translation_new=language_translator.translate(text=englishtext ,model_id='en-fr').get_result()
    frenchtext =translation_new['translations'][0]['translation']
    return frenchtext

def frenchtoenglish(frenchtext):
    "Translate French to English"
    if frenchtext=="":
        return ""
    translation_new=language_translator.translate(text=frenchtext ,model_id='fr-en').get_result()
    englishtext =translation_new['translations'][0]['translation']
    return englishtext
