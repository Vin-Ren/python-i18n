from .config import get
from .translations import container as translations_container
from .translator import t


class TranslatorGroup:
    TRANSLATION_FORMAT='{namespace}.{key}' # possible keys = namespace, locale, key
    
    def __init__(self, namespace='', locale=None):
        self.namespace=namespace
        self.locale=locale if locale is not None else get('locale')
        self.data={'namespace':self.namespace, 'locale':self.locale}
    
    def __repr__(self):
        return "<{cls} object namespace='{namespace}' locale='{locale}'>".format(cls=self.__class__.__name__, **self.data)
    
    def __call__(self, key, *args, **kwds):
        [kwds.__setitem__(k,v) for k,v in self.data.items() if k not in kwds]
        return t(self.TRANSLATION_FORMAT.format(**self.data, key=key).lstrip('.'), *args, **kwds)
    
    def __getitem__(self, key):
        return t(self.TRANSLATION_FORMAT.format(**self.data, key=key).lstrip('.'), **self.data)
    
    def reset(self, all_locale=False):
        """Resets all of the accessible translations of this TranslatorGroup."""
        accessible_prefix=self.TRANSLATION_FORMAT.format(**self.data, key='').lstrip('.')
        
        for locale in translations_container:
            if (locale==self.locale) or all_locale:
                for key in list(translations_container[locale]):
                    if key.startswith(accessible_prefix):
                        translations_container[locale].pop(key)
