from django.test import TestCase
from blog.models import Post
from model_bakery import baker
from django.urls import reverse, resolve

class ModelTests(TestCase):
    def setUp(self):
        self.blog = baker.make('blog.Post', title = 'yousef').pk


    def test_post_model(self):
        data = baker.make('blog.Post', title='nono')
        self.assertTrue(isinstance(data, Post))
        self.assertEqual(data.title, 'nono')


    def test_url(self):
        res = Post.objects.get(id= self.blog)
        response = self.client.post(reverse('post-detail', args=[res.pk,]))
        self.assertEqual(response.status_code, 405)