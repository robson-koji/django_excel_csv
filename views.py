from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render
import json


class NotImplementedError(Exception):
    pass


class get_excel(TemplateView):

    def add_comment(self):
        """ Adds one line of comment at the end of the file """
        return

    def get_colum_names(self):
        """ column_names = ["col 1", "col 2", "col n"] """
        raise NotImplementedError('Create get_colum_names method to provide csv headers')

    def get_data(self):
        """ Data is a list of strings (comma separated). Each string is the row
        containing the cells separated by comma.
        data = ["row_1", "row_2", "row_n"] """
        raise NotImplementedError('Create get_data method to provide csv data')

    def post(self, request, *args, **kwargs):
            data = self.get_data()
            column_names = self.get_colum_names()
            column_names = ";".join(cn for cn in column_names)

            t = loader.get_template('django_excel_csv/csv.txt')

            """
            Include the BOM (byte order mark) and its done.
            Excel will recognise the output data as UTF-8 encoding.
            """
            column_names = u'\ufeff'.encode('utf8') + column_names

            c = Context({'column_names': column_names,
                         'data': data,
                         'comment': self.add_comment()
                        })

            if self.is_ajax:
                """
                Retorna JSON para Ajax, que monta o csv no front.
                """
                csv = t.render(c)
                response_data = {}
                response_data['csv'] = csv
                response_data['message'] = "Any message to AJAX"
                return HttpResponse(json.dumps(response_data), content_type="application/json")

            else:
                """
                Retorna HTTP response text/csv. Abre direto o programa para ler o CSV,
                ou para salvar em disco
                """
                response = HttpResponse(content_type='text/csv')
                response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
                response.write(t.render(c))
                return response
