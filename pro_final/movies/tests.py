import string
import random
from movies.models import Movies
from django.test import TestCase

# Create your tests here.

KEY_LEN=20
char_list = [random.choice((string.ascii_letters+string.digits))for _ in range(KEY_LEN)]
mock_name=''.join(char_list)

class MoviesTestCase(TestCase):
    def setUp(self):
        self.movies = Movies.objects.create(
            name=mock_name,
            release_date='2020-06-07',
            director_name=mock_name,
            description=mock_name,
            )
        
    
    def test_movie_creation(self):
        self.assertEqual(self.movies.name, mock_name)
        self.assertEqual(self.movies.release_date, '2020-06-07')
        self.assertEqual(self.movies.director_name, mock_name)
        self.assertEqual(self.movies.description, mock_name) 
