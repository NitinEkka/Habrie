from django.db import models

class AcademicDetail(models.Model):
    enroll_id = models.CharField(max_length=20)
    class_id = models.CharField(max_length=20)
    section_id = models.CharField(max_length=20)
    doj = models.DateField()
    session = models.CharField(max_length=30, null=True)

    def __str__(self):
        return str(self.enroll_id)

class Student(models.Model):
    enroll_number = models.ForeignKey(AcademicDetail, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=250, primary_key=True)
    gender = models.CharField(max_length=20)
    aadhar = models.CharField(max_length=20)
    dob = models.DateField()
    id_mark = models.CharField(max_length=250)
    addmission_cat = models.CharField(max_length=50)
    height = models.CharField(max_length=30)
    weight = models.CharField(max_length=30)
    mail = models.EmailField()
    contact = models.CharField(max_length=13)
    address = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)
    
class Parent(models.Model):
    student_name = models.ForeignKey(Student, on_delete=models.CASCADE)
    father_name = models.CharField(max_length=30)
    father_qualification = models.CharField(max_length=30)
    father_profession = models.CharField(max_length=30)
    father_designation = models.CharField(max_length=250)
    father_aadhar = models.CharField(max_length=20)
    father_number = models.CharField(max_length=13)
    father_mail = models.EmailField()
    mother_name = models.CharField(max_length=30)
    mother_qualification = models.CharField(max_length=13)
    mother_profession = models.CharField(max_length=100)
    mother_designation = models.CharField(max_length=100)
    mother_aadhar = models.CharField(max_length=30)
    mother_number = models.CharField(max_length=13)
    mother_mail = models.EmailField()

    def __str__(self):
        return str(self.father_name)
    


    

class Document(models.Model):
    student_name = models.ForeignKey(Student, on_delete=models.CASCADE)
    document_name = models.FileField(upload_to='document', null=True)
    

    def __str__(self):
        return str(self.student_name)
    









