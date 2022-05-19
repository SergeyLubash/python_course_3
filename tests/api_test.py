from run import app

class TestApi:

    def test_app_all_posts_status_code(self):
        """���������, ���������� �� ���������� ������"""
        response = app.test_client('/api/posts', follow_redirects=True)

        print(response.status_code)
        print(response.mimetype)

        assert response.status_code == 200, "������ ��� ������� ���� ������ ��������"
        assert response.mimetype == "application/json", "������� �� JSON"


    def test_app_one_post_status_code(self):
        """���������, ���������� �� ���������� ������"""
        response = app.test_client('/api/posts', follow_redirects=True)

        print(response.status_code)
        print(response.mimetype)

        assert response.status_code == 200, "������ ��� ������� ���� ������ ��������"
        assert response.mimetype == "application/json", "������� �� JSON"