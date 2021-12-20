### File with additional functions and constants Ariadne is using ###

# Up-to-date texts
supported_texts = {
    'hello': 'Hi there :)',
    'maria': 'I will always love you, Maria',
    'creator': 'Vladimir of the House Ilyin, the First of His Name, The Unburnt, King of the Andals, the Rhoynar and '
               'the First Men, King of Meereen, Khal of the Great Grass Sea, Protector of the Realm, Lord Regent of '
               'the Seven Kingdoms, Breaker of Chains and Father of Dragons '
}


# Build string of dictionary
def getDictionaryValues(dic):
    res = []
    for cm in dic:
        res.append(str(cm))
    return str(res)[1:len(str(res)) - 1]

### End of 'helpers.py' file ###
