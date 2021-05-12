import requests, json, time
from tqdm import tqdm
from main import VK_TOKEN

class VkData:

    def __init__(self, token):
        self.token = token
        self.version = 5.103
        self.vk_user_id = input("Введите ID вашей страницы ВК или короткое имя: ")
        self.params = {
            "access_token":self.token,
            "v":self.version
        }

    #Метод проверки id и поиск id по короткому имени
    def get_id(self, user_id):
        id_params = {
            "user_ids": user_id
        }
        try:
            response = requests.get("https://api.vk.com/method/users.get", params={**self.params, **id_params})
            return response.json()["response"][0]["id"]
        except KeyError:
            return "Введено неккоректное имя или ID."

    #Метод получения данных фото из ВК
    def get_foto_data(self, ID, offset=0, count=5):
        foto_params = {
            "owner_id": ID,
            "album_id": "profile",
            "offset": offset,
            "count": count,
            "photo_sizes": 0,
            "extended": 1
        }
        response = requests.get("https://api.vk.com/method/photos.get", params={**self.params, **foto_params})
        return response.json()

class YaUploader:

    def __init__(self, token):
        self.token = token
        self.HOST = "https://cloud-api.yandex.net:443"
        self.url = f"{self.HOST}/v1/disk/resources/upload"
        self.headers = {"Authorization": self.token}
    #Метод загрузки фоток на яндекс диск
    def upload_foto(self):

        vk = VkData(token=VK_TOKEN)
        foto_data = vk.get_foto_data(vk.get_id(vk.vk_user_id))
        fotos = []
        try:
            for i, files in enumerate(tqdm(foto_data["response"]["items"])):
                file_url = files["sizes"][-1]["url"]
                file_name = files["likes"]["count"]
                dict = {'file_name':f"{file_name}.jpg"}
                dict["size"] = f'{files["sizes"][-1]["type"]}'
                fotos.append(dict)
                params = {"path":f"netologiya/{file_name}.jpg","url":file_url}
                response = requests.post(self.url, headers=self.headers, params=params)
                time.sleep(1.5)
            #json фоток
            with open('data1.txt', 'w') as outfile:
                json.dump(fotos, outfile)

            if response.status_code == 202:
                return "Все фото успешно загружены на Yandex Диск."
            else:
                return "Произошла ошибка при загрузке!"
        except KeyError:
            return "Произошла ошибка при загрузке!"



