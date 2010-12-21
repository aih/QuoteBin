from django.utils.datastructures import SortedDict
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
import json
from utils.json_utils import JsonResponse
from django.conf import settings
import ast
import urllib2
from utils.tab import Tab
from master import element as E
from master import models as M
from utils.nodes import Node
from utils.callback import Callback
cb = Callback()

class HeaderTab(Tab):
    _element_class = E.HeaderElement
    title = ''

class SideTab(Tab):
    _element_class = E.SideElement
    title = ''
    
    def _prepare(self):
        if self.user.is_anonymous():
            self.ids = ['All', 'My Quotes']
        else:
            self.ids = ['All', 'My Quotes'] + list(M.QuoteBin.objects.filter(user=self.user))
        self.context['data_id'] = self.login_user.key
        self.context['user'] = self.user.is_authenticated()
        self.context['project'] = self.project.key

    @staticmethod
    @cb.register
    def project(request):
        name = request.GET.get('name').strip()
        obj, created = M.QuoteBin.objects.get_or_create(user=request.user, name=name)
        if not created:
            return JsonResponse(json.dumps({'success': False}))
        return JsonResponse(json.dumps({
            'success': True,
            'html': SideTab(request.user, True, None).show()['html']
        }))

    @staticmethod
    @cb.register
    def login_user(request):
        code = request.GET.get('code').strip()
        print code
        try:
            email = M.EmailCode.objects.get(code=code).email
            print email
            user = User.objects.get(username=email)
            print user
            user.backend='django.contrib.auth.backends.ModelBackend'
            login(request, user)
            success = True
        except Exception, e:
            print e
            success = False
        return JsonResponse(json.dumps({'success':success}))
        
class QuickQuoteTab(Tab):
    _element_class = E.QuickQuoteElement
    title = ''

class QListTab(Tab):
    _element_class = E.QListElement
    title = ''
    
    def _prepare(self):
        if self.client is None:
            if self.user.is_authenticated():
                self.ids = M.Quote.objects.filter(user = self.user).order_by('-update_date')
            else:
                self.ids = M.Quote.objects.filter(is_public=True).order_by('-update_date')
        else:
            code = self.client
            if code == 'All':
                self.ids = M.Quote.objects.filter(is_public=True).order_by('-update_date')[:10]
            elif code == 'MyQuotes':
                self.ids = M.Quote.objects.filter(user = self.user).order_by('-update_date')[:10]
            else:
                bin = M.QuoteBin.objects.get(id=int(self.client))
                self.ids = bin.quote.all().order_by('-update_date')[:10]
                code = bin.name
                self.context['delete'] = "%s+%d" % (self.delete.key, bin.id)
            self.context['display_title'] = code
            
    @staticmethod
    @cb.register
    def delete(request):
        id = request.GET.get('data_id').split('+')[1]
        bin = M.QuoteBin.objects.get(id=int(id))
        bin.delete()
        return HttpResponse('ok')

class CreateQuoteTab(Tab):
    _element_class = E.CreateQuoteElement
    title = ''

class QuoteTab(Tab):
    _element_class = E.QuoteElement
    title = ''

class SearchResultTab(Tab):
    _element_class = E.QListElement
    title=''
    
    def _prepare(self):
        #query_dict = {'query':self.client or '*'}
        #query_url = '_val_:"scale(log(sum(votes,1)),0,10)"^10 name:(%(query)s)^5 name:"%(query)s"^5 alternative_name:(%(query)s)^3 alternative_name:"%(query)s"^3 original_name:(%(query)s)^3 original_name:"%(query)s"^3' % query_dict
        #query_url = urllib2.quote(query_url)
        #static_url = settings.SOLR_URL + 'q=%s&version=2.2&wt=python&rows=100&start=0&qt=standard&fl=*,score'
        #conn = urllib2.urlopen(static_url % query_url)
        #rsp = ast.literal_eval(conn.read())    
        #result = [e for e in rsp['response']['docs']]
        
        #self.ids = M.Movie.objects.filter(name__icontains=self.client or '')
        #self.ids = [M.Movie.objects.get(id=e['id']) for e in result]
        self.ids = M.Quote.objects.filter(title__contains=self.client)
        print self.client
        print self.ids
        
    
    def show(self, is_json=False, start=0, count=10):
        #self.context['title'] = Node(self.title, data_id=self.get_data.key)
        r= super(SearchResultTab, self).show(None, is_json, start, count,
                next_key = '%s+%s' % (self.get_next.key, self.client or ''),
                prev_key = '%s+%s' % (self.get_next.key, self.client or ''))
        return r

    @staticmethod
    @cb.register
    def get_next(request):
        data_id = request.GET.get('data_id').split('+')[1:]
        start = int(data_id[1])
        query = data_id[0]
        return HttpResponse(SearchResultTab(request.user, True, query).show(start=start)['html'])
        
class LoginTab(Tab):
    _element_class = E.LoginElement
    title = 'Login'

class SignUpTab(Tab):
    _element_class = E.SignUpElement
    title = ''

class SearchTab(Tab):
    _element_class = E.SearchElement
    title=''
