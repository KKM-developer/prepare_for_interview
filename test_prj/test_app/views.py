from django.shortcuts import render
from django.http import HttpResponse
from .models import GoodItem
from django.views.generic import TemplateView

def index(request):
    return HttpResponse(f'hello')

def ajax_test(request):
    return HttpResponse('<h1>AJAX</h1>', content_type='text/html')

def goods_list(request):
    all_goods = GoodItem.objects.all()
    context = {
        'page_header': 'Все товары',
        'goods': all_goods,
    }
    return render(request, template_name='goods_list.html', context=context)

class GoodsList(TemplateView):
    template_name = 'goods_list.html'

    def get_context_data(self, **kwargs):
        all_goods = GoodItem.objects.all()
        context =  super().get_context_data(**kwargs)
        context.update({
            'page_header': 'Все товары',
            'goods': all_goods,
        })
        return context

