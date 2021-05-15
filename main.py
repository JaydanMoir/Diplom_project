from uploaoding_photo import YaUploader, VkData

VK_TOKEN = ""
YA_TOKEN = ""

vk_id = input("Введите ID вашей страницы ВК или короткое имя: ")

if __name__ == "__main__":
    vk = VkData(VK_TOKEN)
    photo_data = vk.get_photo_data(vk.get_id(vk_id))

    ya = YaUploader(YA_TOKEN)
    print(ya.upload_photo(photo_data))
