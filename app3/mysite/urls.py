from django.conf.urls import include, url
from django.contrib import admin
from kilogram import views as kilogram_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', login_required(kilogram_views.IndexView.as_view()), name = "root"),
    url(r'^kilogram/', include('kilogram.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/signup/$',kilogram_views.CreateUserView.as_view(), name = 'signup'),
    url(r'^accounts/signup/done/$', kilogram_views.RegisteredView.as_view(), name = 'create_user_done'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
