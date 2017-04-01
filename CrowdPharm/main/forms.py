from django import forms

from .models import Medicine

class MedicineForm(forms.ModelForm):
	class Meta:
		model = Medicine
		fields = [
			"medicine_name",
			"expiry_date",
			"batch_no",
			"medicine_id",
			"quantity",
			"image"
		]