from uploaoding_photo import YaUploader

YA_TOKEN = "AQAAAAAIcNm8AADLWzAowJfzLEhGmmskVJAJWsI"

vk_id = input("Введите ID вашей страницы ВК или короткое имя: ")

if __name__ == "__main__":

    ya = YaUploader(YA_TOKEN, vk_id)
    print(ya.upload_photo())
