# -*- coding: utf-8 -*-
from five import grok
from zope import schema
from plone.directives import form

from zope.interface import Invalid

from plone.namedfile.interfaces import IImageScaleTraversable
from plone.namedfile.field import NamedBlobImage

from plone.app.textfield import RichText

from pythonchile.content import PythonChileMessageFactory as _

# Indexer
from plone.indexer import indexer

# Uniqueness validator
from z3c.form import validator
from plone.uuid.interfaces import IUUID
from Products.CMFCore.utils import getToolByName

from zope.schema import ValidationError

from Products.CMFDefault.utils import checkEmailAddress
from Products.CMFDefault.exceptions import EmailAddressInvalid

def validateaddress(value):
    try:
        checkEmailAddress(value)
    except EmailAddressInvalid:
        raise InvalidEmailAddress(value)
    return True

class InvalidEmailAddress(ValidationError):
    "Invalid email address"

class IJob(form.Schema, IImageScaleTraversable):
    """Describes a job posting
    
    We mix in IImageScaleTraversable so that we can use the @@images view
    to look up scaled versions of the 'image' field.
    """

    title = schema.ASCIILine(
            title=_(u"Posición"),
        )

    position = RichText(
            title=_(u"Descripción"),
    )
    
    how_to_apply = schema.Text(
            title=_(u"Cómo Aplicar"),
            required=False
    )    

    location = schema.ASCIILine(
            title=_(u"Lugar"),
        )

    company_name = schema.ASCIILine(
            title=_(u"Empresa"),
    )


    company_logo = NamedBlobImage(
            title=_(u"Logo Empresa"),
            required=False
     )

    company_website = schema.URI(
            title=_(u"URL Empresa"),
            required=False
    )

    email = schema.ASCIILine(
            title=_(u"Email"),
            constraint=validateaddress,
    )
    
    
@indexer(IJob)
def SearchableText(obj):
    return ' '.join([obj.title, obj.position.output])    

class View(grok.View):
    """Default view (called "@@view"") for a job.
    
    The associated template is found in job_templates/view.pt.
    """

    grok.context(IJob)
    grok.require('zope2.View')
    grok.name('view')

    def update(self):
        """Prepare information for the template
        """        