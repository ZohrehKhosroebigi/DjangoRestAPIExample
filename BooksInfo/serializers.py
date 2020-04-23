from rest_framework import serializers
from .models import books #import model
from django.shortcuts import render

class booksSerializer(serializers.ModelSerializer):
    class Meta:
        model=books
        fields='__all__'

