from django import forms
import os
from student.models import Student


class StudentUploadForm(forms.Form):
    file = forms.FileField(
        required=True,
        error_messages={'required': 'Please upload an Excel or CSV file.'}
    )

    def clean_file(self):
        uploaded_file = self.cleaned_data.get('file')
        if uploaded_file:
            ext = os.path.splitext(uploaded_file.name)[1].lower()
            if ext not in ['.csv', '.xls', '.xlsx']:
                raise forms.ValidationError('Only Excel or CSV files are allowed.')
        return uploaded_file


class StudentEditForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'address', 'email']