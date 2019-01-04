from django.db import models
from user import models as usermodels


# Create your models here.
# 需求分类

class Classification(models.Model):
    catagory = models.CharField(max_length=20)

    class Meta:
        db_table = "classification"

class Demand(models.Model):
    # 信息发布者id，外键
    uerid = models.ForeignKey(usermodels.Userinfo, on_delete=models.CASCADE)
    # 发布标题
    title = models.CharField(max_length=50, null=False)
    # 发布内容
    comment = models.CharField(max_length=250, null=False)
    # 地域要求
    area = models.CharField(max_length=50)
    # 上传的图片
    image = models.ImageField(upload_to='media/')
    # 截止日期
    endtime = models.DateField(auto_now=True)
    # 赏金
    money = models.DecimalField(max_digits=10, decimal_places=2)
    # 联系方式
    wechar = models.CharField(max_length=20, null=True)  # 威信
    QQ = models.CharField(max_length=20, null=True)  # qq
    tel = models.CharField(max_length=11, null=True)  # tel
    #需求分类
    catagoryid = models.ForeignKey(Classification,on_delete=models.CASCADE,default=1)

    class Meta:
        db_table = "demand"


