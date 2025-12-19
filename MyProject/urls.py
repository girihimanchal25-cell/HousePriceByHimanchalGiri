from MyApp import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('file',views.file, name='file'),
    path('adddata',views.addData),
    path('readData',views.readData, name='readData'),
    path('deletedetails/<int:id>',views.deletedetails,name="deletedetails"),
    # path('done',views.done),
    path('addfromcsv',views.addfromcsv),
    path('addfromexcel',views.addfromexcel),
    path('update/ <int:id>',views.update, name="update"),
    path('prediction',views.prediction),
    path('admin/', admin.site.urls),

]
