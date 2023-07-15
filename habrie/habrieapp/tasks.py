import csv
import pandas as pd
from celery import shared_task
from django.http import HttpResponse
from .models import AcademicDetail, Document, Parent, Student
from csvs.models import Csv
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


@shared_task
def csv_upload():
    obj = Csv.objects.get(activated=False)
    with open(obj.file_name.path, 'r') as f:
            
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                if i==0:
                    pass
                else:
                    # print(row[0])
                    academic_data = {
                            'enroll_id': row[25],
                            'class_id': row[26],
                            'section_id': row[27],
                            'doj': row[28],
                            'session': row[30]
                    }
                    # AcademicDetail.objects.update_or_create(enroll_id=row[25], defaults=academic_data)
                    if not all(value == '' for value in academic_data.values()):
                        academic_detail, _ = AcademicDetail.objects.update_or_create(
                                                                                        enroll_id=row[25],
                                                                                        defaults=academic_data,
                                                                                        session = row[30]
                                                                                    )
                    academic_detail = AcademicDetail.objects.get(enroll_id=row[25])
                    student_data = {
                            'name': row[0],
                            'gender': row[1],
                            'aadhar': row[2],
                            'dob': row[3],
                            'id_mark': row[4],
                            'addmission_cat': row[5],
                            'height': row[6],
                            'weight': row[7],
                            'mail': row[8],
                            'contact': row[9],
                            'address': row[10],
                            'enroll_number': academic_detail,
                    }
                    student, _ = Student.objects.update_or_create(name=row[0], defaults=student_data)
                    
                    parent_data = {
                            'student_name': student,
                            'father_name': row[11],
                            'father_qualification': row[12],
                            'father_profession': row[13],
                            'father_designation': row[14],
                            'father_aadhar': row[15],
                            'father_number': row[16],
                            'father_mail': row[17],
                            'mother_name': row[18],
                            'mother_qualification': row[19],
                            'mother_profession': row[20],
                            'mother_designation': row[21],
                            'mother_aadhar': row[22],
                            'mother_number': row[23],
                            'mother_mail': row[24],
                    }
                    Parent.objects.update_or_create(student_name=student, defaults=parent_data)

                    document_data = {
                            'student_name': student,
                    }
                    Document.objects.update_or_create(student_name=student, defaults=document_data)
            obj.activated = True 
            obj.save()  
    return "DONE"


@shared_task
def send_templated_email(recipient_email, recipient_name, enroll_no, class_id, section, session):
    subject = 'Templated Email'
    from_email = 'nitin.ekka30@gmail.com'
    to = ['nitin.ekka30@gmail.com']
    
    student_email_content = render_to_string('student_mail.html', {'recipient_name': recipient_name, 'enroll_no': enroll_no, 'class_id': class_id, 'section': section, 'session': session})
    admin_email_content = render_to_string('admin_mail.html', {'recipient_name': recipient_name, 'enroll_no': enroll_no, 'class_id': class_id, 'section': section, 'session': session})
    email_student = EmailMessage(subject, student_email_content, from_email, to)
    email_student.content_subtype = 'html'
    email_student.send()


    # admin_html = strip_tags(admin_email_content)
    email_admin = EmailMessage(subject, admin_email_content, from_email, to)
    email_admin.content_subtype = 'html'
    email_admin.send()
    
    
