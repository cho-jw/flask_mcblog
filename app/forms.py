from flask_wtf import FlaskForm  # 从flask_wtf包中导入FlaskForm类
from wtforms import StringField, PasswordField, BooleanField, SubmitField  # 导入这些类
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired()])
    password = PasswordField('密 码', validators=[DataRequired()])
    remember_me = BooleanField('记住我')
    submit = SubmitField('Sign In')
