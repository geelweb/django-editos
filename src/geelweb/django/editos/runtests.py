import os
import sys


os.environ['DJANGO_SETTINGS_MODULE'] = 'test_settings'
test_dir = os.path.dirname(__file__)
sys.path.insert(0, test_dir)

import django
from django.test.utils import get_runner
from django.conf import settings


def runtests():
    if django.VERSION[0] == 1 and django.VERSION[1] < 7:
        from django.test.utils import setup_test_environment
        setup_test_environment()

    if django.VERSION[0] == 1 and django.VERSION[1] >= 7:
        django.setup()

    TestRunner = get_runner(settings)
    test_runner = TestRunner()
    failures = test_runner.run_tests(['geelweb.django.editos'])
    sys.exit(bool(failures))
