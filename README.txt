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

* add a 'TokenRoleMailerAdapter'

    * choose an existing private document you want to share (field "Private doc")

    * validity (minutes), the token validity. Default: 60 minutes

    * Extract Recipient (choose "From Your E-Mail Address")

    * fill the fields of the Message tab

Authors
=======

* Davide Moro <davide.moro@redomino.com> - Idea and main implementation


