# from typing_extensions import Self
from django.test import TestCase
from .models import Profile,Project
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTest(TestCase):
    def setUp(self):
        self.machuka = Profile(bio = 'my awwards', id = 1, profile_pic = 'image.jpeg',date_craeted='May,16.2022')

    def test_instance(self):
        self.assertTrue(isinstance(self.machuka,Profile))

    def test_save_profile(self):
        self.machuka.save_profile()
        self.machuka = Profile.objects.all()
    
    def test_delete_profile(self):
        self.machuka.delete_profile()
        all_profiles = Profile.objects.all()
        self.assertEqual(len(all_profiles),0)

        
class ProjectsTestCase(TestCase):
    def setUp(self):
        self.new_project = Project(title = 'galleria',image = 'galleria.jpeg',description = 'a gallery app',link = 'https://link.com',date_craeted='May,16.2022')
        self.new_project.save()

    def test_save_project(self):
        self.new_project.save_project()
        pictures = Project.objects.all()
        self.assertEqual(len(pictures),1)

    def test_delete_image(self):
        self.new_project.save_project()
        self.new_project.delete_project()
        picture_list = Project.objects.all()
        self.assertTrue(len(picture_list)==0)

    def test_get_all_images(self):
       self.new_project.save_project()

    def test_get_one_image(self):
        self.new_project.save_project()