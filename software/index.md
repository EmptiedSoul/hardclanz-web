%!
include('substitutes.py')
preferences['template'] = 'newsite'

preferences['buttons'] = [
('Главная', substitutes['$WEBROOT'] + '/index.html', False),
('Программы', substitutes['$WEBROOT'] + '/software', True),
('Поездки', substitutes['$WEBROOT'] + '/trips', False),
('Разное', substitutes['$WEBROOT'] + '/misc', False)
]

substitutes['%TITLE%'] = 'Программы'
!%

# Программы

...
