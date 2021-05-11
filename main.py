import Uploaoding_photo

VK_TOKEN = ""
YA_TOKEN = ""

if __name__ == '__main__':
    u = Uploaoding_photo.YaUploader(token=YA_TOKEN)
    print(u.upload_foto())

