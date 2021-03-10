from studentbio.serialize import studentdataserializer
from rest_framework import viewsets
from studentbio.models import studentdata
from django.shortcuts import render
import requests
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.contrib import messages


class studentdataapi(viewsets.ModelViewSet):
    queryset=studentdata.objects.all()
    serializer_class=studentdataserializer

def displaydata(request):
    tabledata = requests.get('http://127.0.0.1:8000/studentdata/') 
    jtable=tabledata.json()
    return render(request , 'base.html' , {"joindata":jtable})


        

def  postapi(request):
    if request.method=="POST":
        enrollment_id=request.POST.get('enrollment_id')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        dob=request.POST.get('dob')
        mobile_number=request.POST.get('mobile_number')
        email_id=request.POST.get('email_id')
        login_password=request.POST.get('login_password')
        login_otp=request.POST.get('login_otp')
        data={'enrollment_id':enrollment_id,'first_name':first_name,'last_name':last_name,'dob':dob,'mobile_number':mobile_number,'email_id':email_id,'login_password':login_password,'login_otp':login_otp}
        headers={'Content-Type': 'application/json'}
        read=requests.post('http://127.0.0.1:8000/studentdata/',json=data,headers=headers)
        messages.success(request,("New Data Added!"))    
        return render(request,'forms.html')
        
    else:
        return render(request,'forms.html')


class studentupdate(APIView):
    def get_object(self,pk):
        try:
            return studentdata.objects.get(pk=pk)
        except studentdata.DoesNotExit:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    def get(self,request,pk):
        studentj=self.get_object(pk)
        serialj=studentdataserializer(studentj)
        return Response(serialj.data)
    def put(self,request,pk):
        studentj=self.get_object(pk)
        empserial=studentdataserializer(studentj,data=request.data)
        if empserial.is_valid():
            empserial.save()
            return Response(empserial.data,status=status.HTTP_200_OK)
        return Response(empserial.error,status=status.HTTP_400_REQUEST)
#
    def delete(self,request,pk):
        studentj=self.get_object(pk)
        studentj.delete()
        return Response(status=status.HTTP_200_OK) 
           


   
    






