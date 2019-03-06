from collections import OrderedDict

glossary = OrderedDict()

glossary['string'] = 'a word'
glossary['variable'] = 'a value'
glossary['loop'] = 'repeated action on something'
glossary['dictionary'] = 'a key-value pair'
glossary['array'] = 'a list of things'
glossary['boolean expression'] = 'an expression that evaluates to true or false'
glossary['key'] = 'first item in a key value dictionary'
glossary['value'] = 'second item in a key value dictionary'


for word, definition in glossary.items():
    print("\n" + word.title() + ": " + definition)
    