# pages/tests.py
from django.http import request, response
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import HomePageView


class HomepageTests(SimpleTestCase):
    def test_homepage_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_homepage_url_name(self):
        response = self.client.get(reverse('home'))
        self.assertAlmostEqual(response.status_code, 200)

    def test_homepage_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
    
    def test_homepage_contains_correct_data(self):
        response = self.client.get('/')
        self.assertContains(response, 'HomePage')
    
    def test_homepage_doesnot_contains_correct_html(self):
        response = self.client.get('/')
        self.assertNotContains(response, "This text is not present in site")

    def test_homepage_url_resolve_homepageview(self):
        view = resolve('/')
        self.assertEqual(
            view.func.__name__,
            HomePageView.as_view().__name__
        )