from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Paste, PasteFile
import json

class PasteTestCase(APITestCase):
    def setUp(self):
        pass

    def test_post_get(self):
        post_data = '''
{
  "id": "TESTING2",
  "title": "TestPaste",
  "files": [
    {
      "id": "47a43dc9-4279-49e5-994f-c7e4762cf9ab",
      "name": "File2",
      "contents": "Data 2",
      "language": "plain_text"
    },
    {
      "id": "d520d90f-f3f9-44d6-b7fd-e89d969e451a",
      "name": "File1",
      "contents": "Data 1",
      "language": "plain_text"
    }
  ]
}
'''
		# create a Paste and PasteFile(s) with the above JSON data
        response = self.client.post('/api/v1/paste/create', post_data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # retrieve the Paste we just created
        paste_id = response.data['id']
        response = self.client.get('/api/v1/paste/view/' + paste_id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = json.loads(post_data)
        # ids are not preserved on POST by design, so don't compare them
        del data['id']
        del data['files'][0]['id']
        del data['files'][1]['id']

        del response.data['id']
        del response.data['files'][0]['id']
        del response.data['files'][1]['id']

        data_json = json.dumps(data)
        # lazy way of avoiding OrderedDict
        response_data_json = json.dumps(json.loads(json.dumps(response.data)))
        self.assertEqual(data_json, response_data_json)
