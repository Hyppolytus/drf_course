from . import models
#venv/lib/python3.9/site-packages/rest_framework/serializers.py
from rest_framework import serializers
from rest_framework.fields import CharField, EmailField



class ContactSerializer(serializers.ModelSerializer):

    #Very similar to django forms, source means we are trying to get this information from the client.

	name = CharField(source="title", required=True)
	message = CharField(source="description", required=True)
	email = EmailField(required=True)
	
    # This directs the ser. to the model that we have.
	class Meta:
		model = models.Contact
		fields = (
			'name',
			'email',
			'message'
		)