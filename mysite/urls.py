from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]

# include() 함수는 다른 URLconf들을 참조할 수 있도록 도와줍니다. Django가 함수 include()를 만나게 되면, URL의 그 시점까지 일치하는 부분을 잘라내고, 남은 문자열 부분을 후속 처리를 위해 include 된 URLconf로 전달합니다.

# include()에 숨은 아이디어 덕분에 URL을 쉽게 연결할 수 있습니다. polls 앱에 그 자체의 URLconf(polls/urls.py)가 존재하는 한, 《/polls/》, 또는 《/fun_polls/》, 《/content/polls/》와 같은 경로, 또는 그 어떤 다른 root 경로에 연결하더라도, 앱은 여전히 잘 동작할 것입니다.

# 언제 include()를 사용