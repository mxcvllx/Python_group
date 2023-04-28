from django.urls import path

from . import views

app_name = "polls"

urlpatterns = [
    path('capybara.wiki/', views.information_about_capybara, name='information_about_capybara'),
    path('polls/', views.homepage, name="homepage"),
    path('urgent-news/', views.urgent_news, name='urgent_news'),
    path('test/', views.test, name='test'),
    path('wikipedia.org/wiki/Тамерлан/', views.tamerlan, name='tamerlan'),
    path('questions/', views.questions_list, name='questions_list'),
    path('questions/<int:question_id>/', views.question_detail, name="question_detail"),
    path('questions/<int:question_id>/vote/', views.question_vote, name='question_vote'),
    path('questions/add/', views.question_add, name='question_add'),
]
