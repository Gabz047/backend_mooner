from rest_framework import mixins, parsers, viewsets

from core.uploader.models import Document, Image
from core.uploader.serializers import DocumentUploadSerializer, ImageUploadSerializer
from utils.images_filter import ImagesFilter
from django_filters.rest_framework import DjangoFilterBackend

class CreateViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    pass


class DocumentUploadViewSet(CreateViewSet):
    queryset = Document.objects.all() # pylint: disable=no-member
    serializer_class = DocumentUploadSerializer
    parser_classes = [parsers.FormParser, parsers.MultiPartParser]


class ImageUploadViewSet(CreateViewSet):
    queryset = Image.objects.all() # pylint: disable=no-member
    serializer_class = ImageUploadSerializer
    parser_classes = [parsers.FormParser, parsers.MultiPartParser]
    filter_backends = [DjangoFilterBackend]
    filterset_class = ImagesFilter
