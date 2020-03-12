# coding=utf-8
from django.test import TestCase, RequestFactory
from ..views import GetExcel


class TestGeneric(TestCase):
    """ Test all except post method """
    @classmethod
    def setUpClass(cls):
        super(TestGeneric, cls).setUpClass()
        cls.factory = RequestFactory()
        cls.request = cls.factory.get('/')
        cls.response = GetExcel.as_view()(cls.request)

    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_get_data(self):
        with self.assertRaisesRegexp(Exception, "Create get_data method to provide csv data"): self.response.context_data['view'].get_data()

    def test_get_column_names(self):
        with self.assertRaisesRegexp(Exception, "Create get_column_names method to provide csv headers"): self.response.context_data['view'].get_column_names()

    def test_add_comment(self):
        self.assertIsNone(self.response.context_data['view'].add_comment())


class TestPostMethod(TestCase):
    """ Test post method of the TemplateView Class """

    @classmethod
    def setUpClass(cls):
        """ Main targe here is to call the post method """
        super(TestPostMethod, cls).setUpClass()
        cls.factory = RequestFactory()
        cls.request = cls.factory.get('/')
        cls.response = GetExcel.as_view()(cls.request)

        # Get the view
        get_excel_obj = cls.response.context_data['view']

        # Create methods with dummy data to patch the view
        def dummy_get_data():
            return ["1,2,3", "4,5,6", "7,8,9"]

        def dummy_get_column_names():
            return ['a','b','c']

        # Patch class instance with dummy methods
        get_excel_obj.get_data = dummy_get_data
        get_excel_obj.get_column_names = dummy_get_column_names

        # Call post method
        cls.post_response = get_excel_obj.post(cls.request)

    def test_post_response_200(self):
        self.assertEqual(self.post_response.status_code, 200)

    def test_post_response_content(self):
        # import pdb; pdb.set_trace()
        self.assertIn(b'1,2,3', self.post_response.content )
