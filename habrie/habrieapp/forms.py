from django import forms
from .models import Student, Parent, AcademicDetail, Document

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        exclude = ['enroll_number']

class ParentForm(forms.ModelForm):
    class Meta:
        model = Parent
        exclude = ('student_name',)

class AcademicDetailForm(forms.ModelForm):
    class Meta:
        model = AcademicDetail
        fields = '__all__'
        exclude = ['enroll_id']


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = '__all__'
        # exclude = ('student_name',)
