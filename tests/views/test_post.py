import pytest
import os
import json

from django.urls import reverse

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_blog.settings")

@pytest.mark.django_db
def test_post_view(client):
    url = reverse('home')
    response = client.get(url)
    assert response.status_code == 200

    import pdb; pdb.set_trace()
    
    response = json.loads(response.content)
    assert response.content == 'home'
