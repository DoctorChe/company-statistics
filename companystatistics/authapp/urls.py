from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy

import authapp.views as authapp
from authapp import views

app_name = 'authapp'

urlpatterns = [
    path('login/', authapp.user_login, name='login'),
    path('logout/', authapp.user_logout, name='logout'),
    path('edit/', authapp.user_edit, name='edit'),
    path('profile/', authapp.user_profile, name='profile'),

    # change password urls
    path('password_change/',
         auth_views.PasswordChangeView.as_view(
             success_url=reverse_lazy('authapp:password_change_done')
         ),
         name='password_change'),
    path('password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(),
         name='password_change_done'),

    # reset password urls
    path('password_reset/',
         auth_views.PasswordResetView.as_view(
             success_url=reverse_lazy('authapp:password_reset_done')
         ),
         name='password_reset'),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),

    # path('enroll-department/',
    #      authapp.UserEnrollDepartmentView.as_view(),
    #      name='user_enroll_department'),
    #
    # path('departments/',
    #      views.UserDepartmentListView.as_view(),
    #      name='user_department_list'),
    # path('department/<pk>/',
    #      views.UserDepartmentDetailView.as_view(),
    #      name='user_department_detail'),
    # path('department/<pk>/<card_id>/',
    #      views.UserDepartmentDetailView.as_view(),
    #      name='user_department_detail_card'),
]
