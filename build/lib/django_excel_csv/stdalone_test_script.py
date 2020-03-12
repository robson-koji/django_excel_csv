#!/usr/bin/env python

import sys
import os
SETTINGS_PATH = os.path.dirname(os.path.dirname(__file__))


try:
    import django
    from django.conf import settings

    settings.configure(
        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.mysql",
            }
        },
        INSTALLED_APPS=[
        ],
        NOSE_ARGS=['-s'],

        TEMPLATE_DIRS = (
            os.path.join(SETTINGS_PATH, 'templates'),
        )
    )

    # import pdb; pdb.set_trace()
    django.setup()

    from django_nose import NoseTestSuiteRunner
except ImportError:
    raise ImportError("To fix this error, run: pip install -r requirements.txt")


def run_tests(*test_args):
    if not test_args:
        test_args = ['tests']

    test_runner = NoseTestSuiteRunner(verbosity=1)
    failures = test_runner.run_tests(test_args)
    if failures:
        sys.exit(failures)


if __name__ == '__main__':
    run_tests(*sys.argv[1:])
