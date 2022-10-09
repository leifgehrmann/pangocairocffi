# How to contribute

Thanks for reading!

You can help by:

* Reporting any issues and requesting enhancements,
* Updating documentation, or...
* Modifying code and submitting a pull request.

## Reporting issues and requesting enhancements

Issues and enhancements can be reported on [pangocairocffi issues on GitHub].

[pangocairocffi issues on GitHub]: https://github.com/leifgehrmann/pangocairocffi/issues/new

## Modifying code

You'll first need to setup a development environment. Hopefully you will
already have modern version of python and pip installed. Naturally for the
package to work you will also need to have the Pango library and it's relevant
dependencies installed.

After checking out this repository, install the dev dependencies:

```bash
$ pip install -r requirements.txt
```

Then run the `setup.py install` command so the package can be tested and so
documentation can be auto-generated. 

```bash
$ make install
```

### Testing code changes

A quick test can be done by running:

```bash
$ make test
```

To check code coverage, run:

```bash
$ make coverage
```

For completeness, it's recommended to run tests for *all* python
interpreters using [tox]:

```bash
$ make test-all
```

**Note:** The tests are also run via GitHub actions, so don't worry too much if you
are unable to setup tox with the correct python environments.

[tox]: https://tox.wiki

### Formatting

This repository uses [flake8] to enforce various linting rules. To check your
code complies, run:

```bash
$ make lint
```

[flake8]: https://gitlab.com/pycqa/flake8

### Modifying documentation

Any changes to the documentation can be generated and viewed by running:

```bash
$ make docs
```

## Making a new release

This project uses SemVer for managing version numbers. The version number in
the file `pangocairocffi/VERSION` should be updated, and committed before a new
release.

After this change has been merged into master, a new release on GitHub should
be made. Changes in the release should be added to the Releases section on
GitHub.

Finally, with the tagged version checked out on a machine, run the following:

```bash
$ make release
```

This command will prompt for username and password of the PyPi account. Making
a release requires credentials of the project owner. If you would like to be
co-owner of the project, do not hesitate to ask!
