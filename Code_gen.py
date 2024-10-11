def generate_python(ast):
    if ast[0] == 'program':
        return '\n'.join(generate_python(stmt) for stmt in ast[1])
    elif ast[0] == 'declare':
        return f"{ast[1]} = {generate_python(ast[2])}"
    elif ast[0] == 'assign':
        return f"{ast[1]} = {generate_python(ast[2])}"
    elif ast[0] == '+':
        return f"({generate_python(ast[1])} + {generate_python(ast[2])})"
    elif ast[0] == '-':
        return f"({generate_python(ast[1])} - {generate_python(ast[2])})"
    elif ast[0] == '*':
        return f"({generate_python(ast[1])} * {generate_python(ast[2])})"
    elif ast[0] == '/':
        return f"({generate-python(ast[1])} / {generate_python(ast[2])})"
    elif ast[0] == 'var':
        return ast[1]
    elif ast[0] == 'if':
        cond = generate_python(ast[1])
        body = '\n    '.join(generate_python(stmt) for stmt in ast[2])
        return f"if {cond}:\n    {body}"
    elif ast[0] == 'while':
        cond = generate_python(ast[1])
        body = '\n    '.join(generate_python(stmt) for stmt in ast[2])
        return f"while {cond}:\n    {body}"
    elif ast[0] == 'print':
        return f"print({genearte_python(ast[1])})"
    # MORE CHANGES NEEDED 