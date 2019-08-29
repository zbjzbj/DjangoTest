from django import forms
from app01.models import *
from django.core.validators import RegexValidator


class RegForm(forms.Form):
    username = forms.CharField(
        min_length=3,
        label='用户名',
        required=True,
        initial="张三",
        error_messages={
            "required": "不能为空",
            "invalid": "格式错误",
            "min_length": "用户名最短3位"
        }
    )
    pwd = forms.CharField(
        min_length=8,
        label='密码',
        # 把密码框设置为password类型，并指定class为c1和c2的样式类
        # 当出现出错时，其他类型的input框默认是保留你写的内容，只有密码框不会保存
        # 想要密码框错误时也保留内容，就设置render_value=True
        widget=forms.widgets.PasswordInput(attrs={'class': 'c1 c2'},
                                           render_value=True)
    )
    gender = forms.ChoiceField(
        choices=((1, "男"), (2, "女")),
        label="性别",
        initial=1,
        widget=forms.widgets.RadioSelect()
    )
    hobby = forms.ChoiceField(
        choices=((1, "篮球"), (2, "足球"), (3, "双色球")),
        label='爱好',
        initial=3,
        widget=forms.widgets.Select()
    )
    hobby2 = forms.MultipleChoiceField(
        choices=((1, "美女"), (2, "游戏"), (3, "大home妹")),
        label='爱好2',
        initial=3,
        widget=forms.widgets.SelectMultiple()
    )
    keep = forms.fields.ChoiceField(
        label="是否记住密码",
        initial="checked",
        widget=forms.widgets.CheckboxInput()
    )
    hobby3 = forms.fields.MultipleChoiceField(
        choices=((1, "读书"), (2, "打架"), (3, "扫黄"),),
        label="爱好3",
        initial=[1, 3],
        widget=forms.widgets.CheckboxSelectMultiple()
    )
    phone = forms.CharField(
        label='手机号码',
        widget=forms.widgets.TextInput(),
        validators=[RegexValidator(r'^1[3-9]\d{9}$', "手机号码不正确")]
    )
#
# ######### 在数据库中查询数据后展示出来 #########
# # 方式一：
# # 重写Form类的__init__，使其每次初始化都去查一次数据库
# class RegForm2(forms.Form):
#     users = forms.fields.MultipleChoiceField(
#         choices=Userinfo.objects.all().values_list('id', 'name'),
#         label='已经注册的用户',
#         initial=[1, 3],
#         widget=forms.widgets.CheckboxSelectMultiple()
#     )
#
#     def __init__(self):
#         super(RegForm2, self).__init__()
#         self.fields['hobby'].choices = Userinfo.objects.all().values_list('id', 'name')
#
# # 方式二：
# # 使用forms.models.ModelMultipleChoiceField
# class RegForm3(forms.Form):
#     users = forms.models.ModelMultipleChoiceField(
#         queryset=Userinfo.objects.all(),  # 使用queryset而不是choices
#         label='已经注册的用户',
#         initial=[1],
#         widget=forms.widgets.CheckboxSelectMultiple()
#     )
#
#
# ####### form校验 ##########
# 方式一：使用RegexValidator
# from django.core.validators import RegexValidator  # 导入使用正则表达的模块
#
# class RegexForm(forms.Form):
#     phone = forms.CharField(
#         label='手机号码',
#         widget=forms.widgets.TextInput(),
#         validators=[RegexValidator(r'^1[3-9]\d{9}$', "手机号码不正确")]
#     )

# 方式二：自定义校验规则
# from django.core.exceptions import ValidationError

# 自定义校验函数
# def check_sb(value):
#     # value就是用户输入的值
#     if 'sb' in value:
#         raise ValidationError('你才是sb')
#
# class ValidationForm(forms.Form):
#     name = forms.CharField(
#         min_length=2,
#         max_length=12,
#         label="用户名",
#         widget=forms.widgets.TextInput(),
#         validators=[check_sb]  # 直接调用自定义的函数
#     )

# 方式三：使用RegexField字段
# class RegexFieldForm(forms.Form):
#     phone = forms.RegexField(
#         label='手机号码',
#         regex=r'^1[3-9]\d{9}$',
#         widget=forms.widgets.TextInput()
#     )

############### 钩子函数(hook) ###########





