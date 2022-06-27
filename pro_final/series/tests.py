import string
from unicodedata import name
import random
from models import Series

# Create your tests here.
def series_test():
    KEY_LEN=20
    char_list = [random.choice((string.ascii_letters+string.digits))for _ in range(KEY_LEN)]
    mock_name=''.join(char_list)

    movies = Series(
        name=mock_name,
        release_date='2020-09-11',
        director_name=mock_name,
        description=mock_name,
        )
    movies.save()

series_test()