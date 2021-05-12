import uploaoding_photo

VK_TOKEN = ""
YA_TOKEN = ""

success = "Все фото успешно загружены на Yandex Диск."
error = "Произошла ошибка при загрузке!"
incorrect_id = "Введено неккоректное имя или ID."


if __name__ == "__main__":

    ya = uploaoding_photo.YaUploader(token=YA_TOKEN)
    print(ya.upload_photo())
