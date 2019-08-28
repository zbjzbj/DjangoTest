from django import forms


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