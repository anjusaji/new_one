from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from .models import Tweet


class TweetList(generic.ListView):
	model = Tweet
	template_name = 'tweets/tweet-list.html'
	context_object_name = 'tweets'
	queryset = Tweet.objects.all().order_by('-created_on')


class CreateTweet(LoginRequiredMixin, generic.CreateView):
	model = Tweet
	fields = ('text', 'photo')
	template_name = 'tweets/create-tweet.html'
	success_url = reverse_lazy('tweets:tweet_list')
	
	def form_valid(self, form):
		tweet = form.save(commit=False)
		tweet.user = self.request.user
		tweet.save()
		
		return redirect(self.success_url)
