import nltk
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


def getArticle(words):
    if not isNounPhrase(words):
        return "not noun phrase"
    if isDemonstrativePronounOrEachBefore(words):
        return "demonstrative pronoun or each"
    if isProperNoun(words):
        return "proper noun"
    if isPronoun(words):
        return "pronoun"
    if not isSingular(words):
        return "plural"
    if isFirstVowelSound(words):
        return "an"
    return "a"

# If it is noun phrase, return True
def isNounPhrase(words):
    token = nltk.word_tokenize(words)
    tag = nltk.pos_tag(token)
    print(tag)
    if not 'NN' in tag[-1][1]:
        print('not noun!')
        return False
    for index, item in enumerate(tag):
        if index == len(tag)-1:
            break
        if item[1] == 'JJ' or item[1] == 'DT' or item[1] == 'PRP$':
            continue
        else :
            print('not noun!!')
            return False

    # print(token)

    print('noun')
    return True

# If it start with demonstrative pronoun or each, return True
def isDemonstrativePronounOrEachBefore(words):
    token = nltk.word_tokenize(words)
    tag = nltk.pos_tag(token)

    if tag[0][1] == 'DT' or tag[0][1] == 'PRP$':
        print('DT')
        return True
    else :
        print('not DT')
        return False

# If it is propernoun, return True
def isProperNoun(words):
    token = nltk.word_tokenize(words)
    tag = nltk.pos_tag(token)

    if 'NNP' in tag[-1][1]:
        print('NNP')
        return True
    else :
        print('not NNP')
        return False

# If it is pronoun, return True
def isPronoun(words):

    return False

# If it is singular, return True
def isSingular(words):
    return True

# If its sound start with vowel sound return True
def isFirstVowelSound(words):
    return True
