from django.urls import path,re_path
from . import views

app_name = "students"


urlpatterns = [
    path('student/',views.create_student,name="create_student" ),
    path('student-list/',views.student_list,name="student_list" ),
    re_path(r'^student-sinle/(?P<pk>.*)/',views.single_student,name="single_student"),
    re_path(r'^student-update/(?P<pk>.*)/',views.update_student,name="update_student"),
    re_path(r'^student-delete/(?P<pk>.*)/',views.delete_student,name="delete_student"),

    #score

    path('score/',views.create_score,name="create_score" ),
    re_path(r'^score-sinle/(?P<pk>.*)/',views.single_score,name="single_score"),

]