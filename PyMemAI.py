# Created by Derek LaFever, 2022.

import requests

class MemAPI:
    """
    Create and append mems to Mem.ai

    Mem.ai API Documentation: https://docs.mem.ai/docs/api/mems/create

    Class Variables
    ---------------
    @BASE_URL
        stores the base mem.ai url for API calls
    @MemResponseType
        used for type hinting, this variable should hold the mem ID
        and mem URL for a given mem

    Instance Variables
    ------------------
    @self.HEADERS
        the header mem.ai expects when recieving API calls. This header
        will hold your API Key
    @self.statusCode
        the last requests HTML status code.
    @self.errorMsg
        if the last request was not a 200 status, this variable will contain
        the error message mem.ai sent back as a response.
    @self.memID
        the ID of the last mem that was created or appended to. Used to later append
        to an already created mem.
    @self.memURL
        the url to see the new mem that was created/appended.

    """

    BASE_URL = "https://api.mem.ai/v0/mems"
    MemResponseType = tuple[str, str]

    def __init__(self, apiKey: str):
        """
        Takes an API Key obtained from https://mem.ai/flows/api
        and stores it in `headers` with the correct format for later use.

        @apiKey: str
            the api key obtained form mem.ai/flows/api
        """
        self.HEADERS = {"Content-Type": "application/json",
                        "Authorization": f"ApiAccessToken {apiKey}"}
        self.statusCode = 200
        self.errorMsg   = ""
        self.memID      = ""
        self.memURL     = ""

    def createMem(self, content: str, isRead=False, isArchived=False) -> MemResponseType:
        """
        Creates a mem. Returns the Mem ID and URL to the mem.
        Additionally appends the Mem ID to the created mem if
        it was successful in creating.

        Allows for mem.ai's version of markdown: https://docs.mem.ai/docs/general/mem-markdown-format

        @content: str
            the text you want to store in mem. Can be markdown
        @isRead: bool
            Denotes if this mem should be considered already read
        @isArchived: bool
            Denotes if this mem should be auto archived
        """
        payload = {"content": content,
                   "isRead": isRead,
                   "isArchived": isArchived}

        response = requests.post(MemAPI.BASE_URL, headers=self.HEADERS, json=payload)
        self.__processResponse(response)

        # store the memID inside of the file so we can append to it later
        # if we wish to.
        if self.statusCode == 200:
            self.appendToMem(self.memID, f"**MemID: {self.memID}**")

        return (self.memID, self.memURL)

    def appendToMem(self, memId: str, content: str) -> MemResponseType:
        """
        Appends to an existing mem. Prints out the Mem ID and URl to the mem.

        Allows for mem's version of markdown: https://docs.mem.ai/docs/general/mem-markdown-format

        @content: str
        the text you want to store in mem. Can be markdown
        @isRead: bool
        Denotes if this mem should be considered already read
        @isArchived: bool
        Denotes if this mem should be auto archived
        """
        url = f"{MemAPI.BASE_URL}/{memId}/append"
        payload = {"content": content}

        response = requests.post(url, headers=self.HEADERS, json=payload)
        self.__processResponse(response)

        return (self.memID, self.memURL)

    def __processResponse(self, response: requests.Response):
        """
        Updates MemID, MemURL for mem that was created or appended.
        Also updates self.statusCode based on the `response`.

        stores error messge from mem.ai if statusCode is not 200
        and sets (MemID, MemURL) to empty strings.

        @response: requests.Response
        the response object generated from a POST requests to mem.ai
        """
        rJson = response.json()

        self.memID = ""
        self.memURL = ""
        self.statusCode = response.status_code
        self.errorMsg = ""

        if self.statusCode != 200:
            self.errorMsg = rJson['error']['message']
        else:
            self.memID  = rJson['id']
            self.memURL = rJson['url']

if __name__ == "__main__":
    from getpass import getpass # don't import this class unless we are using this file as main
    apiKey = getpass(prompt="Input Mem API Key: ")

    pymem = MemAPI(apiKey)

    content = """# Test Title
#PyMem #Test
Here is some text"""

    memID, memURL = pymem.createMem(content)

    if pymem.statusCode == 200:
        print(f"MemID: {memID}")
        print(f"MemURL: {memURL}")
        pymem.appendToMem(memID, "More text in Mem!")
    else:
        print(f"Request Error ({pymem.statusCode}): {pymem.errorMsg}")
