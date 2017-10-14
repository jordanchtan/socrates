# refer to https://cloud.google.com/natural-language/docs/reference/libraries#client-libraries-usage-python

from google.cloud import language
import urllib.request
import urllib.parse
import json
import six

## HelpingVerbclass ##

helpingVerbs = ["am ","is ","are ","was ","were ", "could ","should ","would ","can ","shall ",
"will ","may ","might ","must ", "do ","does ","did ", "have ",
"has ","had ", "be ","being ","been "];

def reorder(text):
    thishelpverb = ''
    for helpverb in helpingVerbs:
        if helpverb in text:
            thishelpverb = helpverb
            break
    return thishelpverb + text.replace(thishelpverb,'')
    # not moving first helping verb in sentence to front, soft fix by putting helpingVerbs more commonly found at front of list


## Other Statements ##

def getVerb(text):
    language_client = language.Client()
    if isinstance(text, six.binary_type):
        text = text.decode('utf-8')
    document = language_client.document_from_text(text)
    tokens = document.analyze_syntax().tokens
    for token in tokens:
        # print(u'{}: {}'.format(token.part_of_speech, token.text_content))
        tag = token.part_of_speech
        if tag == "VERB":
            return token.text_content
    return "Error 404"

def getSubject(text):
    language_client = language.Client()
    if isinstance(text, six.binary_type):
        text = text.decode('utf-8')
    document = language_client.document_from_text(text)
    tokens = document.analyze_syntax().tokens
    for token in tokens:
        tag = token.part_of_speech
        if tag == "PRON" or tag == "NOUN":
            return token.text_content
    return "Error 404"

def isSimplePresentTenseVerb(text):
    mashapeurl = 'https://webknox-words.p.mashape.com/words/' + text + '/simplePresent'
    headers = {
            "X-Mashape-Key": "ftQkraKaBNmshLnHBLHAzExn8zzAp1efaAHjsny7vXnbQbergD",
            "Accept": "application/json"
            }
    request = urllib.request.Request(mashapeurl, headers=headers)
    response = urllib.request.urlopen(request).read()
    word = json.loads(response)
    if word.get('simplePresent') == text:
        return True
    return False

def isSingularSubject(text):
    if text == "You" or text == "We" or text == "They":
        return False
    language_client = language.Client()
    if isinstance(text, six.binary_type):
        text = text.decode('utf-8')
    document = language_client.document_from_text(text)
    tokens = document.analyze_syntax().tokens
    for token in tokens:
        word = token.text_content
        base = token.lemma
        if word == base:
            return True
    return False

def getPresentTenseForm(text):
    # Api doesnt work always eg Saved becomes sav
    mashapeurl = 'https://webknox-words.p.mashape.com/words/' + text + '/simplePresent'
    headers = {
            "X-Mashape-Key": "ftQkraKaBNmshLnHBLHAzExn8zzAp1efaAHjsny7vXnbQbergD",
            "Accept": "application/json"
            }
    request = urllib.request.Request(mashapeurl, headers=headers)
    response = urllib.request.urlopen(request).read()
    word = json.loads(response)
    return word.get('simplePresent') + ' '

## language client for the boolean functions may not need to tokenise as only 1 item


def changeStatement(text):
    verb = getVerb(text)
    subject = getSubject(text)
    singular = isSingularSubject(subject)
    simplePresent = isSimplePresentTenseVerb(verb)
    if singular and simplePresent:
        changeVerb = verb[:-1]
        return "Does " + text.replace(verb,changeVerb,1)
    elif not singular and simplePresent:
        return "Do " + text
    elif not simplePresent:
        verbinpresent = getPresentTenseForm(verb)
        return "Did " + text.replace(verb,verbinpresent,1)
    else:
        return "Sorry! Did not manage to interpret texting :("

## main function

def containsAHelpVerb(text):
    for helpverb in helpingVerbs:
        if helpverb in text:
            return True
    return False

def main(text):
    if containsAHelpVerb(text):
        return reorder(text)
    else :
        return changeStatement(text)
