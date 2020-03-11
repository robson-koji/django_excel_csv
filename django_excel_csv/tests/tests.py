# coding=utf-8
from django.test import TestCase, RequestFactory
from ..views import GetExcel


class TestAll(TestCase):
    @classmethod
    def setUpClass(cls):
        super(TestAll, cls).setUpClass()
        cls.factory = RequestFactory()
        cls.request = cls.factory.get('/')
        cls.response = GetExcel.as_view()(cls.request)

    #"""
    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_get_data(self):
        with self.assertRaisesRegexp(Exception, "Create get_data method to provide csv data"): self.response.context_data['view'].get_data()

    def test_get_column_names(self):
        with self.assertRaisesRegexp(Exception, "Create get_column_names method to provide csv headers"): self.response.context_data['view'].get_column_names()

    def test_add_comment(self):
        self.assertIsNone(self.response.context_data['view'].add_comment())
    #"""


    # Testar o post passando dados dummy para os metodos. get_data, get_column_names

    def test_post_method(self):
        get_excel_obj = self.response.context_data['view']
        def new_get_data():
            return [1,2,3]

        def new_get_column_names():
            return ['a','b','c']

        get_excel_obj.get_data = new_get_data
        get_excel_obj.get_column_names = new_get_column_names


        post = self.response.context_data['view'].post(self.request)

        import pdb; pdb.set_trace()
