from django.http import HttpResponse
from django.urls import reverse_lazy
import pyshorteners
from Shortify.forms import UrlForm
from .models import URLShortener
from django.views.generic import FormView
from django.shortcuts import render

class Urlgenerate(FormView):
    template_name = 'home.html'
    form_class = UrlForm
    success_url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)  # Call the parent method to render the form

    def form_valid(self, form):
        link = form.cleaned_data['link']
        try:
            s = pyshorteners.Shortener()
            short_url = s.tinyurl.short(link)

            # Save to the model
            URLShortener.objects.create(original_url=link, short_url=short_url)

            # Prepare context to render
            context = {
                'short_url': short_url,
                'original_url': link,
                'form': form,  # Include the form to re-render it
            }
            return render(self.request, self.template_name, context)
        except Exception as e:
            context = {
                'error': 'Give Valid Url',
                'form': form,  # Include the form to re-render it
            }
            return render(self.request, self.template_name, context)