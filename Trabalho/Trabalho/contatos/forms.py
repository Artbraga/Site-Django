from django import forms

class ContatoCurso(forms.Form):

    name = forms.CharField(label='Nome (obrigatório)', max_length=30, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label='E-mail (obrigatório)', widget=forms.TextInput(attrs={'class':'form-control'}))
    assunto = forms.CharField(label='Assunto (obrigatório)', widget=forms.TextInput(attrs={'class':'form-control'}))
    mensagem = forms.CharField(label='Mensagem (obrigatório)', widget=forms.Textarea(attrs={'class':'form-control'}))