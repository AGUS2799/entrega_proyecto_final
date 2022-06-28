import string
import random
from unicodedata import name
from series.models import Series
from django.test import TestCase

# Create your tests here.

KEY_LEN=20
char_list = [random.choice((string.ascii_letters+string.digits))for _ in range(KEY_LEN)]
mock_name=''.join(char_list)

class SeriesTestCase(TestCase):
    def setUp(self):
        self.serie = Series.objects.create(
            name=mock_name,
            release_date='2020-06-07',
            director_name=mock_name,
            description=mock_name,
            )
        
    
    def test_serie_creation(self):
        self.assertEqual(self.serie.name, mock_name)
        self.assertEqual(self.serie.release_date, '2020-06-07')
        self.assertEqual(self.serie.director_name, mock_name)
        self.assertEqual(self.serie.description, mock_name) 
