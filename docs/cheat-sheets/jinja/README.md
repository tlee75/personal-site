# Jinja

###### Test Jinja Locally

```python
from jinja2 import Template

var = '0'
tm = Template("{{ '0' if (passed_var|string) == '0' else '1'")
msg = tm.render(passed_var=var)

print(msg)
```
