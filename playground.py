css = ""

def add_class(name, body, amount, css):
    curr=""
    for i in range(amount):
        curr += f""".st-key-{name}-{i} {{
    {body}
}}
"""
    return css+"\n"+curr

css = add_class("black_centered", "pipi",5,css)
css = add_class("black_centered", "pipi",5,css)
print(css)