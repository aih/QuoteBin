from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.core.validators import email_re #changed from django.forms.fields to use django 1.2
from django.http import HttpResponse
from django.conf import settings
from django.db.models import Avg, Max, Min, Count
from utils.json_utils import JsonResponse
from master import models as M
from master import data_methods as dm
import json
import xmlrpclib
import time
import ast
import urllib2, urllib
from utils.element import Element
from utils.callback import Callback
cb = Callback()

def send_mail(to, sender, subject, body):
    url = 'https://api.elasticemail.com/mailer/send'
    POST = {
        'username': 'spicavigo@gmail.com',
        'api_key': '362a1404-1619-47df-aceb-8477d041ea5f',
        'from': 'yousuffauzan@gmail.com',
        'from_name': sender or 'QuotesBin',
        'to' : ';'.join(to),
        'subject': subject,
        'body_text': body
    }
    print urllib2.urlopen(url, urllib.urlencode(POST)).read()
    
@cb.register
def share(request):
    id = request.GET.get('data_id').split('+')[1]
    quote = M.Quote.objects.get(id=int(id))
    to = request.GET.get('to').split(',')
    subject = request.GET.get('subject') or 'Quote:' + quote.title
    body = request.GET.get('body') or 'http://localhost:8000/quote/' + str(id) 
    sender = request.GET.get('from')
    send_mail(to, sender, subject, body)
    return JsonResponse(json.dumps('ok'))
    
class HeaderElement(Element):
    def _prepare(self):
        self.context = {'user': self.user.is_authenticated()}

class SideElement(Element):
    def _prepare(self):
        key=self.client
        code = key
        if isinstance(self.client, M.QuoteBin):
            key = self.client.name
            code = self.client.id
        self.context = {'name': key, 'data_id': self.get_quotes.key, 'code': code}

    @staticmethod
    @cb.register
    def get_quotes(request):
        print request.GET
        code = request.GET.get('code')
        if code == 'All':
            ids = M.Quote.objects.filter(is_public=True).order_by('-update_date')[:10]
        elif code == 'MyQuotes':
            ids = M.Quote.objects.filter(user = request.user).order_by('-update_date')[:10]
        else:
            ids = M.QuoteBin.objects.get(id=int(code)).quotes.all().order_by('-update_date')[:10]
        
        from master.tab import QListTab
        print ids
        tab = QListTab(request.user, True, ids)
        return HttpResponse(tab.show()['html'])
        
class QuickQuoteElement(Element):
    def _prepare(self):
        self.context = {}

class QListElement(Element):
    def _prepare(self):
        self.context = {'title': self.client.title,
                        'text': self.client.text,
                        'author': self.client.author,
                        'id': self.client.link,
                        'tags': self.client.tag_set.all(),
                        'created_date': self.client.created_date,
                        'share': '%s+%d' % (share.key, self.client.id,),
                        'user': self.user.is_authenticated(),
                        'is_owner': self.user == self.client.user,
                        'delete': "%s+%d" % (self.delete.key, self.client.id),
                        'link': self.client.link}
    
    @staticmethod
    @cb.register
    def delete(request):
        id = request.GET.get('data_id').split('+')[1]
        quote = M.Quote.objects.get(id = int(id))
        quote.delete()
        return HttpResponse('ok')

class CreateQuoteElement(Element):
    def _prepare(self):
        self.context = {'data_id': self.submit.key, 'types': M.DOC_CHOICES, 'user': self.user.is_authenticated()}
    
    @staticmethod
    @cb.register
    def submit(request):
        text = request.GET.get('text')
        title = request.GET.get('title') or text[:20] + '...'
        author = request.GET.get('author')
        doc_type = request.GET.get('doctype')
        tags = request.GET.get('tag').split(',')
        email = request.GET.get('email')
        code = request.GET.get('code')
        references = request.GET.getlist('reference')
        is_public = request.GET.get('is_public') == 'on'
        em = None
        user = None
        if email:
            em, created = M.EmailCode.objects.get_or_create(email=email, defaults={'code': email})
            em = em.code
            if not created and (code and code != em):
                return JsonResponse(json.dumps({
                    'success': False,
                    'reason': 'Email already present. Please provide the right code which was emailed to you'
                }))
            if created:
                user = User.objects.create_user(username=email, email=email, password=em)
            #    send_mail([email], 'yousuffauzan@hotmail.com', 'Your QuotesBin code', em)
        if code:
            try:
                em = M.EmailCode.objects.get(code=code)
                user = User.objects.get(username=em.email)
                user.backend='django.contrib.auth.backends.ModelBackend'
                login(request, user)
            except:
                return JsonResponse(json.dumps({
                    'success': False,
                    'reason': 'Email already present. Please provide the right code which was emailed to you'
                }))
        if not user and request.user.is_authenticated():
            user = request.user
        obj = M.Quote.objects.create(user = user, text=text, author=author, doc_type=doc_type, title = title, is_public = is_public)
        
        for t in tags:
            tg = M.Tag.objects.create(text=t, quote=obj)
        for ref in references:
            r, created = M.Reference.objects.get_or_create(text=ref)
            obj.references.add(r)
        print references
        return JsonResponse(json.dumps({'success': True, 'url': '/quote/' + str(obj.link)}))

