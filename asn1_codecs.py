# -*- coding: UTF-8 -*-
# Code automatically generated by pycrate_asn1c

from pycrate_asn1rt.utils            import *
from pycrate_asn1rt.err              import *
from pycrate_asn1rt.glob             import make_GLOBAL, GLOBAL
from pycrate_asn1rt.dictobj          import ASN1Dict
from pycrate_asn1rt.refobj           import *
from pycrate_asn1rt.setobj           import *
from pycrate_asn1rt.asnobj_basic     import *
from pycrate_asn1rt.asnobj_str       import *
from pycrate_asn1rt.asnobj_construct import *
from pycrate_asn1rt.asnobj_class     import *
from pycrate_asn1rt.asnobj_ext       import *
from pycrate_asn1rt.init             import init_modules

class TestSchema:

    _name_  = 'TestSchema'
    _oid_   = []
    
    _obj_ = [
        'OctetString',
        ]
    _type_ = [
        'OctetString',
        ]
    _set_ = [
        ]
    _val_ = [
        ]
    _class_ = [
        ]
    _param_ = [
        ]
    
    #-----< OctetString >-----#
    OctetString = OCT_STR(name='OctetString', mode=MODE_TYPE)
    
    _all_ = [
        OctetString,
    ]

init_modules(TestSchema)
