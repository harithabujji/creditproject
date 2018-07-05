from creditapp.views import *

app_name="creditapp"

urlpatterns=[
    #path('crd/',CardView.as_view(),name="cards"),

    path('cards/', CreditList.as_view(), name="credit_list"),

    path('cards/add/', AddCard.as_view(), name="add_card"),

    path('cards/<int:pk>/edit/', EditCard.as_view(), name="edit_card"),

    path('cards/<int:pk>/delete/', DeleteCard.as_view(), name="delete_card"),

    path('login/', LoginController.as_view(), name="login"),

    path('logout/', logout_user, name="logout"),
        ]