class QuoteElement(Element):
    def _prepare(self):
        self.context = {'title': self.client.title,
                        'text': self.client.text,
                        'author': self.client.author,
                        'id': self.client.id,
                        'tags': self.client.tag_set.all(),
                        'created_date': self.client.created_date,
                        'share': '%s+%d' % (share.key, self.client.id,),
                        'data_id': self.add_to_bundle.key,
                        'bundles': M.QuoteBin.objects.filter(user=self.user),
                        'user': self.user.is_authenticated()}
    
    @staticmethod
    @cb.register
    def add_to_bundle(request):
        id = request.GET.get('name')
        quote = request.GET.get('quote')
        qbin = M.QuoteBin.objects.get(id = int(id))
        quote = M.Quote.objects.get(id = int(quote))
        qbin.quote.add(quote)
        qbin.save()
        return HttpResponse('ok')
        
class LoginElement(Element):
    def _prepare(self):
        self.context ={
            'data_id': self.login.key,
            'ts': time.time()
        }
    
    @staticmethod
    @cb.register
    def login(request):
        username = request.GET.get('username')
        password = request.GET.get('password')
        error = ''
        success = True
        user = authenticate(username=username, password=password)
        if not user:
            error = 'Invalid Email or password'
            success = False
        else:
            login(request, user)
        print json.dumps({'success': success, 'url': '/home', 'error': error})
        return JsonResponse(json.dumps({'success': success, 'url': '/home', 'error': error}))

class SignUpElement(Element):
    def _prepare(self):
        self.context = {
            'data_id': self.signup.key
        }
    
    @staticmethod
    @cb.register
    def signup(request):
        username = request.GET.get('username')
        password = request.GET.get('password')
        password2 = request.GET.get('password2')
        success = False
        error = ''
        if email_re.search(username):
            try:
                User.objects.get(username = username)
            except User.DoesNotExist:
                pass
            else:
                error = 'Username Exists'
            if not error:
                if not password == password2:
                    error = 'Passwords do not match'
                elif len(password) < 6:
                    error = 'Minimum length of password is 6'
            if not error:
                user = User.objects.create_user(username = username, email = username, password = password)
                M.UserProfile.objects.create(user=user)
                user.first_name = username.split('@')[0]
                user.save()
                user = authenticate(username=username, password=password)
                login(request, user)
                success = True
        else:
            error = 'Invalid email address'
        return JsonResponse(json.dumps({'success': success, 'url': '/home', 'error': error}))

class SearchElement(Element):
    def _prepare(self):
        self.context = {'q': self.client or '', 'data_id': self.query.key}
    
    @staticmethod
    @cb.register
    def query(request):
        q = request.GET.get('query')
        #query_url = 'e_name:(%s) e_alternative_name:(%s) e_original_name:(%s)' % (q,q,q)
        #query_url = urllib2.quote(query_url)
        #static_url = settings.SOLR_URL + 'q=%s'
        #conn = urllib2.urlopen(static_url % query_url + '&version=2.2&wt=python&rows=10&start=0&qt=standard&fl=name%2Cid&sort=votes+desc')
        #rsp = ast.literal_eval(conn.read())    
        #result = [e for e in rsp['response']['docs']]
        result = M.Quote.objects.filter(title__contains=q)
        ret = {
            'query':q,
            'suggestions': [e.title for e in result],
            'data': [e.link for e in result]
        }
        return JsonResponse(json.dumps(ret))
        
