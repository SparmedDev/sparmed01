from django import template
from django.core.urlresolvers import reverse
from django.conf import settings
from django.core.urlresolvers import resolve
from django.utils import translation

register = template.Library()

from classytags.helpers import InclusionTag
from django.template.loader import render_to_string

class CookielawCustomBanner(InclusionTag):  
    template = 'cookielaw_c/banner.html';
    
    def render_tag(self, context, **kwargs):
        template = self.get_template(context, **kwargs)
        if context['request'].COOKIES.get('cookielaw_accepted', False):
            return ''
        data = self.get_context(context, **kwargs)
        return render_to_string(template, data)

register.tag(CookielawCustomBanner)

@register.simple_tag
def get_flag(language_code):
    if language_code == 'en':
        language_code = 'gb'
    langs = language_code.split('-')
    return 'flags/%s.gif' % langs[-1]


@register.simple_tag
def navactive(request, urls):
    if request.path in ( reverse(url) for url in urls.split() ):
        return " active"

    if urls in request.path_info:
        return " active"

    return ""

@register.simple_tag
def productnavactive(request, name):
    if name in request.path_info:
        return "active"
    
    return ""

@register.simple_tag(takes_context=True)
def change_lang(context, lang=None, *args, **kwargs):
    """
    Get active page's url by a specified language
    Usage: {% change_lang 'en' %}
    """

    path = context['request'].path
    url_parts = resolve( path )

    url = path
    cur_language = translation.get_language()
    try:
        translation.activate(lang)
        url = reverse( url_parts.view_name, kwargs=url_parts.kwargs )
    finally:
        translation.activate(cur_language)

    return "%s" % url  
  
@register.tag
def settings_value(parser, token):
    try:
        # split_contents() knows not to split quoted strings.
        tag_name, var = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError, "%r tag requires a single argument" % token.contents.split()[0]
    return SettingsValue(var)

class SettingsValue(template.Node):
    def __init__(self, var):
        self.arg = template.Variable(var)
    def render(self, context):
        return settings.__getattr__(str(self.arg))
