import re

def read(path):
    with open(path, "r", encoding="utf-8") as file:
        content = file.read()
        return {
            "problem": re.search(r"---\s*\n([\s\S]+?)\n---", content).group(1).strip(),
            "codes": js_codes(content)
        }

def js_codes(content):
    return re.findall(r"```js\s*([\s\S]*?)\s*```", content)