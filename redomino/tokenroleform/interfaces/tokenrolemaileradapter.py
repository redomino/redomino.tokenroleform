from zope.interface import Interface
# -*- Additional Imports Here -*-
from zope import schema

from redomino.tokenroleform import tokenroleformMessageFactory as _



class ITokenRoleMailerAdapter(Interface):
    """Token role mailer adapter"""

    # -*- schema definition goes here -*-
    private_doc = schema.Object(
        title=_(u"Private doc"),
        required=True,
        description=_(u"Choose the private item you are going to share"),
        schema=Interface, # specify the interface(s) of the addable types here
    )
#
    minutes = schema.Int(
        title=_(u"Validity (minutes)"),
        required=True,
        description=_(u"Type the token validity in minutes"),
    )
#
