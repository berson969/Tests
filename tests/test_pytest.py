import pytest
from yandex_api import YaUploader


class TestYandexApi(YaUploader):
    @pytest.mark.parametrize(
        'path',
        [
            'New_dir',
            '222'
        ]
    )
    def test_yandex_api(self, path):
        response_status = self.create_dir(path)
        print(response_status)
        # assert response_status == 201
        assert response_status == 409


if __name__ == '__main__':
    main()