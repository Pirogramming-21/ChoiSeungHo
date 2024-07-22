from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)  # 제목
    content = models.TextField()  # 내용
    created_at = models.DateTimeField(auto_now_add=True)  # 작성 시간

    def __str__(self):
        return self.title


class Like(models.Model):
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)  # Post 모델의 외래키

    def __str__(self):
        return f'Like for {self.post.title}'


class Comment(models.Model):
    content = models.TextField()  # 댓글의 내용
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)  # Post 모델의 외래키
    created_at = models.DateTimeField(auto_now_add=True)  # 댓글 작성 시간

    def __str__(self):
        return f'Comment by {self.post.title}'
