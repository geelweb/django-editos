from django.test import TestCase
from django.template import Template, Context
from django.core.files import File
from geelweb.django.editos.models import Edito
import datetime

class EditoTagTest(TestCase):
    TEMPLATE = Template("{% load editos %}{% editos %}")

    def test_no_editos(self):
        rendered = self.TEMPLATE.render(Context({}))
        self.assertEqual(u'\n', rendered)

    def test_no_active_editos(self):
        Edito.objects.create(
                display_from=datetime.date.today(),
                display_until=datetime.date.today() + datetime.timedelta(days=1),
                image=File(open('image.svg')),
                active=False)
        Edito.objects.create(
                display_from=datetime.date.today() + datetime.timedelta(days=1),
                display_until=datetime.date.today() + datetime.timedelta(days=2),
                image=File(open('image.svg')))
        Edito.objects.create(
                display_from=datetime.date.today() - datetime.timedelta(days=2),
                display_until=datetime.date.today() - datetime.timedelta(days=1),
                image=File(open('image.svg')))
        rendered = self.TEMPLATE.render(Context({}))
        self.assertIn(u'\n', rendered)

    def test_many_editos(self):
        for n in range(3):
            Edito.objects.create(
                    display_from=datetime.date.today(),
                    display_until=datetime.date.today() + datetime.timedelta(days=1),
                    image=File(open('image.svg')))
        rendered = self.TEMPLATE.render(Context({}))
        self.assertIn('carousel-editos', rendered)

