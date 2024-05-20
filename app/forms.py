from django import forms


class SchoolForm(forms.Form):
    Sname=forms.CharField(max_length=20)
    Sage=forms.IntegerField()
    Surl=forms.URLField()
    Semail=forms.EmailField()
    Spassword=forms.CharField(widget=forms.PasswordInput)
    Saddress=forms.CharField(widget=forms.Textarea())