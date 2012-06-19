"""Definition of the TokenRoleMailerAdapter content type
"""

import datetime

from AccessControl import ClassSecurityInfo

from zope.interface import implements

from archetypes.referencebrowserwidget.widget import ReferenceBrowserWidget

from Products.Archetypes import atapi
from Products.ATContentTypes.content import schemata

from Products.PloneFormGen.content.formMailerAdapter import FormMailerAdapter
from Products.PloneFormGen.content.formMailerAdapter import formMailerAdapterSchema
from Products.PloneFormGen import dollarReplace

# -*- Message Factory Imported Here -*-
from redomino.tokenrole.utils import make_uuid
from redomino.tokenrole.interfaces import ITokenInfoSchema

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
            startup_directory_method='startupDirectoryMethod',
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
        default=60,
        validators=('isInt'),
    ),


))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

TokenRoleMailerAdapterSchema['title'].storage = atapi.AnnotationStorage()
TokenRoleMailerAdapterSchema['description'].storage = atapi.AnnotationStorage()
TokenRoleMailerAdapterSchema['recipient_name'].widget.visible = {'edit':'invisible','view':'invisible'}
TokenRoleMailerAdapterSchema['recipient_email'].widget.visible = {'edit':'invisible','view':'invisible'}
TokenRoleMailerAdapterSchema['body_pre'].default = '${TOKEN_URL}'
TokenRoleMailerAdapterSchema['body_post'].default = '${TOKEN_URL}'
TokenRoleMailerAdapterSchema['body_footer'].default = '${TOKEN_URL}'

schemata.finalizeATCTSchema(TokenRoleMailerAdapterSchema, moveDiscussion=False)

TokenRoleMailerAdapterSchema.changeSchemataForField('to_field', 'default')


class TokenRoleMailerAdapter(FormMailerAdapter):
    """Token role mailer adapter"""
    implements(ITokenRoleMailerAdapter)

    meta_type = "TokenRoleMailerAdapter"
    content_icon = 'mailaction.gif'
    schema = TokenRoleMailerAdapterSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    security = ClassSecurityInfo()

    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    private_doc = atapi.ATReferenceFieldProperty('private_doc')

    minutes = atapi.ATFieldProperty('minutes')


    security.declarePrivate('onSuccess')
    def onSuccess(self, fields, REQUEST=None):
        """
           e-mails data.
        """

        REQUEST['form.widgets.token_id'] = self.generate_token()
        super(TokenRoleMailerAdapter, self).onSuccess(fields, REQUEST)

    security.declarePrivate('_dreplace')
    def _dreplace(self, s):
        form = getattr(self.REQUEST, 'form', {})
        if form and self.REQUEST.get('form.widgets.token_id'):
            form['TOKEN_URL'] = self.REQUEST.get('form.widgets.token_id')
        return dollarReplace.DollarVarReplacer(form).sub(s)

    def generate_token(self):
        """ Generate a new token """
        minutes = self.getMinutes()
        token_roles = ['Reader']
        private_doc = self.getPrivate_doc()
        if private_doc:
            token_id = make_uuid(private_doc.getId())
            token_end = datetime.datetime.now() + datetime.timedelta(minutes=minutes)
    
            private_doc.REQUEST.set('form.widgets.token_id', token_id)
            ITokenInfoSchema(private_doc).token_id = token_id
            ITokenInfoSchema(private_doc).token_end = token_end
            ITokenInfoSchema(private_doc).token_roles = token_roles
            return "%s?token=%s" % (private_doc.absolute_url(), token_id)


    def startupDirectoryMethod(self):
        return "/".join(self.getPhysicalPath()[:-2])



atapi.registerType(TokenRoleMailerAdapter, PROJECTNAME)
