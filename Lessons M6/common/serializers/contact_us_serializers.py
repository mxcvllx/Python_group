from rest_framework import serializers

from common.models.contact_us_models import ContactUs


class ContactUsListSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=False)

    class Meta:
        model = ContactUs
        fields = ['id', 'country', 'city', 'street', 'location', 'email', 'phone']