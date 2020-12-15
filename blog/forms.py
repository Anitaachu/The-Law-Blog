from django import forms
from django import forms

TAG_CHOICES =( 
    ("1", "Private Law"), 
    ("2", "Public Law"), 
    ("3", "International Law"), 
    ("4", "Jurisprudence"), 
    ("5", "Others"), 
) 
  

class InputForm(forms.Form):
    Title = forms.CharField(max_length = 200) 
    Tag_field = forms.ChoiceField(choices = TAG_CHOICES)
    Author = forms.CharField(max_length = 50)
    Body = forms.CharField(max_length = 2000, widget=forms.Textarea(),
        help_text='Write here your blog post!'
    )

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['fullname'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user