from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Post


class TestingMyAppBlog(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username='arta', password='azadi')
        cls.post1 = Post.objects.create(
            title='post 1',
            text='this is one post',
            author=cls.user,
            status=Post.STATUS[0][0],
        )
        cls.post2 = Post.objects.create(
            title='post 2',
            text='this is tow post',
            author=cls.user,
            status=Post.STATUS[1][0],
        )
    # start testing urls whit url and name
    # -----------------------------

    def test_url_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse('post_home'))
        self.assertEqual(response.status_code, 200)

    def test_url_blog(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)

    def test_url_detail(self):
        response = self.client.get(f'/blog/{self.post1.id}/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse('post_detail', args=[self.post1.id]))
        self.assertEqual(response.status_code, 200)

    def test_url_create(self):
        response = self.client.get('/blog/create/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse('post_create'))
        self.assertEqual(response.status_code, 200)

    def test_url_update(self):
        response = self.client.get(f'/blog/{self.post1.id}/update/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse('post_update', args=[self.post1.id]))
        self.assertEqual(response.status_code, 200)

    def test_url_delete(self):
        response = self.client.get(f'/blog/{self.post1.id}/delete/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse('post_delete', args=[self.post1.id]))
        self.assertEqual(response.status_code, 200)

    # ----------------------------------------
    # end testing urls whit url and name

    # * * * * * * * * * * * * * * * * * * * * *

    # start testing pages
    # ----------------------------------------

    def test_post_list(self):
        response = self.client.get('/blog/')
        self.assertContains(response, self.post1.text)
        self.assertContains(response, self.post1.title)
        self.assertNotContains(response, self.post2.title)
        self.assertNotContains(response, self.post2.text)

        response = self.client.get(reverse('post_list'))
        self.assertContains(response, self.post1.text)
        self.assertContains(response, self.post1.title)
        self.assertNotContains(response, self.post2.title)
        self.assertNotContains(response, self.post2.text)

    def test_post_detail(self):
        response = self.client.get(f'/blog/{self.post1.id}/')
        self.assertContains(response, self.post1.text)
        self.assertContains(response, self.post1.title)

        response = self.client.get(reverse('post_detail', args=[self.post1.id]))
        self.assertContains(response, self.post1.text)
        self.assertContains(response, self.post1.title)

    def test_post_create(self):
        response = self.client.post(reverse('post_create'), {
            'title': 'this is title on',
            'text': 'this is text one in title one',
            'status': 'PUB',
            'author': self.user.id,
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, 'this is title on')
        self.assertEqual(Post.objects.last().text, 'this is text one in title one')

    def test_post_update(self):
        response = self.client.post(reverse('post_update', args=[self.post2.id]), {
            'title': 'update title in post 2',
            'text': 'update text in post 2',
            'status': 'PUB',
            'author': self.user.id,
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, 'update title in post 2')
        self.assertEqual(Post.objects.last().text, 'update text in post 2')

    def test_post_delete(self):
        response = self.client.post(reverse('post_delete', args=[self.post2.id]))
        self.assertEqual(response.status_code, 302)



