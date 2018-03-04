from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from aspc.forum.views import home, question, post, QuestionView, AnswerView, TagView, showAllQuestions, showAllPosts, PostView, showResources, about

urlpatterns = [
    url(r'^$', home, name="forum_home"),
    url(r'^question/$', showAllQuestions, name="all_questions"),
    url(r'^question/(?P<question_id>\d+)/answer/?$', login_required(AnswerView.as_view()), name="new_answer"),
    url(r'^question/new/?$', login_required(QuestionView.as_view()), name="new_question"),
    url(r'^posts/$', showAllPosts, name="all_posts"),
    url(r'^posts/(?P<post_id>\d+)/?$', post, name="post"),
    url(r'^posts/new/?$', login_required(PostView.as_view()), name="new_post"),
    url(r'^question/(?P<question_id>\d+)/?$', question, name="question"),
    url(r'^resources/$', showResources, name="resources"),
    url(r'^about/$', about, name="about"),
    url(r'^tag/$', login_required(TagView.as_view()), name="add_tag")
]