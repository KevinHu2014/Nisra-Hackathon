from django.conf.urls import patterns, include, url
from django.contrib import admin
import message.views as views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'futureMessage.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^login/',views.checkLogin),
	url(r'^login/',views.checkLogin2),
    url(r'^page/login/',views.loginPage),
	url(r'^page/userAdd',views.userAdd),
	url(r'^verifyCheckCode',views.verifyCheckCode),
	url(r'^page/Reg',views.pageReg),
	
)
