Disable the Plone feature on indexing files contents when you are developing

Use case
========

You are developing in a Plone environment with a production Data.fs (and blobs) that contains *a lot* of
File contents and then you need to perform some actions like "Update catalog" or "Clean and Rebuild".

It will be really slow, but probably the indexed files are not the reason why you are performing the action.

How it works
============

This products is an hack that will monkey-patch the default Plone ATFile (with or without ATBlob support)
disabling the ``searchable`` settings.

This is automatically enabled in development mode while it's disabled in production mode.

You can force the indexing to stop adding the ``DISABLE_FILE_INDEXING`` environment var::

    [instance]
    ...
    
    environment-vars =
        DISABLE_FILE_INDEXING True

In the same way you can keep the indexing active while in development mode::

    [instance]
    ...
    
    environment-vars =
        DISABLE_FILE_INDEXING False

.. warning::
    Keep an eye open to this product if it will be pushed to a production environment. While it will disabled in
    production mode, it will be enabled if you run a debug/emergency instance.

TODO
====

Plone 5/plone.app.contenttypes support

Authors
=======

This product was developed by RedTurtle Technology team.

.. image:: http://www.redturtle.it/redturtle_banner.png
   :alt: RedTurtle Technology Site
   :target: http://www.redturtle.it/
