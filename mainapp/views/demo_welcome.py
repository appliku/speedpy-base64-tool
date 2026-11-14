from django.views.generic import TemplateView


class DemoWelcomeView(TemplateView):
    template_name = "mainapp/welcome_demo.html"