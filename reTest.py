import re


p=re.compile(r'\d+')
print(p.findall('one1two2three3four4'))
q=re.compile(r'<td data-toggle="tooltip" data-placement="left" title="password_pos">(\d+)</td>')
print(q.findall('<td data-toggle="tooltip" data-placement="left" title="password_pos">112345</td>'))
