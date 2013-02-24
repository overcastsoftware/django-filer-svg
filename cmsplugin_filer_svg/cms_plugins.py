'''
Created on 24 Feb 2013

@author: cooke
'''
from cms.plugin_base import CMSPluginBase
from models import SvgPluginEditor
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

class SvgPluginPublisher(CMSPluginBase):
    model = SvgPluginEditor
    name = _("Svg Plugin")
    #render_template = "svg/svg.html"
    text_enabled = True
    admin_preview = False

    def render(self, context, instance, placeholder):
        context.update({
            'svg':instance,
            'placeholder':placeholder,
        })
        return context
plugin_pool.register_plugin(SvgPluginPublisher)
