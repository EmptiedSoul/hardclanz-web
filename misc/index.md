%!
include('substitutes.py')
preferences['template'] = 'newsite'

preferences['buttons'] = [
('Главная', substitutes['$WEBROOT'] + '/index.html', False),
('Программы', substitutes['$WEBROOT'] + '/software', False),
('Поездки', substitutes['$WEBROOT'] + '/trips', False),
('Разное', substitutes['$WEBROOT'] + '/misc', True)
]

substitutes['%TITLE%'] = 'Разное'
!%

# Разное

...
