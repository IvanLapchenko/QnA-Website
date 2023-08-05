from django.test import TestCase as DjangoTC
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Category, Question


class TestWithoutAuthorization(DjangoTC):
    def setUp(self) -> None:
        self.url = 'http://localhost:8000'

    def test_render_main_page(self):
        response_without_query = self.client.get(f'/')
        self.assertEqual(response_without_query.status_code, 200)

        response_with_query = self.client.get(f'/?id=1')
        self.assertEqual(response_with_query.status_code, 200)

    def test_categories_page(self):
        response = self.client.get(f'/categories')
        self.assertEqual(response.status_code, 200)

    def test_correct_search(self):
        response = self.client.get(f'/search?q=question')
        self.assertEqual(response.status_code, 200)

    def test_render_question_page(self):
        response_with_query = self.client.get(f'/question_page?pk=6')
        self.assertEqual(response_with_query.status_code, 404)

        response_without_query = self.client.get(f'/question_page')
        self.assertEqual(response_without_query.status_code, 404)


class AuthorizationTests(DjangoTC):
    def setUp(self):
        self.username = 'admin'
        self.password = 'admin'
        self.user = User.objects.create_user(username=self.username, password=self.password)
        self.category = Category(name='test').save()
        self.question_data = {'id': 1, 'title': 'test', 'text': 'test text', 'category': 1}
        self.question = Question(self.question_data)

    def test_login_failure(self):
        response = self.client.post(reverse('login'), {'username': self.username, 'password': 'wrong_password12345'})
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.wsgi_request.user.is_authenticated)

    def test_login_success(self):
        # Make a POST request to the login endpoint with valid credentials
        response = self.client.post(reverse('login'), {'username': self.username, 'password': self.password})

        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 302)

        # Assert that the user is now authenticated
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_create_question(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.post(reverse('create_question'), self.question_data)
        self.assertEqual(response.status_code, 302)

    def test_render_ask_question_page(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(reverse('ask_question'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('ask_question.html')

    # def test_render_user_questions(self):
    #     self.question.refresh_from_db()
    #     print(self.question)
    #     print(Question.objects.all())
    #     self.client.login(username=self.username, password=self.password)
    #     response = self.client.get('/question_page?pk=1')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed('user_questions.html')

    # def test_edit_model(self):
    #     self.client.login(username=self.username, password=self.password)
    #     Question.objects.create(title='title', author_id=self.client.pk)
    #     print(Question.objects.all())
    #     response = self.client.get('/Question/edit/1/')
    #     self.assertEqual(response.status_code, 302)
    #     self.assertTemplateUsed('edit_record.html')

    # def test_vote_upvote(self):
    #     url = reverse('vote', args=('Question', 'upvote', 1))
    #     self.client.login(username=self.username,  password=self.password)
    #     response = self.client.post(url)
    #     self.assertEqual(response.status_code, 302)
    #
    #     self.assertEqual(len(Question.objects.all()[0].upvotes), 1)
    #
    #     self.assertEqual(response.url, f'/question_page?pk={1}')



