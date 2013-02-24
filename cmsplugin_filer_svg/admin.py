from django.contrib import admin
from filer.admin.fileadmin import FileAdmin
from models import Svg

admin.site.register(Svg, FileAdmin) # use the standard FileAdmin