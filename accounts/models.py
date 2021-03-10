from django.db import models
import jwt
from datetime import datetime, timedelta
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):

    """
    custom manager user class for own authentication
    """

    def create_user(self, username, email, password=None):

        """ create and return user with mail, password and username """

        if username is None:
            raise TypeError('Users must have a username.')

        if email is None:
            raise TypeError('Users must have an email address.')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password):

        """ Create and return a user with admin privileges. """

        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    # Each user needs a human-readable unique identifier,
    # which we can use to provide User in the user
    # interface. We will also index this column in the database for
    # improve search speed in the future.
    username = models.CharField(db_index=True, max_length=255, unique=True)

    # We also need a field with which we will be able to
    # contact the user and identify him at login.
    # Since we need the email address anyway, we will also
    # use it for logins, as it is the most
    # the most common form of credentials at the moment.
    email = models.EmailField(db_index=True, unique=True)

    # When a user no longer wants to use our system, he can
    # want to delete your account. This is a problem for us, since the collected
    # data is very valuable for us, and we do not want to delete it. We just offer
    # for users a way to deactivate the account instead of completely deleting it.
    # This way they won't show up on the site, but we can still
    # further analyze the information.
    is_active = models.BooleanField(default=True)

    # This flag determines who can log into the admin area of our
    # site. For most users, this flag will be false.
    is_staff = models.BooleanField(default=False)

    # Timestamp of object creation.
    created_at = models.DateTimeField(auto_now_add=True)

    # Timestamp showing when the object was last updated.
    updated_at = models.DateTimeField(auto_now=True)

    # Additional fields required by Django
    # when specifying a custom user model.

    # The USERNAME_FIELD property tells us which field we will use
    # to login. In this case, we want to use mail.
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    # Tells Django that the UserManager class defined above is
    # must manage objects of this type.
    objects = UserManager()

    def __str__(self):
        """ String representation of the model (displayed in the console) """
        return self.email

    @property
    def token(self):
        """
        Lets get the user's token by calling user.token, instead of
        user._generate_jwt_token (). The @property decorator above does this
        possible.
        """
        return self._generate_jwt_token()

    def get_full_name(self):
        """
        This method is required by Django for things like handling email
        mail. This is usually the user's first name, but since we do not
        use them, we will return username.
        """
        return self.username

    def get_short_name(self):
        """ Same as get_full_name() method. """
        return self.username

    def _generate_jwt_token(self):
        """
        Generate a JSON web token that stores the ID of this
        user, the token validity period is 1 day from creation
        """
        dt = datetime.now() + timedelta(days=1)

        token = jwt.encode({
            'id': self.pk,
            'exp': int(dt.strftime('%s'))
        }, settings.SECRET_KEY, algorithm='HS256')

        return token.decode('utf-8')
