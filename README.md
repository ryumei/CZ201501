CZ201501
========

Regist an issue to a redmine by Python.

## Description

Web 記事の連載でご紹介する予定内容のサンプルコードです。

## Demo

Just do it.

    $ python issue_reporter.py \
	  -u endpoint_url -k API_KEY \
      -p project_id -s "subject" -d "description"
  

## Requirement

* Python 2.x (or 3.x)
* [python-remine](http://python-redmine.readthedocs.org/)

Tested on Python 2.7.6 on Windows

## Usage

    $ python issue_reporter.py \
	  -u endpoint_url -k API_KEY \
      -p project_id -s "subject" -d "description"


## Install

1. Fork or download source code.

2. Get required libraries

    $ easy_install python-redmine Jinja2

3. Rename and edit configuration file ``conf.json``

    $ mv sample.conf.json conf.json

## Contribution

## Licence

[MIT](https://github.com/tcnksm/tool/blob/master/LICENCE)

## Author

[NAKAJIMA Takaaki](https://github.com/ryumei)
