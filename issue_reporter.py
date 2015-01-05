#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  issue_reporter.py
#  Created by NAKAJIMA Takaaki on Jan. 5, 2015.
#
import sys
from redmine import Redmine
from optparse import OptionParser

parser = OptionParser()
parser.add_option('-u', '--url', dest='url', help='Endpoint url of a redmine')
parser.add_option('-k', '--key', dest='key', help='API Access  Key')
parser.add_option('-s', '--subject', dest='subject', help='Subject of a reporting issue')
parser.add_option('-p', '--project_id', dest='project_id', help='Project ID of the issue')
parser.add_option('-d', '--description', dest='description', help='Description of the issue')
(options, args) = parser.parse_args()

redmine = Redmine(options.url, key=options.key)
issue = redmine.issue.create(project_id=options.project_id, 
                             subject=options.subject)
if options.description is None:
    issue.description = u"This ticket was created by issue_reporter.py"
else:
    issue.description = options.description
issue.notes = u"""
このチケットは自動登録されました。
確認、対応をお願いします。
"""

issue.save()

