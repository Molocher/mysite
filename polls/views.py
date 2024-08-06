from django.http import HttpResponse
from django.views.decorators.http import require_http_methods, require_GET, require_POST, require_safe


def index(request):
    return HttpResponse('Hello,world.You are at the polls index.')


@require_GET
def get_request(request):
    pass


@require_POST
def post_request(request):
    pass


@require_http_methods(['GET', 'POST'])
def require_http_request(request):
    pass


from django.http import HttpResponseRedirect
from django.shortcuts import render
from .form import UploadFileForm


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # 处理上传的文件
            handle_uploaded_file(request.FILES["file"])
            # using a ModelForm
            # form.save()
            pass


def handle_uploaded_file(f):
    with open('', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


from django.views.generic.edit import FormView
from .form import FileFieldForm


class FileFieldFormView(FormView):
    form_class = FileFieldForm
    template_name = "upload.html"
    success_url = "...."

    def form_valid(self, form):
        files = form.cleaned_data["file_field"]
        for f in files:
            pass

        return super().form_valid(form)


from django.views import View


class MyView(View):
    http_method_names = 'get'

    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello,World!")


from django.views.generic.base import TemplateView
from .models import Question


class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest_questions"] = Question.objects.all()[:5]
        return context


from django.shortcuts import get_object_or_404
from django.views.generic.base import RedirectView
from .models import Question


class ArticleCounterRedirectVew(RedirectView):
    permanent = False
    query_string = True
    pattern_name = "article-detail"

    def get_redirect_url(self, *args, **kwargs):
        article = get_object_or_404(Question, pk=kwargs["pk"])
        article.update_counter()
        return super().get_redirect_url(*args, **kwargs)


from django.utils import timezone
from django.views.generic.detail import DetailView
from .models import Question


class QuestionDetailView(DetailView):
    model = Question

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context
