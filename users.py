from PIL import Image, ImageDraw, ImageFont
from mastodon import Mastodon
import datetime
import sys

##init and get data
mastodon = Mastodon(
    client_id="app_key.txt",
    access_token="user_key.txt",
    api_base_url="https://freespeech.gaac2.com"
)
instance = mastodon.instance()
users = instance['stats']['user_count']

##image
im = Image.new("RGB", (600, 310), (256, 256, 256))
draw = ImageDraw.Draw(im)
font1 = ImageFont.truetype('C:/Windows/Fonts/meiryob.ttc', 70)
font2 = ImageFont.truetype('C:/Windows/Fonts/meiryob.ttc', 140)
font3 = ImageFont.truetype('C:/Windows/Fonts/meiryob.ttc', 30)
text1 = "現在のユーザー数"
text2 = users
text3 = str(datetime.datetime.now().strftime("%Y/%m/%d %H:%M"))+"取得 by@bot"
#position
draw.text((20, 0), text1, fill=(0, 0, 0), font=font1)
draw.text((20, 80), str(text2), fill=(26, 39, 146), font=font2)
draw.text((20, 270), text3, fill=(0, 0, 0), font=font3)
#export
im.save("./image.png")

##toot
img1 = mastodon.media_post("image.png")
img_files = [img1]
mastodon.status_post(
    status = '#ユーザー数',
    media_ids = img_files
    )


