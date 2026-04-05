%!
include('substitutes.py')
preferences['template'] = 'newsite'

preferences['buttons'] = [
('Главная', substitutes['$WEBROOT'] + '/index.html', True),
('Программы', substitutes['$WEBROOT'] + '/software', False),
('Поездки', substitutes['$WEBROOT'] + '/trips', False),
('Разное', substitutes['$WEBROOT'] + '/misc', False)
]
substitutes['%TITLE%'] = 'Главная'
!%

%nb

### ВЕДУТСЯ РАБОТЫ
Сайт готов не полностью. Не удивляйтесь, если что-то не работает или
осталось недописано.

nb%

# Добро пожаловать. Снова.
Это сайт проекта [hardclanz.org](https://hardclanz.org/), а также его создателя, известного под ником emptiedsoul. Здесь публикуются сведения о разработке программ, их исходные коды и документация; отчёты о поездках; записки и размышления на разные темы. (см. разделы)

Предложить свою статью или ответить на существующую можно на почту [emptiedsoul@hardclanz.org](mailto:emptiedsoul@hardclanz.org)

Сайт вдохновлен ресурсами [suckless.org](https://suckless.org/), [cat-v.org](https://cat-v.org/),
[stallman.org](https://stallman.org/), [gnu.org](https://gnu.org/), [lukesmith.xyz](https://lukesmith.xyz).

Подробнее о технической части сайта -- на [странице]($WEBROOT/software/hweb/) в разделе "Программы".

## Свежие статьи:

<table>
<thead>
<tr><th>Дата</th>
<th>Раздел</th>
<th>Заголовок</th></tr>
</thead>
<tbody>
%!
import misc
import datetime
md = ''
articles = misc.get_all_files('.', 'html', True)
for fname, mtime in articles[:15]:
    if 'index.html' in fname:
        continue
    if '~' in fname:
        continue
    md += '<tr>'
    md += f'<td><nobr>{datetime.date.fromtimestamp(mtime)}</nobr></td>'
    if 'software' in fname:
        md += f'<td>Программы</td>'
    elif 'trips' in fname:
        md += f'<td>Поездки</td>'
    elif 'misc' in fname:
        md += f'<td>Разное</td>'
    else:
        md += '<td>Вне раздела</td>'
    header = misc.retrieve_header(fname.replace('html', 'md'))
    md += f'<td><a href="{fname}">{header}</a></td>'
    md += '</tr>'
insert = md
!%
</tbody>
</table>
<style>
table {
    width: 100%;
    text-align: left;
}
</style>

%!
import datetime
now = datetime.datetime.now()
insert = f"Последнее обновление: {now}"
!%


