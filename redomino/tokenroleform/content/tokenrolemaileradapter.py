"""Definition of the TokenRoleMailerAdapter content type
"""

from zope.interface import implements

from archetypes.referencebrowserwidget.widget import ReferenceBrowserWidget

from Products.Archetypes import atapi
from Products.ATContentTypes.content import schemata

from Products.PloneFormGen.content.formMailerAdapter import FormMailerAdapter
from Products.PloneFormGen.content.formMailerAdapter import formMailerAdapterSchema

# -*- Message Factory Imported Here -*-
from redomino.tokenroleform import tokenroleformMessageFactory as _

from redomino.tokenroleform.interfaces import ITokenRoleMailerAdapter
from redomino.tokenroleform.config import PROJECTNAME

TokenRoleMailerAdapterSchema = formMailerAdapterSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    atapi.ReferenceField(
        'private_doc',
        storage=atapi.AnnotationStorage(),
        widget=ReferenceBrowserWidget(
            label=_(u"Private doc"),
            description=_(u"Choose the private item you are going to share"),
        ),
        required=True,
        relationship='tokenrolemaileradapter_private_doc',
        allowed_types=(), # specify portal type names here ('Example Type',)
        multiValued=False,
    ),


    atapi.IntegerField(
        'minutes',
        storage=atapi.AnnotationStorage(),
        widget=atapi.IntegerWidget(
            label=_(u"Validity (minutes)"),
            description=_(u"Type the token validity in minutes"),
        ),
        required=True,
        default=_(u"3600"),
        validators=('isInt'),
    ),


))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

TokenRoleMailerAdapterSchema['title'].storage = atapi.AnnotationStorage()
TokenRoleMailerAdapterSchema['description'].storage = atapi.AnnotationStorage()
TokenRoleMailerAdapterSchema['recipient_name'].widget.visible = {'edit':'invisible','view':'invisible'}
TokenRoleMailerAdapterSchema['recipient_email'].widget.visible = {'edit':'invisible','view':'invisible'}

schemata.finalizeATCTSchema(TokenRoleMailerAdapterSchema, moveDiscussion=False)

TokenRoleMailerAdapterSchema.changeSchemataForField('to_field', 'default')


class TokenRoleMailerAdapter(FormMailerAdapter):
    """Token role mailer adapter"""
    implements(ITokenRoleMailerAdapter)

    meta_type = "TokenRoleMailerAdapter"
    schema = TokenRoleMailerAdapterSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    private_doc = atapi.ATReferenceFieldProperty('private_doc')

    minutes = atapi.ATFieldProperty('minutes')


atapi.registerType(TokenRoleMailerAdapter, PROJECTNAME)
