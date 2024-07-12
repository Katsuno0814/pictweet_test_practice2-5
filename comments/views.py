from django.shortcuts import render, redirect
from django.views import View
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')
class CommentCreateView(View):
    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.tweet_id = kwargs['pk']
            comment.save()
            return redirect('Tweets:detail', pk=comment.tweet_id)
        else:
            # フォームが不正な場合の処理。
            return render(request, 'tweets:detail', {'form': form, 'pk': comment.tweet_id})