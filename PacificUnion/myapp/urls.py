from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.home, name='home'),
    path('analytics/', views.analytics, name='analytics'),
    path('profile/', views.profile, name='profile'),
    path('settings/', views.settings, name='settings'),
    path('support_agent/', views.support_agent, name='support_agent'),
    path('withdraw/', views.withdraw, name='withdraw'),
    path('deposit', views.deposit, name='deposit'),
    path('reg/', views.reg, name='reg'),
    path('OTP/', views.OTP, name='OTP'),
    path('reports/', views.reports, name='reports'),
    path('loginPage/', views.loginPage, name='login'),
    path('logout/', views.LogoutPage, name='LogoutPage'),
    path('pending/', views.pending, name='pending'),
    path('index_page/', views.index_page, name="index_page"),
    path('details/', views.details, name="details"),

    #withdrawal pages

    path('PayPal/', views.PayPal, name='PayPal'),
    path('Payoneer/', views.Payoneer, name='Payoneer'),
    path('Bank_transfer/', views.Bank_transfer, name='Bank_transfer'),
    path('skrill/', views.skrill, name='skrill'),
    path('Google_pay/', views.Google_pay, name='Google_pay'),
    path('trust_wise/', views.trust_wise, name='trust_wise'),
    path('western/', views.Western_Union, name='western'),
    path('crypto_page/', views.Crypto_page, name='crypto_page'),

]