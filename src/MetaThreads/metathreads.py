import dotenv
import requests
import os


class MediaContainer:
    def __init__(self):
        pass


class Metrics:
    """_summary_"""

    follower_demographics = "follower_demographics"
    followers_count = "followers_count"
    quotes = "quotes"
    reposts = "reposts"
    replies = "replies"
    likes = "likes"
    views = "views"
    age = "age"
    city = "city"
    country = "country"
    gender = "gender"


class Permissions:
    """_summary_"""

    threads_basic = "threads_basic"
    threads_content_publish = "threads_content_publish"
    threads_manage_replies = "threads_manage_replies"
    threads_read_replies = "threads_read_replies"
    threads_manage_insights = "threads_manage_insights"


class ThreadsAPI:

    def __init__(
        self, base_url: str = "https://graph.threads.net", api_version: str = "v1.0"
    ):
        """_summary_
        mainly makes sure that the api url is correct. Makes it possible to create more than one API instance in one module

        Args:
            base_url (str, optional): _description_. Defaults to "https://graph.threads.net".
            api_version (str, optional): _description_. Defaults to "v1.0".
        """
        self.api_url = f"{base_url}/{api_version}"

    def get_profile(
        self,
        userid: str = "me",
        fields: str = "id,username,threads_profile_picture_url,threads_biography",
        token: str = None,
    ) -> dict:
        """_summary_

                Args:
                    userid (str, optional): _description_. Defaults to "me".
                    fields (str, optional): _description_. Defaults to "id,username,threads_profile_picture_url,threads_biography".
                    token (str, optional): _description_. Defaults to None.

                Returns:
                    dict: {
                        "id": "1234567",
                        "username": "threadsapitestuser",
                        "threads_profile_picture_url": "https://scontent-sjc3-1.cdninstagram.com/link/to/profile/picture/on/threads/",
                        "threads_biography": "This is my Threads bio."
        }
        """
        response: requests.Response = requests.get(
            f"{self.api_url}/{userid}",
            params={"fields": fields},
            headers={"Authorization": "Bearer " + token},
        )
        if response.status_code == 200:
            return response.json()
        else:
            raise RuntimeError(
                {"status_code": response.status_code, "reason": response.reason}
            )

    def get_threads_publishing_limit(
        self, userid: str = "me", token: str = None
    ) -> dict:
        """_summary_

        Args:
            userid (str, optional): _description_. Defaults to "me".
            token (str, optional): _description_. Defaults to None.

        Returns:
            dict: _description_
        """
        response: requests.Response = requests.get(
            f"{self.api_url}/{userid}/threads_publishing_limit",
            params={"fields": "quota_usage,config"},
            headers={"Authorization": "Bearer " + token},
        )
        if response.status_code == 200:
            return response.json()
        else:
            return {"status_code": response.status_code, "reason": response.reason}

    def get_replies_publishing_limit(
        self, userid: str = "me", token: str = None
    ) -> dict:
        """_summary_

        Args:
            userid (str, optional): _description_. Defaults to "me".
            token (str, optional): _description_. Defaults to None.

        Returns:
            dict: _description_
        """
        response: requests.Response = requests.get(
            f"{self.api_url}/{userid}/threads_publishing_limit",
            params={"fields": "reply_quota_usage,reply_config"},
            headers={"Authorization": "Bearer " + token},
        )
        if response.status_code == 200:
            return response.json()
        else:
            return {"status_code": response.status_code, "reason": response.reason}

    def create_thread(self) -> MediaContainer:
        pass

    def threads_publish(self):
        pass

    def get_token(
        self, client_id: str, client_secret: str, code: str, redirect_uri: str
    ) -> dict:
        """_summary_

        Args:
            client_id (str): _description_
            client_secret (str): _description_
            code (str): _description_
            redirect_uri (str): _description_

        Raises:
            RuntimeError: _description_

        Returns:
            dict: _description_
        """
        parms = {
            "client_id": client_id,
            "client_secret": client_secret,
            "code": code,
            "grant": "authorization_code",
            "redirect_uri": redirect_uri,
        }

        r = requests.post(f"{self.api_url}/oauth/access_token", params=parms)
        if r.status_code != 200:
            raise RuntimeError("Invalid Authorization Code")
        else:
            return r.json()

    def get_long_token(self, access_token: str, client_secret: str) -> dict:
        """_summary_

        Args:
            short_token (str): _description_
            client_secret (str): _description_

        Raises:
            RuntimeError: _description_

        Returns:
            dict: _description_
        """
        parms = {
            "client_secret": client_secret,
            "grant_type": "th_exchange_token",
            "access_token": access_token,
        }

        r = requests.post(f"{self.api_url}/oauth/access_token", params=parms)
        if r.status_code != 200:
            raise RuntimeError("Invalid Authorization Code")
        else:
            return r.json()

    def refresh_token(self, long_lived_access_token: str) -> dict:
        """_summary_

        Args:
            long_lived_access_token (str): _description_

        Raises:
            RuntimeError: _description_

        Returns:
            dict: {
                "access_token": "<LONG_LIVED_USER_ACCESS_TOKEN>",
                "token_type": "bearer",
                "expires_in": 5183944 // number of seconds until token expires
                }
        """
        parms = {
            "grant_type": "th_refresh_token",
            "access_token": long_lived_access_token,
        }

        r = requests.post(f"{self.api_url}/refresh_access_token", params=parms)
        if r.status_code != 200:
            raise RuntimeError("Failed to Refresh Token")
        else:
            return r.json()

    def get_user_insights(
        self,
        userid: str = "me",
        since: str = None,
        until: str = None,
        metric: str = "follower_demographics,followers_count,quotes,reposts,replies,likes,views",
        breakdown: str = None,
        access_token: str = None,
    ) -> dict:
        """_summary_

        Args:
            userid (str, optional): _description_. Defaults to "me".
            since (str, optional): _description_. Defaults to None.
            until (str, optional): _description_. Defaults to None.
            metric (str, optional): _description_. Defaults to "follower_demographics,followers_count,quotes,reposts,replies,likes,views".
            breakdown (str, optional): _description_. Defaults to None. Value must be one of "country", "city", "age", "gender"
            access_token (str, optional): _description_. Defaults to None.

        Raises:
            RuntimeError: _description_

        Returns:
            dict: _description_
        """

        parms = {"metric": metric}
        if since != None:
            parms["since"] = since

        if until != None:
            parms["until"] = until

        if metric.find("follower_demographics") != -1:
            if breakdown != None:
                parms["breakdown"] = breakdown
            else:
                raise RuntimeError(
                    "Breakdown must be provided for follower_demographics"
                )

        response: requests.Response = requests.get(
            f"{self.api_url}/{userid}/threads_insights",
            params=parms,
            headers={"Authorization": "Bearer " + access_token},
        )
        if response.status_code == 200:
            return response.json()
        else:
            raise RuntimeError(
                {"status_code": response.status_code, "reason": response.reason}
            )

    def get_post_insights(
        self,
        media_id: str = None,
        metric: str = "views,likes,replies,reposts,quotes",
        access_token: str = None,
    ) -> dict:
        """_summary_

        Args:
            media_id (str, optional): _description_. Defaults to None.
            metric (str, optional): _description_. Defaults to "views,likes,replies,reposts,quotes".
            access_token (str, optional): _description_. Defaults to None.

        Returns:
            dict: _description_
        """
        if media_id == None:
            raise RuntimeError("media_id must be provided")

        parms = {"metric": metric}

        response: requests.Response = requests.get(
            f"{self.api_url}/{media_id}/insights",
            params=parms,
            headers={"Authorization": "Bearer " + access_token},
        )
        if response.status_code == 200:
            return response.json()
        else:
            raise RuntimeError(
                {"status_code": response.status_code, "reason": response.reason}
            )

    def get_user_threads(
        self,
        threads_user_id: str = "me",
        fields: str = "*",
        since:str=None,
        until:str=None,
        limit:int=25,
        before:str=None,
        after:str=None,
        access_token: str = None,
    ):
        
        parms:dict ={   }
        
        if fields == "*":
            parms["fields"] =  "id,media_product_type,media_type,media_url,permalink,owner,username,text,timestamp,shortcode,thumbnail_url,children,is_quote_post,has_replies,reply_audience"   
        else:
            parms["fields"] = fields
            
        if since != None:
            parms["since"] = since
        if until != None:
            parms["until"] = until
        if limit != None:
            parms["limit"] = limit  
        if before != None:
            parms["before"] = before
        if after != None:
            parms["after"] = after

        if access_token == None:
            raise RuntimeError("Access Token is required")

        response: requests.Response = requests.get(
            f"{self.api_url}/{threads_user_id}/threads",
            params=parms,
            headers={"Authorization": "Bearer " + access_token}
        )
        
        if response.status_code == 200:
            return response.json()
        else:
            raise RuntimeError(
                {"status_code": response.status_code, "reason": response.reason}
            )

    def get_thread(self,threads_media_id:str = None,access_token:str = None,fields:str = "*"):
        
        parms:dict = {}
        
        if threads_media_id == None:
            raise RuntimeError("media_id must be provided")
        
        if access_token == None:
            raise RuntimeError("Access Token is required")

        if fields == "*":
            parms["fields"] = "id,media_product_type,media_type,media_url,permalink,owner,username,text,timestamp,shortcode,thumbnail_url,children,is_quote_post,has_replies,is_reply_owned_by_me,root_post,replied_to,hide_status,reply_audience"
        else:
            parms["fields"] = fields
            
        response: requests.Response = requests.get(
            f"{self.api_url}/{threads_media_id}",
            params=parms,
            headers={"Authorization": "Bearer " + access_token},
        )
        if response.status_code == 200:
            return response.json()
        else:
            raise RuntimeError(
                {"status_code": response.status_code, "reason": response.reason}
            )
    
