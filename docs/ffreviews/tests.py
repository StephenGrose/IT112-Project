from django.test import TestCase, RequestFactory
from .models import ffGame, ffReview
from django.urls import reverse
from .forms import GameForm, ReviewForm
from datetime import datetime
from django.contrib.auth.models import AnonymousUser, User



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

#These do not work, and when I came into office hours there was not an answer on how to do these.
class GetGameDetailsTest(TestCase):
    def setUp(self):
        self.game=ffGame(gameTitle='Final Fantasy Infinity')
    
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('gamedetails'))
        self.assertEqual(response.status_code,200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('gamedetails'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'ffreviews/gamedetails.html')

class GetGameReviewsTest(TestCase):
    def setUp(self):
        self.game=ffGame(gameTitle='Final Fantasy Infinity')
        self.review=ffReview(reviewTitle='Good')
    
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('gamereviews'))
        self.assertEqual(response.status_code,200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('gamereviews'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'ffreviews/gamereviews.html')
#End of test cases that fail, but I know I should test for these views.


#test forms
class NewGameForm(TestCase):
    #valid form data
    def test_gameform(self):
        data={
        'gameTitle':'final fantasy',
        'gameReleaseDate':'2021-03-27',
        'gameReleasePlatform':'console',
        'gameSummary':'characters and story'
        }
        form=GameForm(data)
        self.assertTrue(form.is_valid)

class NewReviewForm(TestCase):
    #valid form data
    def test_reviewform(self):
        gamedata={
        'gameTitle':'final fantasy',
        'gameReleaseDate':'2021-03-27',
        'gameReleasePlatform':'console',
        'gameSummary':'characters and story'
        }
        game=ffGame(gamedata)
        self.user=AnonymousUser()
        data={
            'reviewTitle' : 'I like it',
            'reviewDate' : '2021-03-27',
            'reviewBody' : 'A review of the game',
            'reviewRating' : '4',
            'game_id' : game,
            'user_id' : self.user
        }
        form=ReviewForm(data)
        self.assertTrue(form.is_valid)