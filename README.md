django_filer_svg
================

A plugin for django-filer and django-cms to enable the easy addition of
SVG images to a blog/cms article.

Installation:
===========
Install from git hub by cloning or:

	$ pip install -e git+https://github.com/agcooke/django-filer-svg#egg=cmsplugin_filer_svg
	
Then add it to your settings. to your settings file:
	INSTALLED_APPS = (
					...
	               'cmsplugin_filer_svg',
				...
				)
Then use south or syncdb to add to your database.

A django cms plugin will then be available to add svg's to your post or article.
Contact:
======
adriangerardcooke at your favourite google online mailing system.com

License
=========
BSD version 3.