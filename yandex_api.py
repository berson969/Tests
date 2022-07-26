from pprint import pprint
import requests
from dotenv import load_dotenv
import os
import json


class YaUploader:

    def __init__(self, token: str):
        self.token = token
        self.headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'}
        self.url = 'https://cloud-api.yandex.net/v1/disk/resources'

    def create_dir(self, path: str):
        params = {'path': path}
        response = requests.put(self.url, params=params, headers=self.headers)
        if response.status_code == 201:
            print('Directory is opened')
        elif response.status_code == 409:
            print('Directory already exists')
        return response.status_code


if __name__ == '__main__':
    load_dotenv('.env')
    new_dir = YaUploader(os.getenv('TOKEN'))
    new_dir.create_dir('New_dir')
