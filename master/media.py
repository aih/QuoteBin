from utils.media import Media

class HeaderBoxMedia(Media):
    template = 'common/BoxEmpty.html'

class HeaderTabMedia(Media):
    template = 'common/TabEmpty.html'

class HeaderElementMedia(Media):
    template = 'master/ElementHeader.html'
    css = ['master/ElementHeader.css']

LoginBoxMedia = SignUpBoxMedia = HeaderBoxMedia
LoginTabMedia = SignUpTabMedia = HeaderTabMedia

class QuickQuoteBoxMedia(Media):
    template = 'common/BoxEmpty.html'

class QuickQuoteTabMedia(Media):
    template = 'common/TabEmpty.html'

class QuickQuoteElementMedia(Media):
    template = 'master/ElementQuickQuote.html'

class QuoteTabMedia(Media):
    template = 'common/TabDefault.html'

class SideTabMedia(Media):
    template = 'master/TabSide.html'
    js = ['master/TabSide.js']
    css = ['master/TabSide.css']

class SearchResultTabMedia(Media):
    template = 'master/TabSearchResult.html'
    
SearchResultBoxMedia = SideBoxMedia = QListBoxMedia = CreateQuoteBoxMedia = QuoteBoxMedia = QuickQuoteBoxMedia
CreateQuoteTabMedia = QuoteTabMedia

class QListTabMedia(Media):
    template = 'master/TabQList.html'
    js = ['master/TabQList.js']
    

class QListElementMedia(Media):
    template = 'master/ElementQList.html'
    js = ['master/ElementQList.js']

class CreateQuoteElementMedia(Media):
    template = 'master/ElementCreateQuote.html'
    js = ['jquery.validate.pack.js']
    css = ['master/ElementCreateQuote.css']

class QuoteElementMedia(Media):
    template = 'master/ElementQuote.html'
    js = ['master/ElementQuote.js']
    
    
class SideElementMedia(Media):
    template='master/ElementSide.html'
    js=['jquery.fancybox-1.3.1.pack.js','jquery.easing-1.3.pack.js','jquery.mousewheel-3.0.2.pack.js', 'master/ElementSide.js']
    css=['jquery.fancybox-1.3.1.css', 'master/ElementSide.css']

class LoginElementMedia(Media):
    template = 'master/ElementLogin.html'
    css = ['master/ElementLogin.css']
    js = ['master/ElementLogin.js']

class SignUpElementMedia(Media):
    template = 'master/ElementSignUp.html'
    css = ['master/ElementSignUp.css']
    js = ['master/ElementSignUp.js']

    
class SearchBoxMedia(Media):
    template = 'common/BoxEmpty.html'

class SearchTabMedia(Media):
    template = 'common/TabEmpty.html'
    
class SearchElementMedia(Media):
    template = 'master/ElementSearch.html'
    js=['jquery.autocomplete-min.js', 'master/ElementSearch.js']
    css=['master/ElementSearch.css', 'autocomplete.css', 'master/ElementButton.css']


    