class Conversation:
    def __init__(self):
        pass


class ThreadsSesson:

    def __init__(
        self,
        client_id: str = None,
        client_secret: str = None,
        code: str = None,
        token: str = None,
        token_length: str = None,
        env_file: str = "env/metathreads.env",
        secret_file: str = "secrets/metathreads.secret",
        base_url: str = "https://graph.threads.net",
        api_version: str = "v1.0",
    ):

        self.api_url = f"{base_url}/{api_version}"

        dotenv.load_dotenv(env_file)

        dotenv.load_dotenv(secret_file)

        self.auth_url = "https://auth.threads.net"

        self.redirect_uri: str = (os.getenv("REDIRECT_URI"),)

        if client_id == "":
            self.client_id = os.getenv("CLIENT_ID")
        else:
            self.client_id = client_id

        if self.client_id == None:
            raise RuntimeError(
                "CLIENT_ID not provided and not found in environment variables"
            )

        if client_secret == "":
            self.client_secret = os.getenv("CLIENT_SECRET")
        else:
            self.client_secret = client_secret

        if self.client_secret == None:
            raise RuntimeError(
                "CLIENT_SECRET not provided and not found in environment variables"
            )

        if code != "":
            self.code = code
        else:
            raise RuntimeError("Authorization Code not provided")

        if token != None:
            self.token = token
            if token_length != None:
                self.token_length = token_length
            else:
                self.token_length = 0
        try:
            self.token = self.get_token(code)
        except RuntimeError as e:
            raise RuntimeError(e)
        except Exception as e:
            raise RuntimeError("Internal Error" + e)


if __name__ == "__main__":
    s: ThreadsAPI = ThreadsAPI()
    
    t = s.get_threads(limit=100, since="2024-07-11",fields="id,timestamp,media_type,is_quote_post,has_replies,children",
            access_token="THQWJYRG01ZAFBNMGxJaFJFOXM3c1FWMkppdVJMVlBQQ2luUFNpNmdrTW1OQmJmdEN6N21qUTlSZA01oWXdXekpESVN0MkU1MFpVOVR2bW15THIyRXhmbEJMR0JVS1hxOEZAtcU5IZAG13SXp5eXVHU1BpTTlWLXhiU2s3WkEZD",
        )
    print(t)
