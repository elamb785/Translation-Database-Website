from django.conf import settings
from django.shortcuts import render
from django.views import View

languages = [
    {
        'title': 'English',
        'year': 2020,
    },
    {
        'title': 'Spanish',
        'year': 2020,
    },
]


class LangView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request, 'languages/index.html', context={
                'languages': languages,
            }
        )
