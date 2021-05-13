import requests, json, time, sys
from tqdm import tqdm

VK_TOKEN = "958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008"

class VkData:


    def __init__(self, token):
        self.token = token
        self.version_vk = 5.103
        self.params = {
            "access_token": self.token,
            "v":self.version_vk
        }

    # Метод проверки id и поиск id по короткому имени
    def get_id(self, user_id):
        incorrect_id = "Введено неккоректное имя или ID."
        id_params = {
            "user_ids": user_id
        }
        try:
            response = requests.get("https://api.vk.com/method/users.get", params={**self.params, **id_params})
            return response.json()["response"][0]["id"]
        except KeyError:
            print("Неверный ID:")
            self.get_id()

    # Метод получения данных фото из ВК
    def get_photo_data(self, ID, offset=0, count=5):
        photo_params = {
            "owner_id": ID,
            "album_id": "profile",
            "offset": offset,
            "count": count,
            "photo_sizes": 0,
            "extended": 1
        }
        response = requests.get("https://api.vk.com/method/photos.get", params={**self.params, **photo_params})
        return response.json()

class YaUploader:

    def __init__(self, token, vk_user_id):
        self.token = token
        self.vk_user_id = vk_user_id
        self.HOST = "https://cloud-api.yandex.net:443"
        self.url = f"{self.HOST}/v1/disk/resources/upload"
        self.headers = {"Authorization": self.token}

    # Метод загрузки фоток на яндекс диск
    def upload_photo(self):
        success = "Все фото успешно загружены на Yandex Диск."
        error = "Произошла ошибка при загрузке!"

        vk = VkData(token=VK_TOKEN)
        photo_data = vk.get_photo_data(vk.get_id(self.vk_user_id))
        photos = []
        try:
            for files in tqdm(photo_data["response"]["items"]):
                file_url = files["sizes"][-1]["url"]
                file_name = files["likes"]["count"]
                dict = {'file_name':f"{file_name}.jpg"}
                dict["size"] = f'{files["sizes"][-1]["type"]}'
                photos.append(dict)
                params = {"path":f"netologiya/{file_name}.jpg","url":file_url}
                response = requests.post(self.url, headers=self.headers, params=params)
                time.sleep(1.5)
            # json файл с информацией
            with open("info_file.json", 'w') as outfile:
                json.dump(photos, outfile)

            if response.status_code == 202:
                return success
            else:
                return error
        except KeyError:
            return error




