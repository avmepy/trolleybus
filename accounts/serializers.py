#!/usr/bin/env python3
# -*-encoding: utf-8-*-

from rest_framework import serializers
from accounts.models import User
from django.contrib.auth import authenticate


class RegistrationSerializer(serializers.ModelSerializer):
    """ Serializing user registration and creating a new one. """

    # Make sure the password contains at least 8 characters, no more than 128,
    # and also that it cannot be read by the client side
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    # The client side should not be able to send a token along with
    # registration request. it is read-only.
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:

        model = User
        fields = ['email', 'username', 'password', 'token']

    def create(self, validated_data):
        # Use the create_user method that we
        # written earlier to create a new user.
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=255, read_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        # In the validate method, we make sure that the current instance
        # LoginSerializer value valid. If a user is logged in
        # this means confirmation that an email address is present
        # mail and that this combination matches one of the users.
        email = data.get('email', None)
        password = data.get('password', None)

        if email is None:
            raise serializers.ValidationError(
                'An email address is required to log in.'
            )

        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )

        # The authenticate method is provided by Django and checks that
        # the provided mail and password correspond to some user in
        # our database. We pass the email as username, as in the model
        # user USERNAME_FIELD = email.
        user = authenticate(username=email, password=password)

        # If the user with the given mail / password is not found, then authenticate
        # will return None. Raise an exception in this case.
        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password was not found.'
            )

        # Django provides the is_active flag for the User model. Its purpose
        # tell if the user has been deactivated or blocked.
        # It's worth checking, throwing an exception if True.
        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated.'
            )

        # The validate method should return a word of validated data. it
        # data that is transmitted incl. to create and update methods.
        return {
            'email': user.email,
            'username': user.username,
            'token': user.token
        }


class UserSerializer(serializers.ModelSerializer):
    """ Serializes and deserializes User objects. """

    # Password must be between 8 and 128 characters. This is the standard rule. we
    # could override this in our own way, but that would create extra work for
    # us, without adding real benefits, so let's leave it as it is.
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'token',)

        # The read_only_fields parameter is an alternative to explicitly specifying the field
        # using read_only = True as we did for the password above.
        # Reason why we want to use 'read_only_fields' here
        # is that we don't need to specify anything about the field. In field
        # the password requires the min_length and max_length properties,
        # but this does not apply to the token field.
        read_only_fields = ('token',)

    def update(self, instance, validated_data):
        """ Updates User. """

        # Unlike other fields, passwords should not be processed with
        # setattr. Django provides a function that handles passwords
        # hashing and 'salting'. This means that we need to remove the field
        # password from dictionary 'validated_data' before using it further.
        password = validated_data.pop('password', None)

        for key, value in validated_data.items():
            # For keys remaining in validated_data, we set values
            # into the current User instance, one at a time.
            setattr(instance, key, value)

        if password is not None:
            # 'set_password ()' solves all security issues
            # when updating the password, so we don't need to worry about that.
            instance.set_password(password)

        # After everything has been updated, we must save our instance
        # User. It's worth noting that set_password () doesn't save the model.
        instance.save()

        return instance
