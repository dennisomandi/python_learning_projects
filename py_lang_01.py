def greet(lang) :
    if lang == 'es' :
        return 'Hola'
    elif lang == 'fr' :
        return 'Bonjouir'
    else:
        return 'Hello'

print(greet('en'),'Glenn')
print(greet('es'),'Sally')
print(greet('fr'),'Hillary')