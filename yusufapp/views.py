from django.shortcuts import render
from .models import Image

def home (request):
	imgs=Image.objects.all()
	context={
		'imgs':imgs
	}
	return render(request,'index.html',context=context)

