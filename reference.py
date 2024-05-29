str = r"" # paste from desmos here

rules = [
    [r"\left", ""],
    [r"\right", ""],
    [r"_", ""],
    # multiply
    [r"\cdot", "*"],
    # division
    [r"\frac{", "("],
    [r"}{", ")/("],
    # special functions
    [r"\sqrt", "sqrt"],
    [r"\sin", "sin"],
    [r"\cos", "cos"],
    [r"\ln", "ln"],
    # cleanup all remaining curly brackets
    # make sure this is at the end
    [r"{", "("],
    [r"}", ")"]
]

for rule in rules:
    str = str.replace(rule[0], rule[1])

print(str)
