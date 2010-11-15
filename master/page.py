#!/usr/bin/env python
from django.http import HttpResponseRedirect
from utils.page import DefaultPage
from utils.page import Page

from django.contrib.auth.models import User

from master import box as B

class LandingPage(Page):
    url = 'master_landing_page',
    template = 'master/PageLanding.html'
    
    def __init__(self):
        self.header = B.HeaderBox
        self.boxes = [B.SideBox, B.SearchBox, B.QListBox]
        super(LandingPage, self).__init__(login_required=False)
    
    def view(self, request, *args, **kwargs):
        return super(LandingPage, self).show(request, *args, **kwargs)
        
class CreateQuotePage(Page):
    url = 'master_cq_page'
    template = 'master/PageLanding.html'
    
    def __init__(self):
        self.header = B.HeaderBox
        self.boxes = [B.SideBox, B.SearchBox, B.CreateQuoteBox]
        super(CreateQuotePage, self).__init__(login_required=False)
        
    def view(self, request, *args, **kwargs):
        return super(CreateQuotePage, self).show(request, *args, **kwargs)
        
class QuotePage(Page):
    url = 'master_quote_page'
    template = 'master/PageLanding.html'
    
    def __init__(self):
        self.header = B.HeaderBox
        self.boxes = [B.SideBox, B.SearchBox, B.QuoteBox]
        super(QuotePage, self).__init__(login_required=False)
        
    def view(self, request, *args, **kwargs):
        return super(QuotePage, self).show(request, *args, **kwargs)
        
class SearchPage(Page):
    url='master_search_page'
    template = 'master/PageLanding.html'
    
    def __init__(self):
        self.header = B.HeaderBox
        self.boxes = [B.SideBox, B.SearchBox, B.SearchResultBox,]
        super(SearchPage, self).__init__(login_required=False)
        
    def view(self, request, *args, **kwargs):
        return super(SearchPage, self).show(request, *args, **kwargs)