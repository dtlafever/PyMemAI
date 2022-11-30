# PyMemAI

A basic tool for creating and appending mems to your personal [mem.ai](https://mem.ai) account.

## Get Started

1. Create an account with mem.ai if you have not already done so
2. [Generate your API Key](https://mem.ai/flows/api)
3. install requirements
`pip install -r requirements.txt`
3. Create a Mem!
```python
from pymemai import MemAPI

pymem = MemAPI("<INSERT API KEY>")

# The text you want to put into Mem, including using their Mem Markdown
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

Example Output
```
MemID: 10000000-0000-0000-0000-00000000000
MemURL: https://mem.ai/m/XXXXXXXX
```

You can view your created/appended mem by going to the url provided.

## Usage

1. `MemAPI(apiKey: str)`

Intialize Object and add our API Key to the header

2. `createMem(content: str, isRead=False, isArchived=False) -> (memID: str, memURL: str)`

Sends a `POST` request to mem.ai to create a mem with `content` as the data. If the request does not return a 200 status, `memID` and `memURL` will be empty strings. Additionally, `MemAPI.errorMsg` will contain the error mem.ai returned and `MemAPI.statusCode` will hold the HTTP code.

Additionally, if the request was successful, it appends the `memID` to the newly created mem for later use.

3. `def appendToMem(self, memId: str, content: str) -> (memID: str, memURL: str)`

Sends a `POST` request to mem.ai to append to mem with id `memID`. If the request does not return a 200 status, `memID` and `memURL` will be empty strings. Additionally, `MemAPI.errorMsg` will contain the error mem.ai returned and `MemAPI.statusCode` will hold the HTTP code.

## Limitations

- You can only create and append to mems. **No reading mems.**
- Uploading files is not currently supported by Mem.ai
- Certain limitations on [Mem Markdown Format](https://docs.mem.ai/docs/general/mem-markdown-format)
- There is currently no way to obtain Mem IDs for existing mems. To remedy this, everytime a mem is succesfully created, the Mem ID is appended to the newly created mem.

## FAQ

*Help! My mem keeps putting everything in a code block!*
- Make sure you don't have any unintential spaces when doing a multi line string.
```python
# Good
content = """# Title
#Tags
Text"""

# Bad
content = """# Title
    #Tags
    Text"""
```
