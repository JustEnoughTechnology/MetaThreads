import dotenv
import requests
import os

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
     
    def __init__(self, 
                 client_id:str=None , 
                 client_secret:str=None,
                 code: str =None,
                 token:str=None,
                 token_length:str=None,
                 env_file:str="env/metathreads.env",
                 secret_file:str="secrets/metathreads.secret",
                 base_url:str="https://graph.threads.net",
                 api_version:str="v1"):
        
        self.api_url = f"{base_url}/{api_version}"       
        
        dotenv.load_dotenv(env_file)
        
        dotenv.load_dotenv(secret_file)

        self.auth_url = "https://auth.threads.net"
        
        self.redirect_uri: str = os.getenv('REDIRECT_URI'),
        

        if client_id == "" : 
            self.client_id = os.getenv('CLIENT_ID')
        else : 
            self.client_id = client_id
        
        if self.client_id == None:
            raise ValueError("CLIENT_ID not provided and not found in environment variables")

        if client_secret == "" : 
            self.client_secret = os.getenv('CLIENT_SECRET')
        else :
            self.client_secret = client_secret

        if self.client_secret == None:
            raise ValueError("CLIENT_SECRET not provided and not found in environment variables")
            
        if code != "":
            self.code = code
        else:
            raise ValueError("Authorization Code not provided")
        
        if token != None:
            self.token = token
            if token_length != None:
                self.token_length = token_length
            else:
                self.token_length = 
        try:
            self.token = self.get_token(code)
        except ValueError as e:
            raise ValueError(e)
        except Exception as e:
            raise ValueError("Internal Error"+ e    )
            
    def get_token(self,code: str):
        parms  = {'client_id': self.client_id,
                  'client_secret': self.client_secret,
                  'code': code,
                  'grant':'authorization_code',
                  'redirect_uri': self.redirect_uri}
        
        r = requests.post(f'{self.__base_url}/oauth/access_token',params=parms) 
        self.token = r.json()['access_token']
        
    def get_token(self,code: str)->str:
        parms  = {'client_id': self.client_id,
                  'client_secret': self.client_secret,
                  'code': code,
                  'grant':'authorization_code',
                  'redirect_uri': self.redirect_uri}
        
        r = requests.post(f'{self.__base_url}/oauth/access_token',params=parms) 
            