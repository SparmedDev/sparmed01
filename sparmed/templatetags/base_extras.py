from django import template
from django.core.urlresolvers import reverse
from django.conf import settings
from django.core.urlresolvers import resolve
from django.utils import translation

from classytags.helpers import InclusionTag
from django.template.loader import render_to_string
from django.template import TemplateSyntaxError, Variable, Node, Variable, Library

register = template.Library()

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
  
# I found some tricks in URLNode and url from defaulttags.py:
# https://code.djangoproject.com/browser/django/trunk/django/template/defaulttags.py
@register.tag
def settings_value(parser, token):
  bits = token.split_contents()
  if len(bits) < 2:
    raise TemplateSyntaxError("'%s' takes at least one " \
      "argument (settings constant to retrieve)" % bits[0])
  settingsvar = bits[1]
  settingsvar = settingsvar[1:-1] if settingsvar[0] == '"' else settingsvar
  asvar = None
  bits = bits[2:]
  if len(bits) >= 2 and bits[-2] == 'as':
    asvar = bits[-1]
    bits = bits[:-2]
  if len(bits):
    raise TemplateSyntaxError("'value_from_settings' didn't recognise " \
      "the arguments '%s'" % ", ".join(bits))
  return ValueFromSettings(settingsvar, asvar)

class ValueFromSettings(Node):
  def __init__(self, settingsvar, asvar):
    self.arg = Variable(settingsvar)
    self.asvar = asvar
  def render(self, context):
    ret_val = getattr(settings,str(self.arg))
    if self.asvar:
      context[self.asvar] = ret_val
      return ''
    else:
      return ret_val      
