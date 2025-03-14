from django.http import HttpResponse
from django.urls import reverse_lazy
import pyshorteners
from Shortify.forms import LinkForm
from .models import URLMapping
from django.views.generic import FormView, ListView
from django.shortcuts import render

class LinkGenerator(FormView):
    template_name = 'home.html'
    form_class = LinkForm
    success_url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        url_input = form.cleaned_data['url']
        try:
            shortener = pyshorteners.Shortener()
            shortened_url = shortener.tinyurl.short(url_input)

            URLMapping.objects.create(original_url=url_input, short_url=shortened_url)

            context = {
                'shortened_url': shortened_url,
                'original_url': url_input,
                'form': form,
            }
            return render(self.request, self.template_name, context)
        except Exception as e:
            context = {
                'error_message': 'Please provide a valid URL',
                'form': form,
            }
            return render(self.request, self.template_name, context)

class URLListView(ListView):
    model = URLMapping
    template_name = 'url_list.html' 
    context_object_name = 'url_list' 