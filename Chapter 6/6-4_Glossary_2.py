glossary = {
    'string': 'a word',
    'variable': 'a value',
    'loop': 'repeated action on something',
    'dictionary': 'a key-value pair',
    'array': 'a list of things',
    'boolean expression': 'an expression that evaluates to true or false',
    'key': 'first item in a key value dictionary',
    'value': 'second item in a key value dictionary',
}

for word, definition in glossary.items():
    print("\n" + word.title() + ": " + definition)
    
    