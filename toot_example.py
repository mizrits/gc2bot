import sys
from mastodon import Mastodon

mastodon = Mastodon(
    client_id="app_key.txt",
    access_token="user_key.txt",
    api_base_url="https://freespeech.gaac2.com"
)

mastodon.toot('text')