include('config.py')

substitutes['%nb'] = '<div id="nb">'
substitutes['nb%'] = '</div>'

substitutes['--'] = '—'

if substitutes['$LANG'] == 'ru':
    substitutes['%MOTO%'] = ''
else:
    substitutes['%MOTO%'] = ''
