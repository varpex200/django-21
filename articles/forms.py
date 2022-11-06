from django.forms import ModelForm

from articles.models import Article, Car


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