
import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='django_excel_csv',
     version='0.5',
#     scripts=['django_excel_csv'] ,
     author="BV FAPESP",
     author_email="rmoriya@fapesp.br",
     description="Django app to create csv file. Excel semicolon separator format and utf-8 compatible.",
     long_description=long_description,
     #long_description_content_type="text/markdown",
     url="https://gitlab.com/bv_fapesp/django_excel_csv",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 2.7",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )

