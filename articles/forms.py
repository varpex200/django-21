from django.forms import ModelForm, HiddenInput

from articles.models import Article, Car, Comment


class CarForm(ModelForm):
    class Meta:
        model = Car
        #fields = ['title', 'description']
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(CarForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        widgets = {
            'related_user': HiddenInput(),
            'related_article': HiddenInput()
        }
    
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'