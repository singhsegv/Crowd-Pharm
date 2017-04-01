from django.http import HttpResponse
from django.shortcuts import render
from .models import Medicine
from .forms import MedicineForm
import json
# Create your views here.

def index(request):
	medicine_list = Medicine.objects.all()
	li = []

	for q in medicine_list:
		di = {}
		di['name'] = q.medicine_name
		di['batch'] = q.batch_no
		di['quant'] = q.quantity
		di['exp'] = str(q.expiry_date)
		di['id'] = q.medicine_id

		li.append(di)

	print(li)
	json_string = json.dumps(li)

	return HttpResponse(json_string)


def input_med(request):
	form = MedicineForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance = form.save()
	context = {
		"form" : form,
	}
	return render(request, 'main/forms.html', context)

def display(request):
	medicine_list = Medicine.objects.all()
	context = {

		"medicine_list" : medicine_list
	}
	return render(request, "main/display.html", context)
