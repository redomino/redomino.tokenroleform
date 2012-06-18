"""Definition of the TokenRoleMailerAdapter content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import schemata

from Products.PloneFormGen.content.formMailerAdapter import FormMailerAdapter
from Products.PloneFormGen.content.formMailerAdapter import formMailerAdapterSchema

# -*- Message Factory Imported Here -*-

from redomino.tokenroleform.interfaces import ITokenRoleMailerAdapter
from redomino.tokenroleform.config import PROJECTNAME

TokenRoleMailerAdapterSchema = formMailerAdapterSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

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

atapi.registerType(TokenRoleMailerAdapter, PROJECTNAME)
