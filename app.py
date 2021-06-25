import requests

def lineNotifyMessage(token, message, url):

    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    payload = {
        'message': message,
        # imageThumbnail、imageFullsize為成對的圖片，各有尺寸大小
        'imageThumbnail': url,
        'imageFullsize': url,
    }

    r = requests.post("https://notify-api.line.me/api/notify", headers=headers, params=payload)
    return r.status_code

if __name__ == "__main__":
    # 權杖
    token = 'token'
    # 要傳送的訊息
    message = 'message'
    # 要傳送圖片的網址
    url = 'url'
    lineNotifyMessage(token, message, url)
