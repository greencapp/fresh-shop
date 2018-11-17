from django import forms

from goods.models import GoodsCategory


class GoodsForm(forms.Form):
    goods_front_image = forms.ImageField(required=False)
    name = forms.CharField(max_length=20, required=True,
                           error_messages={
                               'required': '商品名称必填',
                               'max_length': '商品名称长度不超过20个字符'
                           })
    goods_sn = forms.CharField(required=True,
                               error_messages={
                                   'required': '商品货号必填',
                               })
    category = forms.CharField(required=True,
                               error_messages={
                                   'required': '商品类型必填',
                               })
    market_price = forms.FloatField(required=True,
                                    error_messages={
                                        'required': '市场价格必填',
                                    })
    shop_price = forms.FloatField(required=True,
                                  error_messages={
                                      'required': '超市价格必填',
                                  })
    goods_nums = forms.IntegerField(required=True,
                                    error_messages={
                                        'required': '商品数量必填',
                                    })
    goods_brief = forms.CharField(required=True,
                                  error_messages={
                                      'required': '商品描述必填',
                                  })

    def clean_category(self):
        id = self.cleaned_data.get('category')
        category = GoodsCategory.objects.filter(pk=id).first()
        return category
