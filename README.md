Link Class: A Plugin for Pelican
================================

[![Build Status](https://img.shields.io/github/actions/workflow/status/pelican-plugins/linkclass/main.yml?branch=main)](https://github.com/pelican-plugins/linkclass/actions)
[![PyPI Version](https://img.shields.io/pypi/v/pelican-linkclass)](https://pypi.org/project/pelican-linkclass/)
[![Downloads](https://img.shields.io/pypi/dm/pelican-linkclass)](https://pypi.org/project/pelican-linkclass/)
[![License](https://img.shields.io/pypi/l/pelican-linkclass?color=blue)](https://www.gnu.org/licenses/agpl-3.0.en.html)

This Pelican plugin lets you to set the class attribute of `<a>` elements (generated in Markdown by `[ext](link)`), depending on whether the link is external (i.e., starts with `http://` or `https://`) or internal to the Pelican-generated site.

Currently, this plugin only works with Markdown. It has been tested with version 3.0+ of the Python-Markdown module and may not work with earlier versions.


Installation
------------

This plugin [is available as a package](https://pypi.org/project/pelican-linkclass/) at PyPI and can be installed via:

```
python -m pip install pelican-linkclass
```

As long as there is no `PLUGINS` setting in the Pelican settings file, the newly installed plugin should be detected and enabled automatically. Otherwise, you must add `linkclass` to your existing `PLUGINS` list. For more information, please refer to the [How to Use Plugins](https://docs.getpelican.com/en/latest/plugins.html#how-to-use-plugins) documentation.


Configuration
-------------

To avoid clashing with classes already defined in user CSS style sheets, it is possible to specify the names of the classes that will be used. This can be done in the Pelican settings file by defining the `LINKCLASS` variable as a list of tuples, such as in this example:

```python
'LINKCLASS' = (('EXTERNAL_CLASS', 'name-of-the-class-for-external-links'),
               ('INTERNAL_CLASS', 'name-of-the-class-for-internal-links'))
```

The default values for `EXTERNAL_CLASS` and `INTERNAL_CLASS` are, respectively, `'external'` and `'internal'`.


Styling Hyperlinks
------------------

One possible use of this plugin is for styling. Suppose that we have the following Markdown content in your article:

```markdown
This is an [internal](internal) link and this is an
[external](http://external.com) link.
```

Using the default configuration variable values, a possible CSS setting could be:

```css
a.external:before {
    content: url('../images/external-link.png');
    margin-right: 0.2em;
}
```

(The `external-link.png` file is also distributed with this plugin. To use it, copy it to the appropriate location in your website's source tree, for instance in the `theme/static/images/` directory.)

The result will then look like this:

![figure](https://github.com/pelican-plugins/linkclass/raw/main/linkclass-example.png)

Note that this plugin also works with reference-style links, as in the following example:

```markdown
This is an [internal][internal] link and this is an
[external][external] link.

 [internal]: internal
 [external]: http://external.com
```


Contributing
------------

Contributions are welcome and much appreciated. Every little bit helps. You can contribute by improving the documentation, adding missing features, and fixing bugs. You can also help out by reviewing and commenting on [existing issues][].

To start contributing to this plugin, review the [Contributing to Pelican][] documentation, beginning with the **Contributing Code** section.

[existing issues]: https://github.com/pelican-plugins/linkclass/issues
[Contributing to Pelican]: https://docs.getpelican.com/en/latest/contribute.html


Acknowledgments
---------------

Many thanks to [Yuliya Bagriy][] for setting up the package for [PyPI][], to [Lucas Cimon][] for fixing the issues with [pytest][], and to [Justin Mayer][] for helping with migration of this plugin under the Pelican Plugins organization.

[Yuliya Bagriy]: https://github.com/aviskase
[PyPI]: https://pypi.org/
[Lucas Cimon]: https://github.com/Lucas-C
[pytest]: https://pytest.org/
[Justin Mayer]: https://github.com/justinmayer


Author
------

Copyright © 2015, 2017, 2019, 2021-2023, 2025 Rafael Laboissière (<rafael@laboissiere.net>)


License
-------

This project is released under the terms of the GNU Affero Public License, version 3 or later.
