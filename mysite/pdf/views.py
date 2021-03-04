from django.shortcuts import render
from django.views.generic import CreateView,DetailView
from .models import Profile
from .forms import ProfileForm

import pdfkit

# config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin')
# pdfkit.from_url(configuration=config)

from django.http import HttpResponse
from django.template import loader

# Create your views here.


class CreateProfile(CreateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'pdf/profile_form.html'

class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'pdf/profile_detail.html'
    context_object_name = 'user_cv'



def create_pdf(request,pk):

    user_cv = Profile.objects.get(pk=pk)
    template = loader.get_template('pdf/profile_detail.html')
    html = template.render({'user_cv':user_cv})
    options = {
                'page-size':'Letter',
                'encoding':'UTF-8',
                }
    pdf = pdfkit.from_string(html,False,options)
    response = HttpResponse(pdf,content_type="application/pdf")
    response['Content-Disposition'] = 'attachment'
    filename = "resume.pdf"
    return response





#




#
# import pdfkit
# from django.http import HttpResponse
# from django.template import loader
#
# def create_pdf(request):
#     html = loader.render_to_string('invoice.html', {})
#     output= pdfkit.from_string(html, output_path=False)
#     response = HttpResponse(content_type="application/pdf")
#     response.write(output)
#     return response
