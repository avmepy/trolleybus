from django.contrib.auth.models import User, Group
from django.test import TestCase, Client
from django.urls import reverse

from accounts.models import Profile
from transports.models import Transport, Condition


class ReportTest(TestCase):

    @classmethod
    def setUpTestData(cls):

        # create Groups

        driver_group = Group.objects.create(name='Водій')
        manager_group = Group.objects.create(name='Керівник')
        admin_group = Group.objects.create(name='Адміністратор')

        # create driver
        user = User.objects.create(username='driver', password='test_Password1')
        user.groups.add(driver_group)
        condition = Condition.objects.create(title='ok')
        transport = Transport.objects.create(reg_plate='A0 3401 BB', condition=condition, mileage=130)
        Profile.objects.create(user=user, transport=transport)

        # create manager

        user = User.objects.create(username='manager', password='test_Password2')
        user.groups.add(manager_group)

    def test_setup(self):

        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(Transport.objects.count(), 1)
        self.assertEqual(Condition.objects.count(), 1)
        self.assertEqual(Profile.objects.count(), 1)
        self.assertEqual(Group.objects.count(), 3)
        self.assertTrue(User.objects.first().groups.filter(name='Водій').exists())

    def test_report_driver_worked_hours(self):

        driver = User.objects.first()

        client = Client()
        client.force_login(driver)

        url = reverse('reports')

        data = {
            'report': 'hours',
            'from': '2020-05-05',
            'to': '2020-05-07'
        }

        response = client.post(url, data=data)
        self.assertEqual(response.headers.get('Content-Type'), 'application/vnd.ms-excel')

    def test_report_driver_worked_hours_without_date(self):

        driver = User.objects.first()

        client = Client()
        client.force_login(driver)

        url = reverse('reports')

        data = {
            'report': 'hours'
        }

        response = client.post(url, data=data)
        self.assertEqual(response.headers.get('Content-Type'), 'application/vnd.ms-excel')

    def test_report_driver_kzot(self):
        driver = User.objects.first()

        client = Client()
        client.force_login(driver)

        url = reverse('reports')

        data = {
            'report': 'kzot',
            'from': '2020-05-05',
            'to': '2020-05-07'
        }

        response = client.post(url, data=data)
        self.assertEqual(response.headers.get('Content-Type'), 'application/vnd.ms-excel')

    def test_report_driver_kzot_without_date(self):
        driver = User.objects.first()

        client = Client()
        client.force_login(driver)

        url = reverse('reports')

        data = {
            'report': 'kzot'
        }

        response = client.post(url, data=data)
        self.assertEqual(response.headers.get('Content-Type'), 'application/vnd.ms-excel')

    def test_report_manager_hours_all_drivers(self):
        manager = User.objects.get(id=2)

        client = Client()
        client.force_login(manager)

        url = reverse('reports')

        data = {
            'report': 'hours',
            'driver': 'all_drivers',
            'from': '2020-05-05',
            'to': '2020-05-07'
        }

        response = client.post(url, data=data)
        self.assertEqual(response.headers.get('Content-Type'), 'application/vnd.ms-excel')

    def test_report_manager_hours_one_driver(self):
        manager = User.objects.get(id=2)

        client = Client()
        client.force_login(manager)

        url = reverse('reports')

        data = {
            'report': 'hours',
            'driver': 1,
            'from': '2020-05-05',
            'to': '2020-05-07'
        }

        response = client.post(url, data=data)
        self.assertEqual(response.headers.get('Content-Type'), 'application/vnd.ms-excel')

    def test_report_manager_hours_all_drivers_without_date(self):
        manager = User.objects.get(id=2)

        client = Client()
        client.force_login(manager)

        url = reverse('reports')

        data = {
            'report': 'hours',
            'driver': 'all_drivers'
        }

        response = client.post(url, data=data)
        self.assertEqual(response.headers.get('Content-Type'), 'application/vnd.ms-excel')

    def test_report_manager_hours_one_driver_withput_date(self):
        manager = User.objects.get(id=2)

        client = Client()
        client.force_login(manager)

        url = reverse('reports')

        data = {
            'report': 'hours',
            'driver': 1
        }

        response = client.post(url, data=data)
        self.assertEqual(response.headers.get('Content-Type'), 'application/vnd.ms-excel')

    def test_report_manager_kzot_all_drivers(self):
        manager = User.objects.get(id=2)

        client = Client()
        client.force_login(manager)

        url = reverse('reports')

        data = {
            'driver': 'all_drivers',
            'report': 'kzot',
            'from': '2020-05-05',
            'to': '2020-05-07'
        }

        response = client.post(url, data=data)
        self.assertEqual(response.headers.get('Content-Type'), 'application/vnd.ms-excel')

    def test_report_manager_kzot_one_driver(self):
        manager = User.objects.get(id=2)

        client = Client()
        client.force_login(manager)

        url = reverse('reports')

        data = {
            'driver': 1,
            'report': 'kzot',
            'from': '2020-05-05',
            'to': '2020-05-07'
        }

        response = client.post(url, data=data)
        self.assertEqual(response.headers.get('Content-Type'), 'application/vnd.ms-excel')

    def test_report_manager_dest_all_drivers(self):
        manager = User.objects.get(id=2)

        client = Client()
        client.force_login(manager)

        url = reverse('reports')

        data = {
            'driver': 'all_drivers',
            'report': 'drivers_dest',
            'from': '2020-05-05',
            'to': '2020-05-07'
        }

        response = client.post(url, data=data)
        self.assertEqual(response.headers.get('Content-Type'), 'application/vnd.ms-excel')

    def test_report_manager_dest_one_driver(self):
        manager = User.objects.get(id=2)

        client = Client()
        client.force_login(manager)

        url = reverse('reports')

        data = {
            'driver': 1,
            'report': 'drivers_dest',
            'from': '2020-05-05',
            'to': '2020-05-07'
        }

        response = client.post(url, data=data)
        self.assertEqual(response.headers.get('Content-Type'), 'application/vnd.ms-excel')
