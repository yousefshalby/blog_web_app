from django.test import TestCase
from django.urls import reverse, resolve
from blog.models import Post
from model_bakery import baker
from datetime import datetime
from django.contrib.auth.models import User

class TestViews (TestCase):
    
    def setUp(self):
        self.home_url = reverse('blog-home')
        self.create_Post_url = reverse('post-create')
        self.about_url = reverse('blog-about')
        self.user = User.objects.create(first_name = 'yousef')
        self.user.save()
        self.blog = Post.objects.create(
            title = "hamo",
            content = 'soso',
            author = self.user,
        )
        self.blog.save()


    def test_home_view_not_logged(self):
        response = self.client.get(self.home_url)

        self.assertEqual(response.status_code, 302)


    def test_home_view_has_information_fields(self):                   
        self.assertIsInstance(self.blog.title, str)
        self.assertIsInstance(self.blog.content, str)
        self.assertEqual(self.blog.author.first_name, 'yousef')

    def test_home_has_timestamps(self):                           
        self.assertIsInstance(self.blog.date_posted, datetime)

    def test_form_creation_vaidation(self):
        response = self.client.post(self.create_Post_url, {'title':'hamo', 'content':'soso'})

        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.blog.title, 'hamo')
        self.assertEqual(self.blog.content, 'soso')



    def test_form_creation_vaidation(self):
        response = self.client.post(self.create_Post_url, {'title':'hamo', 'content':'soso'})

        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.blog.title, 'hamo')
        self.assertEqual(self.blog.content, 'soso') 

    

    def test_about_view(self):
        response = self.client.get(self.about_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/about.html')

