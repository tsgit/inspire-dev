# -*- coding: utf-8 -*-
##
## $Id$
##
## This file is part of CDS Invenio.
## Copyright (C) 2002, 2003, 2004, 2005, 2006, 2007 CERN.
##
## CDS Invenio is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 2 of the
## License, or (at your option) any later version.
##
## CDS Invenio is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
## General Public License for more details.  
##
## You should have received a copy of the GNU General Public License
## along with CDS Invenio; if not, write to the Free Software Foundation, Inc.,
## 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.
"""BibFormat element test - Prints a custom field
"""


import re
import unittest
from invenio.bibformat_engine import BibFormatObject
class filterTestclass(unittest.TestCase):        #
        # Test case depends on inspires test records

      


        #test CERN_authors
        def testField(self):
            self.bfo=BibFormatObject('73740')
            self.assertEqual(self.bfo.field('100a'),"Dimitrijevic, M.")
        def testAff(self):
            from bfe_CERN_authors import format
            self.bfo=BibFormatObject('73740')
            string =  format(self.bfo,limit="5",print_affiliations="yes")
            self.assert_(re.search(r'Dimitrijevic, M.</a>;',string))
            self.assert_(re.search(r'Moller, L.</a> \(<a.*Zagreb',string))

        #test INSPIRE_arXiv
        def testarX(self):
            from bfe_INSPIRE_arxiv import format
            self.bfo=BibFormatObject('82146')
            print format(self.bfo)
            
            
unittest.main()



