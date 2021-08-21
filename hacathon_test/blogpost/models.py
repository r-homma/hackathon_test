from django.db import models

# Create your models here.
class SampleModel(models.Model):
    title = models.CharField(max_length=100)
    number = models.IntegerField()

CATEGORY = (('network','ネットワーク'),('linux','lunux'),('other','その他'),('web','web'),('programming','プログラミング'))#('左','右')左：pythonの実装で表示される項目,右：htmlファイル上で表示される項目
class BlogModel(models.Model):#以下で定義される変数は、全てオブジェクト
    title = models.CharField(max_length=100)
    question = models.TextField()
    answer = models.TextField(null=True)
    postdate = models.DateField(auto_now_add=True)
    category = models.CharField(max_length = 50, choices = CATEGORY)
    def __str__(self):#特殊メソッド。オブジェクトの文字列表現を返す。
        return self.title