[![travis\_build\_status](https://travis-ci.org/rlaboiss/pelican-linkclass.svg?branch=master)](https://travis-ci.org/rlaboiss/pelican-linkclass)

# Link Class for Pelican

## Description

This plugin allows the setting of the class attribute of `<a>` elements
(generated in Markdown by `[ext](link)`) according to whether the link is
external (i.e. starts with `http://` or `https://`) or internal to the
Pelican-generated site.

For now, this plugin only works with Markdown.  It was tested with version
3.0.1 of the Python Markdown module.  It may not work with previous
versions.

## Installation

This plugin [is available as a package](https://pypi.org/project/pelican-linkclass/)
at PyPI:

```
pip3 install pelican_linkclass
```

## Usage

### Declaring the plugin

This plugin used to be part of the [Pelican plugin
repository](https://github.com/getpelican/pelican-plugins), but users
should now install the plugin in their system (as above) and add to
`pelicanconf.py` a configuration like the following:

```python
import pelican_linkclass
PLUGINS = [pelican_linkclass,]
```

### User Settings

In order to avoid clashes with already-defined classes in the user CSS
style sheets, it is possible to specify the name of the classes that will
be used.  They can be specified in the Pelican setting files with the
`LINKCLASS` variable, which must be defined as a list of tuples, like this:

```python
'LINKCLASS' = (('EXTERNAL_CLASS', 'name-of-the-class-for-external-links')
                'INTERNAL_CLASS', 'name-of-the-class-for-internal-links'))
```

The default values for `EXTERNAL_CLASS` and `INTERNAL_CLASS` are,
respectively, `'external'` and `'internal'`.

### Styling the hyperlinks

One of the possible uses of this plugins is for styling.  Suppose that we
have the following in your article written with Markdown:

```markdown
This is an [internal](internal) link and this is an
[external](http://external.com) link.
```

If the default values of the configuration variables are used, then a
 possible CSS setting would be:

```css
a.external:before {
    content: url('../images/external-link.png');
    margin-right: 0.2em;
}
```

(The file `external-link.png` is also distributed with this plugin.  Just
copy it to the appropriate place in your website source tree, for instance
in `theme/static/images/`.)

Then, the result will look like the following:

![figure](https://github.com/rlaboiss/pelican-linkclass/raw/master/linkclass-example.png)

Note that this plugin also works with reference-style links, as in the
following example:

```markdown
This is an [internal][internal] link and this is an
[external][external] link.

 [internal]: internal
 [external]: http://external.com
```

## Acknowledgments

Many thanks to [Yuliya Bagriy](https://github.com/aviskase) for setting up
the package for [PyPI](https://pypi.org/) and [Lucas
Cimon](https://github.com/Lucas-C) for fixing the issues with
[pytest](https://pytest.org/) and the smooth integration into the Pelican
repository as a sub-module.

## Author

Copyright (C) 2015, 2017, 2019  Rafael Laboissiere (<rafael@laboissiere.net>)

Released under the GNU Affero Public License, version 3 or later.  No warranties.
