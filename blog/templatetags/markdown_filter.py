from django import template
import re

register = template.Library()

@register.filter
def markdown(value):
    value = re.sub(r'\*(.*?)\*', r'<b>\1</b>', value)  # bold
    value = re.sub(r'_(.*?)_', r'<i>\1</i>', value)  # italic
    value = re.sub(r'&(.*?)&', r'<h4><hr>\n\1</h4>', value)  # heading 4
    value = re.sub(r'```(.*?)```', r'<pre style="background-color: lightgray;">\1</pre>', value)  # line code
    return value