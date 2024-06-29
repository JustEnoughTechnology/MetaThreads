import dotenv
env_file = "metathreads.env"
threads_scope: dict = dict(
        threads_basic=True,
        threads_content_publish=True,
        threads_manage_replies=True,
        threads_read_replies=True,
        threads_manage_insights=True
    )

class MediaContainer:
    def __init__(self):
        pass



def refresh_token(token: str)->str:
    pass

def swap_token(token: str)->str:
    pass

def get_profile() -> dict:
    pass

def get_threads_publishing_limit() -> dict:
    pass
    
def create_thread()->MediaContainer:
    pass

def threads_publish():
    pass

class Replies:
    def __init__(self):
        pass

class Conversation:
    def __init__(self):
        pass

class ThreadsSesson:
    """_summary_
    This class encapsulates one session
    Variables:
    __redirect_uri: str 
        Not used in this version, simply for documentation
    __base_url: str
        Should be always set to "https://graph.threads.com"
    __api_version: str
        To complete the api path. May not be necessary
    __api_url: str
        Base+version
    __auth_url: str
        Where we have to get our code, this is not used by this library but it is here for documentation
    __token : str
        The token that we will use to authenticate our requests. It can be a long lived or short lived token. The API doesn't really care


    """
    
    __scope: 
 
    __redirect_uri = "https://localhost"
    __base_url = "https://graph.threads.com"
    __api_version = "v1"
    __api_url = f"{__base_url}/{__api_version}"
    __auth_url = "https://auth.threads.com"
    __token = ""

    def __init__(self, client_id:str, 
                 client_secret:str,
                 grant_type:str="authorization_code", 
                 code: str = ""):
        try:
            __token = get_token(code)
        except Exception as e:
            print(e)
            __token = ""
    def get_token(self,code: str)->str:
        pass