# PyMemAI

A basic tool for creating and appending mems to your personal mem.ai account.

## Get Started

1. Create an account with mem.ai if you have not already done so
2. [Generate your API Key](https://mem.ai/flows/api)
3. install requirements
`pip install -r requirements.txt`
3. Create a Mem!
```python
from pymemai import MemAPI

pymem = MemAPI("<INSERT API KEY>")

content = """# My first Mem with PyMem!
#PyMem #Python
Here is some text"""

memID, memURL = pymem.createMem(content)

if pymem.statusCode == 200:
    print(f"MemID: {memID}")
    print(f"MemURL: {memURL}")
else:
    print(pymem.errorMsg)
```

You can view your created/appended mem by going to the url provided.

## Limitations

- You can only create and append to mems. **No reading mems.**
- Uploading files is not currently supported by Mem.ai
- Certain limitations on [Mem Markdown Format](https://docs.mem.ai/docs/general/mem-markdown-format)
- There is currently no way to obtain Mem IDs for existing mems. To remedy this, everytime a mem is succesfully created, the Mem ID is appended to the newly created mem.

## FAQ

Help! My mem keeps putting everything in a code block!
- Make sure you don't have any unintential spaces when doing a multy line string.
```
# Good
content = """# Title
#Tags
Text"""

# Bad
content = """# Title
    #Tags
    Text"""
```