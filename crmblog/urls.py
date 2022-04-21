from django.urls import path
from .views import *

app_name = 'lead'

urlpatterns = [
    path("leads/", Leads.as_view(), name='leads'),
    path("<int:pk>/", DetailsLead.as_view(), name='leads_info'),
    path("<int:pk>/update/", UpdateLead.as_view(), name='update_lead'),
    path("<int:pk>/delete/", DeleteLead.as_view(), name='delete_lead'),
    path("<int:pk>/agent-assign/", AgentAssignView.as_view(), name='assign_agent'),
    path("create/", CreateLead.as_view(), name='create_lead'),
    path("category-assign/", CategoryAssignView.as_view(), name='category_lead'),
]
