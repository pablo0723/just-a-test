from rest_framework import serializers

from component.personal.models import ProfileType, Title, Gender, Ethnicity, Profile


class ProfileTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileType
        fields = [
            'id',
            'profile_type',
            'description'
        ]


class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Title
        fields = [
            'id',
            'title'
        ]


class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = [
            'id',
            'gender'
        ]


class EthnicitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ethnicity
        fields = [
            'id',
            'ethnicity'
        ]


class AuthSerializer(serializers.ModelSerializer):
    profile_type = ProfileTypeSerializer(many=True, read_only=True)
    title = TitleSerializer()

    class Meta:
        model = Profile
        fields = [
            'id',
            'username',
            'title',
            'first_name',
            'initials',
            'last_name',
            'email',
            'profile_type',
            'terms_and_conditions',
        ]
