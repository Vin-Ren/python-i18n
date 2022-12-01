from .config import get
from .translator import t


class TranslatorGroup:
    TRANSLATION_FORMAT='{namespace}.{key}' # possible keys = namespace, locale, key
    
    def __init__(self, namespace, locale=None):
        self.namespace=namespace
        self.locale=locale if locale is not None else get('locale')
        self.data={'namespace':self.namespace, 'locale':self.locale}
    
    def __repr__(self):
        return "<{cls} object namespace='{namespace}' locale='{locale}'>".format(cls=self.__class__.__name__, **self.data)
    
    def __call__(self, key, *args, **kwds):
        [kwds.__setitem__(k,v) for k,v in self.data.items() if k not in kwds]
        return t(self.TRANSLATION_FORMAT.format(**self.data, key=key), *args, **kwds)
    
    def __getitem__(self, key):
        return t(self.TRANSLATION_FORMAT.format(**self.data, key=key), **self.data)
