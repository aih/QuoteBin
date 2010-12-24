
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template

from utils.box import Box
from master import tab as T
from master import models as M

from utils.json_utils import JsonResponse
import json
from utils.callback import Callback
cb = Callback()

class HeaderBox(Box):
    _tab_class = [T.HeaderTab]
    title = ''
    def __init__(self, request, * args, ** kwargs):
        self.client = request.path
        super(HeaderBox, self).__init__(request, * args, ** kwargs)

class SideBox(Box):
    _tab_class = [T.SideTab]
    title = ''
    
class QuickQuoteBox(Box):
    _tab_class = [T.QuickQuoteTab]
    title = ''

class SearchBox(Box):
    _tab_class = [T.SearchTab]
    title=''
    
    def __init__(self, request, * args, ** kwargs):
        self.client = request.POST.get('q','').strip()
        super(SearchBox, self).__init__(request, * args, ** kwargs)
        
class QListBox(Box):
    _tab_class = [T.QListTab]
    title = ''
    
    def __init__(self, request, * args, ** kwargs):
        self.client = kwargs.get('code')
        #if code == 'All':
        #    self.client = M.Quote.objects.filter(is_public=True).order_by('-update_date')[:10]
        #elif code == 'MyQuotes':
        #    self.client = M.Quote.objects.filter(user = request.user).order_by('-update_date')[:10]
        #elif code:
        #    self.client = M.QuoteBin.objects.get(id=int(code)).quote.all().order_by('-update_date')[:10]
        #else:
        #    self.client = None
        super(QListBox, self).__init__(request, * args, ** kwargs)

class CreateQuoteBox(Box):
    _tab_class = [T.CreateQuoteTab]
    title = ''

    def __init__(self, request, * args, ** kwargs):
        if request.method == 'POST':
            print 'Saving quote'
            
        super(CreateQuoteBox, self).__init__(request, * args, ** kwargs)
        
class QuoteBox(Box):
    _tab_class = [T.QuoteTab]
    title = ''
    
    def __init__(self, request, * args, ** kwargs):
        self.client = M.Quote.objects.get(link=kwargs.get('quote'))
        super(QuoteBox, self).__init__(request, * args, ** kwargs)

class SearchResultBox(Box):
    _tab_class = [T.SearchResultTab]
    title=''
    
    def __init__(self, request, * args, ** kwargs):
        self.client = request.POST.get('q','').strip()
        self.user = request.user
        super(SearchResultBox, self).__init__(request, * args, ** kwargs)
        
class LoginBox(Box):
    _tab_class = [T.LoginTab]
    title = ''

class SignUpBox(Box):
    _tab_class = [T.SignUpTab]
    title = ''
