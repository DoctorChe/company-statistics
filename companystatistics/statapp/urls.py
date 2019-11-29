from django.urls import path

from . import views

app_name = 'statapp'

urlpatterns = [
    path('company/<slug:company>)/',
         views.DepartmentListView.as_view(),
         name='department_list_company'),
    path('<slug:slug>/',
         views.DepartmentDetailView.as_view(),
         name='department_detail'),
    path('<int:department_id>/stat_title_create/',
         views.stat_title_create,
         name='stat_title_create'),
    path('<int:stat_title_id>/stat_create/',
         views.stat_create,
         name='stat_create'),
    path('<int:stat_id>/stat_edit/',
         views.stat_edit,
         name='stat_edit'),
]
