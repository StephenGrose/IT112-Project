from django.test import TestCase
from .models import ffGame, ffReview
from django.urls import reverse
# Create your tests here.

class GameTest(TestCase):
    def setUp(self):
        self.game=ffGame(gameTitle='Final Fantasy Infinity')

    def test_string(self):
        self.assertEqual(str(self.game), 'Final Fantasy Infinity')
    
    def test_tablename(self):
        self.assertEqual(str(ffGame._meta.db_table), 'games')

class ReviewTest(TestCase):
    def setUp(self):
        self.review=ffReview(reviewTitle='I liked it')
    
    def test_string(self):
        self.assertEqual(str(self.review), 'I liked it')

    def test_tablename(self):
        self.assertEqual(str(ffReview._meta.db_table),'reviews')

#views
class IndexTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code,200)
    
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'ffreviews/index.html')
 
class GetGameTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('games'))
        self.assertEqual(response.status_code,200)
 
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('games'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'ffreviews/games.html')