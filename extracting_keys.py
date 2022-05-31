marks={'python':3,'maths':34,'english':34,'physics':34}
out={}
for keys in marks:
    if marks[keys] in out:
        out(marks[keys]).append(keys)
    else:
        out(marks[keys])==keys
