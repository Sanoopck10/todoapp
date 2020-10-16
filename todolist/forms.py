from django import forms

class TodoListForm(forms.Form):
    text = forms.CharField(max_length = 50, widget = forms.TextInput(
        attrs = {'class': 'form-control', 'placeholder': 'Enter todo e.g. Do exercise',
         'aria-lable': 'Todo', 'aria-describeby': 'add-btn' }))