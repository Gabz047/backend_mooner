import cloudinary.uploader
import uuid
from rest_framework import serializers
from core.uploader.helpers.files import CONTENT_TYPE_JPG, CONTENT_TYPE_PNG
from core.uploader.models import Image



class ImageUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ["id","attachment_key", "file", "description", "uploaded_on", "url"]
        read_only_fields = ["attachment_key", "uploaded_on", "url"]
        extra_kwargs = {"file": {"write_only": True}}

    def validate_file(self, value):
        valid_content_types = [CONTENT_TYPE_JPG, CONTENT_TYPE_PNG]
        if value.content_type not in valid_content_types:
            raise serializers.ValidationError("Invalid or corrupted image.")
        return value

    def create(self, validated_data):
        file = validated_data.pop('file')
        folder = "Mooner/images/"
        response = cloudinary.uploader.upload(
            file,
            folder=folder,
            resource_type='raw',
        )
        validated_data['file'] = response['asset_folder']
        validated_data['url'] = response['secure_url']
        validated_data['public_id'] = uuid.uuid4()
        image = Image.objects.create(**validated_data)
        return image

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ["url", "description", "uploaded_on"]
        read_only_fields = ["url", "attachment_key", "uploaded_on"]

    def create(self, validated_data):
        raise NotImplementedError("Use ImageUploadSerializer to create images.")
