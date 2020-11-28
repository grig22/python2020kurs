import requests


class D3:
    api = "https://d3.ru/api"

    # Получить список постов со всех поддоменов
    def posts(self, page=1, per_page=10, sorting="date_created"):
        res = requests.get(f"{self.api}/posts/", {"page": page, "per_page": per_page, "sorting": sorting})
        assert res.status_code == 200
        return res.json()["posts"]

    # Получить пост по ID
    def post(self, post_id):
        res = requests.get(f"{self.api}/posts/{post_id}/")
        assert res.status_code == 200
        return res.json()

    # Получить список комментариев поста
    def comments(self, post_id):
        res = requests.get(f"{self.api}/posts/{post_id}/comments/")
        assert res.status_code == 200
        return res.json()["comments"]
