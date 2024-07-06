import dotenv
import requests
import os


class MediaContainer:
    def __init__(self):
        pass


class ThreadsAPI:
    auth_threads_basic = "threads_basic"
    auth_threads_content_publish = "threads_content_publish"
    auth_threads_manage_replies = "threads_manage_replies"
    auth_threads_read_replies = "threads_read_replies"
    auth_threads_manage_insights = "threads_manage_insights"

    def __init__(
        self, base_url: str = "https://graph.threads.net", api_version: str = "v1.0"
    ):
        """_summary_

        Args:
            base_url (_type_, optional): _description_. Defaults to "https://graph.threads.net".
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
            dict: _description_
        """
        response: requests.Response = requests.get(
            f"{self.api_url}/{userid}",
            params={"fields": fields},
            headers={"Authorization": "Bearer " + token},
        )
        if response.status_code == 200:
            return response.json()
        else:
            return {"status_code": response.status_code, "reason": response.reason}

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
            ValueError: _description_

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
            raise ValueError("Invalid Authorization Code")
        else:
            return r.json()

    def get_long_token(self, access_token: str, client_secret: str) -> dict:
        """_summary_

        Args:
            short_token (str): _description_
            client_secret (str): _description_

        Raises:
            ValueError: _description_

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
            raise ValueError("Invalid Authorization Code")
        else:
            return r.json()

    def refresh_token(self, access_token: str) -> str:
        pass



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
        api_version: str = "v1",
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
            raise ValueError(
                "CLIENT_ID not provided and not found in environment variables"
            )

        if client_secret == "":
            self.client_secret = os.getenv("CLIENT_SECRET")
        else:
            self.client_secret = client_secret

        if self.client_secret == None:
            raise ValueError(
                "CLIENT_SECRET not provided and not found in environment variables"
            )

        if code != "":
            self.code = code
        else:
            raise ValueError("Authorization Code not provided")

        if token != None:
            self.token = token
            if token_length != None:
                self.token_length = token_length
            else:
                self.token_length = 0
        try:
            self.token = self.get_token(code)
        except ValueError as e:
            raise ValueError(e)
        except Exception as e:
            raise ValueError("Internal Error" + e)


if __name__ == "__main__":
    s: ThreadsAPI = ThreadsAPI()
    print(
        s.get_replies_publishing_limit(
            "me",
            "THQWJYRG01ZAFBNMGxJaFJFOXM3c1FWMkppdVJMVlBQQ2luUFNpNmdrTW1OQmJmdEN6N21qUTlSZA01oWXdXekpESVN0MkU1MFpVOVR2bW15THIyRXhmbEJMR0JVS1hxOEZAtcU5IZAG13SXp5eXVHU1BpTTlWLXhiU2s3WkEZD",
        )
    )
