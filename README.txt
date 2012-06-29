redomino.tokenroleform
======================

This product allows unregistered users to download or view a private content by simply filling 
a contact form with personal data and a valid e-mail address; after submitting the form, an automated mail 
containing the link to the requested private content is sent to the user who made the request.

Basically the request is carried out by PloneFormGen action adapter, which activates a temporary access token
thanks to redomino.tokenrole, and sends it via mail. The token's validity only lasts for a few minutes, 
which means it has to be used quickly. This was done in order to avoid unauthorized sharing on social networks 
or other platforms.


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


    <a tal:define="token_url python:request.get('TOKEN_URL');" 
       tal:attributes="href token_url;"
       tal:content="token_url">ACCESS LINK</a>


Tokenrole form screenshot:

.. figure:: https://github.com/redomino/redomino.tokenroleform/blob/master/docs/resources/tokenroleformconf.png 
   :align: center

   Token role form configuration


Authors
=======

* Davide Moro <davide.moro@redomino.com> - Idea and main implementation


