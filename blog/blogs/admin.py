from django.contrib import admin
from .models import ARTICLE, TALLY, COMMENT, KIND
# Register your models here.


class KINDAdmain(admin.ModelAdmin):
    list_display = ['k_content']


class ARTICLEAdmain(admin.ModelAdmin):
    list_display = ['title', 'date']


class COMMENTAdmain(admin.ModelAdmin):
    list_display = ['c_content']


class TALLYAdmain(admin.ModelAdmin):
    list_display = ['t_content']


admin.site.register(ARTICLE, ARTICLEAdmain)
admin.site.register(TALLY, TALLYAdmain)
admin.site.register(COMMENT, COMMENTAdmain)
admin.site.register(KIND, KINDAdmain)
