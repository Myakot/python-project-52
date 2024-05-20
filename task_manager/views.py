from django.shortcuts import render


class IndexView(TemplateView):
    template_name = 'index.html'
    extra_context = {'title': _('Task manager')}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
