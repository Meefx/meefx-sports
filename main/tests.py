from django.test import TestCase, Client
from .models import Item
from django.template import Context, Template
from django.utils.html import escape

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')
    
    # Melakukan setup model Item
    def setUp(self):
        self.item = Item.objects.create(
            name='Sepatu Badminton',
            amount=100,
            description='Bawahnya ada karetnya.'
        )

    # Melakukan test nama item
    def test_item_name(self):
        self.assertEqual(self.item.name, 'Sepatu Badminton')
    
    # Melakukan test jumlah item
    def test_item_amount(self):
        self.assertEqual(self.item.amount, 100)

    # Melakukan test deskripsi item
    def test_item_description(self):
        self.assertEqual(self.item.description, 'Bawahnya ada karetnya.')
    
    # Melakukan test apakah html bisa membaca data
    def test_html_is_equal(self):
        context_data = {
            'name': 'Muhammad Fakhri Robbani',
            'NPM': '2206026252',
            'class': 'PBP C',
        }

        expected_html = f"""
        <h1>Meefx Sports</h1>

        <h5>Name: {escape(context_data['name'])}</h5>
        <h5>NPM: {escape(context_data['NPM'])}</h5>
        <h5>Class: {escape(context_data['class'])}</h5>
        """

        template = Template(open('main/templates/main.html').read())
        rendered_html = template.render(Context(context_data))

        # Assert that the rendered HTML matches the expected HTML
        self.assertHTMLEqual(rendered_html, expected_html)