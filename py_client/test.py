import requests

url = 'http://127.0.0.1:8000/melanoma/upload/'
file_path = r'C:\Notebooks\skin cancer classifier\skin cancer\working\test\malignant\melanoma_10280.jpg'

with open(file_path, 'rb') as file:
    files = {'file': file}
    response = requests.post(url, files=files)

print(response.status_code)
print(response.text)
