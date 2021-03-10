#!/usr/bin/env python3
# -*-encoding: utf-8-*-

from rest_framework import serializers
from accounts.models import User


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
