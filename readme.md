# Stream Twitch Chat Text Data with Python WebSockets

Install the Python environment required for this repo with:

```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

Activate this Python environment:

```bash
source env/bin/activate
```

### Configure Credentials 

For Twitch, get your Oauth token at https://twitchapps.com/tmi/ and edit the below text (within `auth_credentials.py`).

```python
twitch_server = 'irc.chat.twitch.tv'
port = 6667
twitch_auth_username = "<your_username>"
twitch_oauth = '<oauth_auth_token>'  # From https://twitchapps.com/tmi/
twitch_live_channel_name  = '#<poll_livestream_channel_name>'
```
*Note: It's recommended to use environemental variables to store senesitive data such as tokens/credentials.*

Run Twitch Live Chat Webhook

```bash
python3 twitch_live_chat_webhook.py
```
