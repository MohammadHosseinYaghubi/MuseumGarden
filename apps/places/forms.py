from django import forms

class MessageForm(forms.Form):
    full_name=forms.CharField(label='نام و نام خانوادگی',
                              widget=forms.TextInput(attrs=
                                {'placeholder':'نام و نام خانوادگی'}),
                            error_messages={"required":"این فیلد نمی تواند خالی باشد"},)
    email=forms.EmailField(label='ایمیل',
                           widget=forms.EmailInput(attrs=
                                {'placeholder':'ایمیل'}),
                            error_messages={"required":"این فیلد نمی تواند خالی باشد"},)
    subject=forms.CharField(label='عنوان پیام',
                            widget=forms.Textarea(attrs=
                                    {'placeholder':'عنوان پیام', 'rows':'1'}),
                            error_messages={"required":"این فیلد نمی تواند خالی باشد"},)
    message=forms.CharField(label='متن پیام', widget=forms.Textarea(attrs=
                                {'placeholder':'متن پیام', 'rows':'4'}),
                            error_messages={"required":"این فیلد نمی تواند خالی باشد"},)