from django.urls import path
from .views import all_data, create_student, export_to_pdf, export_to_excel, upload_document

urlpatterns = [
    path('', create_student),
    path('create_student/', create_student),
    path('all/', all_data),
    path('export_pdf/', export_to_pdf, name='export_pdf'),
    path('export_excel/', export_to_excel, name='export_excel'),
    path('student_list/', all_data),
    path('upload_doc/', upload_document, name='document_list'),
]




