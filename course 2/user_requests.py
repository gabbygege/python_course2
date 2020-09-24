import requests

url = 'https://detik.com'
try:
    response = requests.get(url)
    print(f'Success! {response}')
    print(f'Content! {response.text}')
except Exception as e:
    print(f'There is an error {e}')
print('Program ended')