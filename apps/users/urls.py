from django.urls import path
from .views import EditProfile

urlpatterns = [
    # path('', ListCandidates.as_view(), name='candidate_list'),
    # path('detail/<int:pk>/', DetailCandidate.as_view(), name='candidate_detail'),
    # path('signup/', CandidateSignUp.as_view(), name="candidate_signup"),
    path('profile/', EditProfile.as_view(), name="user_edit"),
    ]
