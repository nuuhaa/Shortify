from django.urls import reverse_lazy
import pyshorteners
from Shortify.forms import UrlForm
from .models import URLShortener
from django.views.generic import FormView

class Urlgenerate(FormView):
    template_name = 'home.html'
    form_class = UrlForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        link = form.cleaned_data['link']
        try:
            s = pyshorteners.Shortener()
            short_url = s.tinyurl.short(link)

            # Save to the model
            URLShortener.objects.create(original_url=link, short_url=short_url)

            self.success_url += f'?link={short_url}'
        except Exception as e:
            self.success_url += f'?link=Give Valid Url'
        return super().form_valid(form)