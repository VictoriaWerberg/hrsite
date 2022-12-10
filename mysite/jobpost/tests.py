from django.test import TestCase
from rest_framework.test import APITestCase
from jobpost.models import JobPost, Category,Company


class CategoryAPITestCase(APITestCase):
    def test_Category(self):
        url = 'api/v1/jobslist/'
        response = self.client.get(url)
        self.cate1 = Category.objects.create(title='Test category one')
        self.cate2 = Category.objects.create(title='Test category two')


class CompanyAPITestCase(TestCase):
    def test_company(self):
        self.company1 = Company.objects.create(company_name='Test company one')
        self.company2 = Company.objects.create(company_name='Test company two')

        self.company1 = Company.objects.create(
            company_name ='Test title one',
            company_profile ='Test content one',
        )

