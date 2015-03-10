from dimager.models import Photo, Album
from django.contrib.auth.models import User
from django.test import TestCase
import factory


class PhotoFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Photo


class AlbumFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Album


class TestPhoto(TestCase):
    def setUp(self):
        self.onephoto = PhotoFactory.create(title='image1')
        self.twophoto = PhotoFactory.create(title='image2')

    def test_title(self):
        '''Assert that picture contains a title'''
        self.assertEqual(self.onephoto.title, 'image1')

    def test_description(self):
        '''Assert picture contains description'''
        self.assertEqual(self.bobphoto.description, 'No Description')

    # def test_date_uploaded(self):
    #     '''Assert photo has upload date or null'''
    #     assert Photo.date_uploaded == now()

    # def test_date_modified(self):
    #     '''Assert Photo has modified date or null'''
    #     assert Photo.date_modified == now()

    # def test_date_published(self):
    #     '''Assert Photo has published date or null'''
    #     assert Photo.date_published == today()

    def test_private(self):
        '''Assert default privacy option is private; no one can view'''
        self.assertEqual(self.bobphoto.published, 'private')

    def test_shared(self):
        '''Assert option for shared; friends can view'''

    def test_public(self):
        '''Assert option for public; anyone can view that follows'''


class TestAlbum(TestCase):
    def setup(self):
        self.elenor = UserFactory.create()
        self.rigby = UserFactory.create(username='rigby')
        self.elenorphoto = PhotoFactory.create(profile=self.elenor.ImagerProfile)
        self.rigbyphoto = PhotoFactory.create(profile=self.rigby.ImagerProfile)
        self.rigbyalbum = AlbumFactory.create(user=self.rigby)
        self.elenoralbum2 = AlbumFactory.create(user=self.elenor)

    def test_user_album(self):
        '''Assert album contains only user's photos'''
        self.assertEqual(self.elenoralbum.user.username, 'elenor')
        self.assertEqual(self.rigbyalbum.user.username, 'rigby')

    def test_title(self):
        '''Assert that album contains a title'''
        self.assertEqual(self.rigbyalbum.title, 'No Title')

    def test_description(self):
        '''Assert album contains description'''
        self.assertEqual(self.rigbyalbum.description, 'No description')

    def test_date_uploaded(self):
        '''Assert album has upload date or null'''

    def test_date_modified(self):
        '''Assert album has modified date or null'''

    def test_date_published(self):
        '''Assert photo has published date or null'''

    def test_private(self):
        '''Assert default privacy option is private; no one can view'''

    def test_shared(self):
        '''Assert option for shared; friends can view'''

    def test_public(self):
        '''Assert option for public; anyone can view that follows'''

    def test_cover(self):
        '''Assert one contained photo as cover for album'''
        self.rigbyalbum.designate_cover(self.rigbyphoto)
        self.assertEqual(self.rigbyalbum.cover, self.rigbyphoto.photo)

