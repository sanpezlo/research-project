import re


def read(path):
    with open(path, "r", encoding="utf-8") as file:
        content = file.read()
        return {
            "problem": re.search(r"---\s*\n([\s\S]+?)\n---", content).group(1).strip(),
            "codes": js_codes(content)
        }


def js_codes(content):
    blocks = re.split(r"\n={3,}\n", content)
    js = []

    for block in blocks:
        sections = re.findall(r'```(\w+)\n(.*?)```', block, re.DOTALL)
        initials = []
        transformations = []
        finals = []
        codes = []
        infinities = []

        for lang, code in sections:
            if lang == 'initial':
                initials.append(code)
            elif lang == 'final':
                finals.append(code)
            elif lang == 'transformation':
                transformations.append(code)
            elif lang == 'js':
                clean = re.sub(
                    r"(//.*?$)|(/\*[\s\S]*?\*/)", '', code, flags=re.MULTILINE)
                clean = re.sub(r'\n\s*\n', '\n', clean)
                codes.append(clean)

        codes = transform_init(codes, initials)
        codes = transform_transformations(codes, transformations)
        codes = transform_final(codes, finals)

        js += codes

    return js


def transform_init(codes, initials):
    if not initials:
        return codes

    transforms = []
    for code in codes:
        i = re.search(r'(function\s+\w+\s*\([^)]*\)\s*{)', code).end()
        for initial in initials:
            function = code[:i + 1]
            body = code[i + 1:]
            transforms.append(function + initial + body)
    return transforms


def transform_transformations(codes, transformations):
    if not transformations:
        return codes

    transforms = []
    for code in codes:
        i = re.search(r'while\s*\([^)]*\)\s*\{', code).end()

        for transformation in transformations:
            body = code[:i + 1]
            end = code[i + 1:]
            transforms.append(body + transformation + end)

    return transforms


def transform_final(codes, finals):
    if not finals:
        return codes

    transforms = []
    for code in codes:
        i = re.search(r'while\s*\([^)]*\)\s*\{', code).end()
        brace = 1

        while i < len(code) and brace > 0:
            if code[i] == '{':
                brace += 1
            elif code[i] == '}':
                brace -= 1
            i += 1

        for final in finals:
            body = code[:i + 1]
            end = code[i + 1:]
            transforms.append(body + final + end)

    return transforms
