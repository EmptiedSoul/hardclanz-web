%!
include('substitutes.py')
preferences['template'] = 'newsite'

preferences['buttons'] = [
('Главная', substitutes['$WEBROOT'] + '/index.html', False),
('Программы', substitutes['$WEBROOT'] + '/software', False),
('Поездки', substitutes['$WEBROOT'] + '/trips', True),
('Разное', substitutes['$WEBROOT'] + '/misc', False)
]

substitutes['%TITLE%'] = 'Поездки'
!%

# Поездки

...
