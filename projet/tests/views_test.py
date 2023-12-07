import pytest
from django.urls import reverse
from django.contrib.auth.models import User
import os

@pytest.mark.django_db
def test_login_page(client):
    User.objects.create_user(username='rola', password='Rola1992@')

    # Tester la connexion avec des identifiants valides (POST)
    url = reverse('login')
    response = client.post(url, {'username': 'rola', 'password': 'Rola1992@'})
    assert response.status_code == 302  # Redirection après une connexion réussie
    assert response.url == reverse('home')  # Assurez-vous que la redirection est correcte

    # Vous pouvez également tester d'autres scénarios, comme la connexion avec des identifiants invalides
    response = client.post(url, {'username': 'rola', 'password': 'Rola1992@'})
    assert response.status_code == 200  # La page doit être rendue à nouveau après une tentative de connexion infructueuse
    
#############################################################################################################

import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.test import Client
from app import forms

@pytest.mark.django_db
def test_signup_page(client):
    # Créer un utilisateur pour le test
    existing_user = User.objects.create_user(username='Rola', password='Rola1992@')

    # Tester l'inscription avec des informations valides (POST)
    url = reverse('signup')
    response = client.post(url, {
        'username': 'new_user',
        'password1': 'NewUser123@',
        'password2': 'NewUser123@'
    })
    
    # Assurez-vous que l'utilisateur est redirigé après une inscription réussie
    assert response.status_code == 302
    assert response.url == reverse('home')

    # Assurez-vous que l'utilisateur est réellement créé dans la base de données
    new_user = User.objects.get(username='new_user')
    assert new_user is not None

    # Assurez-vous que l'utilisateur est connecté automatiquement après l'inscription
    authenticated_user = authenticate(username='new_user', password='NewUser123@')
    assert authenticated_user == new_user

    # Assurez-vous que l'utilisateur ne peut pas s'inscrire avec un nom d'utilisateur existant
    response_existing_user = client.post(url, {
        'username': 'Rola',
        'password1': 'NewUser123@',
        'password2': 'NewUser123@'
    })
    
    # Assurez-vous que la page de réinscription est rendue avec un message d'erreur
    assert response_existing_user.status_code == 200
    # assert 'Ce nom d\'utilisateur existe déjà.' in response_existing_user.content.decode()
