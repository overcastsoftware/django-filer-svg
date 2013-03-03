'''
Created on 24 Feb 2013

@author: cooke
'''
from filer.models.filemodels import File
from filer.fields.file import FilerFileField
from cms.models import CMSPlugin
import os
from django.utils.translation import ugettext_lazy as _

class Svg(File):
    #file_type = 'Svg'
    @classmethod
    def matches_file_type(cls, iname, ifile, request):
        # the extensions we'll recognise for this file type
        filename_extensions = ['.svg']
        ext = os.path.splitext(iname)[1].lower()
        return ext in filename_extensions
    
class FilerSvgField(FilerFileField):
    default_model_class = Svg
    
class SvgPluginEditor(CMSPlugin):
    svg = FilerSvgField()
