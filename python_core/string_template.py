"""
- Use Template when you just want to substrings the values, you don't need formatting.
- Templates are secure compared to .format()

https://www.geeksforgeeks.org/template-class-in-python/
"""

from string import Template

students = [('Ram', 90), ('Ankit', 78), ('Bob', 92)]

template = Template('Hi $name, you have got $marks marks')

for student in students:
    print(template.substitute(name=student[0], marks=student[1]))
