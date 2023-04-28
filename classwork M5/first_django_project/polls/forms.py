from django import forms

from polls.models import Question


class QuestionForm(forms.ModelForm):
    text = forms.CharField(label="Question text")
    pub_date = forms.DateTimeField()

    class Meta:
        model = Question
        fields = ("text", "pub_date")