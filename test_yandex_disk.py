import requests

url = "https://cloud-api.yandex.net/v1/disk/resources"
token = "y0_AgAAAABlISdqAADLWwAAAADQ81DkuL8cbKsIQSS-yBzDeiQwI9M6Ans"
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": f"OAuth {token}",
}
def test_create_folder(path):
    response1 = requests.put(f'{url}?path={path}', headers=headers)
    assert response1.status_code == 201

def test_copy_file(path_from, path_to):
    response2 = requests.post(f'{url}/copy?from={path_from}&path={path_to}', headers=headers)
    assert response2.status_code == 201

def test_rename_file(path_from, path_to):
    response3 = requests.post(f'{url}/move?from={path_from}&path={path_to}', headers=headers)
    assert response3.status_code == 201
    assert path_from != path_to

def test_log_out_user(path):
    url = "https://passport.yandex.ru/passport"
    response4 = requests.get(f'{url}?mode={path}', headers=headers)
    assert response4.status_code == 200

test_create_folder('New API Folder')
test_copy_file("/Файл для копирования.docx","/New API Folder/Файл для копирования.docx")
test_rename_file("/New API Folder/Файл для копирования.docx","/New API Folder/New_name.docx")
test_log_out_user("https://disk.yandex.ru/client/disk")