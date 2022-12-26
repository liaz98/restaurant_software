import pytest as pytest


@pytest.mark.usefixtures('init_db')
@pytest.mark.db(transaction=True)
class TestMemberProfileMe:
    endpoint = '/api/food/'
    fixtures = ['tests/fixtures/tables.json']

    def get_path(self, id_=None):
        if id_:
            return f"{self.endpoint}{id_}/"
        return self.endpoint

    @pytest.mark.main
    def test_food_list(self):
        path = self.get_path()

        response = client.get(path)

        assert response.status_code == 200
        assert response.data['data']['id'] == 1

    def test_update_me(self, client):
        user = User.objects.get(pk=3)
        client = authorize_client(client, user)

        path = self.get_path() + "me/"

        data = {
            'user': {
                'first_name': 'John',
                'last_name': 'Smith II',
                'services': [1],
            },
            'bio': 'blah blah',
            'birth_date': '1998-01-04',
        }
        response = client.put(path, data=data, format='json')
        assert response.status_code == 200
        assert response.data
        assert response.data['data']['user']['last_name'] == 'Smith II'

    def test_delete_me(self, client):
        client = authorize_client(client, User.objects.get(pk=3))
        path = self.get_path() + "me/"
        response = client.delete(path)

        assert response.status_code == 200
        assert not UserProfile.objects.filter(pk=1).exists()
        assert not User.objects.filter(pk=3).exists()