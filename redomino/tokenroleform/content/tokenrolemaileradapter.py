"""Definition of the TokenRoleMailerAdapter content type
"""

from zope.interface import implements

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
        widget=atapi.ReferenceWidget(
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

schemata.finalizeATCTSchema(TokenRoleMailerAdapterSchema, moveDiscussion=False)


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
