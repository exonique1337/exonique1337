import json
import random
import re
import urllib.parse
import urllib.request

QUOTES_URL = "https://gist.githubusercontent.com/exonique1337/6a3be99d61af7b7a54321834d992e616/raw/2dbda9df618c2382331344d2ab897dff5353c010/quotes.json"

with urllib.request.urlopen(QUOTES_URL) as response:
    data = json.loads(response.read().decode("utf-8"))

q = random.choice(data)
text = urllib.parse.quote(q["quote"])
author = urllib.parse.quote(q["author"])

new_line = (
    "![Quote](https://quotes-github-readme.vercel.app/api?"
    "type=horizontal&theme=dark"
    f"&quote={text}&author={author}"
    "&quoteColor=ebebeb&authorColor=1793d1"
    "&backgroundColor=0a0a0a&symbolColor=1793d1)"
)

with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

pattern = r"!\[Quote\]\(https://quotes-github-readme\.vercel\.app/api\?[^\)]+\)"
new_content = re.sub(pattern, new_line, content)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_content)

print("Quote updated:", q["quote"])
