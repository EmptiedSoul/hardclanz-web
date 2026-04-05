import os
import pypandoc as pandoc
import re

substitutes = {}
preferences = {}

def include(filename):
    exec(open(filename).read(), globals(), locals())

def _process_file(filename, template=False, format='html'):
    document = open(filename).read()

    def execute_and_replace(code):
        local_vars = locals()        
        exec(code, globals(), local_vars)
        return local_vars.get('insert', '')

    def replace_match(match):
        return execute_and_replace(match.group(1))

    exec_pattern = r'%!(.*?)!%'
    document = re.sub(exec_pattern, replace_match, document, flags=re.DOTALL)

    for substitute in substitutes:
        document = document.replace(substitute, substitutes[substitute])

#    print(document)

    if template:
        return document
    else:
        return pandoc.convert_text(document, format, format='gfm')

def _reset_globals():
    global substitutes
    global preferences
    substitutes = {}
    preferences = {}

def convert(filename, output=None, format='html'):
    if output == None:
        output = open(filename.replace('md', 'html'), 'w')
    
    _reset_globals()
    html_document = _process_file(filename, format=format)

    if 'template' in preferences:
        substitutes['%DOCCONTENTS%'] = html_document
        html_document = _process_file(preferences['template'], template=True, format=format)
    
    print(html_document, file=output)
    _reset_globals()


