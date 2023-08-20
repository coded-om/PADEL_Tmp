from django.contrib import admin
from .models import Coustomer


class Main_App_Admin(admin.ModelAdmin):
    list_display = ["UserName", "UserNum", "Amount", "PymentWay", "Time"]
    search_fields = ["UserName"]
    list_filter = ["PymentWay", "Amount"]


# Register your models here.
admin.site.register(Coustomer, Main_App_Admin)
admin.site.site_header = "Royale Padel"
admin.site.site_title = "Royale Padel"
