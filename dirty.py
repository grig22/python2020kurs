import requests
import logging


class D3:

    def __init__(self):
        self.api = "https://d3.ru/api"
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.info("OBJECT CREATED")

    # Получить список постов со всех поддоменов
    def posts(self, page=1, per_page=10, sorting="date_created"):
        url = f"{self.api}/posts/"
        self.logger.info(f"url '{url}', page '{page}', per_page '{per_page}', sorting '{sorting}'")
        res = requests.get(url, {"page": page, "per_page": per_page, "sorting": sorting})
        self.logger.info(f"STATUS '{res.status_code}'")
        assert res.status_code == 200
        return res.json()["posts"]

    # Получить пост по ID
    def post(self, post_id):
        url = f"{self.api}/posts/{post_id}/"
        self.logger.info(f"url '{url}'")
        res = requests.get(url)
        self.logger.info(f"STATUS '{res.status_code}'")
        assert res.status_code == 200
        return res.json()

    # Получить список комментариев поста
    def comments(self, post_id):
        url = f"{self.api}/posts/{post_id}/comments/"
        self.logger.info(f"url '{url}'")
        res = requests.get(url)
        self.logger.info(f"STATUS '{res.status_code}'")
        assert res.status_code == 200
        return res.json()["comments"]

    # Получить список постов пользователя
    def user_posts(self, login):
        url = f"{self.api}/users/{login}/posts/"
        res = requests.get(url)
        self.logger.info(f"STATUS '{res.status_code}'")
        assert res.status_code == 200
        return res.json()

    # Получить список доменов пользователя
    def user_domains(self, login):
        url = f"{self.api}/users/{login}/domains/"
        self.logger.info(f"url '{url}'")
        res = requests.get(url)
        self.logger.info(f"STATUS '{res.status_code}'")
        assert res.status_code == 200
        return res.json()
