redomino.tokenroleform
======================

This product adds a PloneFormGen action adapter that let you share contents sending via email 
a private content.

This action adapter activates a temporary access token thanks to redomino.tokenrole and sends it via mail.

Unregistered people will be able to download or see private contents with a temporary link.

How to use tokenroleform
------------------------

Step by step:

* install redomino.tokenroleform

* create a PloneFormGen

* add a 'TokenRoleMailerAdapter' and configure it:

    * choose an existing private document you want to share (field "Private doc")

    * validity (minutes), the token validity. Default: 60 minutes

    * Extract Recipient (choose "From Your E-Mail Address" or another email field)


In the message tab you can configure fields putting a ${TOKEN_URL} in order to add a textual link.
If you prefer an html link go to the Template tab and add this html:

::
<a tal:define="token_url python:request.get('TOKEN_URL');" 
   tal:attributes="href token_url;"
   tal:content="token_url">ACCESS LINK</a>

Authors
=======

* Davide Moro <davide.moro@redomino.com> - Idea and main implementation


