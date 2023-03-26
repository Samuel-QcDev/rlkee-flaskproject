"""
Docstring
"""
#import json
import os
from ibm_watson import LanguageTranslatorV3, ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    """ Function to translate text from English to French
    Args:
        english_text (str): text to be translated
    Returns:
        _type_: _description_
    """
    try:
        french_text = language_translator.translate(
            text=english_text.lower(),
            model_id='en-fr').get_result()['translations'][0]['translation']
        return french_text
    except ApiException as ex:
        return "Method failed with status code " + str(ex.code) + ": " + ex.message

def french_to_english(french_text):
    """ This frunction translates french to english
    Args:
        french_text (str): french text to be translated
    Returns:
        str: english translation
    """
    try:
        english_text = language_translator.translate(
            text=french_text.lower(),
            model_id='fr-en').get_result()['translations'][0]['translation']
        return english_text
    except ApiException as ex:
        return "Method failed with status code " + str(ex.code) + ": " + ex.message
