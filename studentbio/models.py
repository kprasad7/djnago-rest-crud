from django.db import models 

class studentdata(models.Model):
    enrollment_id=models.IntegerField(primary_key=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    dob=models.CharField(max_length=10)
    mobile_number=models.CharField(max_length=20)
    email_id=models.CharField(max_length=100)
    login_password=models.CharField(max_length=100)
    login_otp=models.IntegerField()
    
    
    