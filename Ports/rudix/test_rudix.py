import unittest
from rudix import *

class RudixTest(unittest.TestCase):
    def test_version_compare(self):
        self.assertEqual( version_compare('1.0', '2.0'), -1)
        self.assertEqual( version_compare('1.0', '1.0.1'), -1)
        self.assertEqual( version_compare('1.0.2', '1.0.10'), -1)
        self.assertEqual( version_compare('1.0.1-2', '1.0.1-10'), -1)
        self.assertEqual(version_compare('1.11-1', '1.11.1-0'), -1)
        self.assertEqual(version_compare('2.1.0b1-0', '2.1.2-0'), -1)
        self.assertEqual(version_compare('2.2.1-10', '3.0-0'), -1)

    def test_communicate(self):
        self.assertEqual(communicate(['echo', 'rudix']), ['rudix'])

    def test_normalization(self):
        self.assertEqual( normalize('rudix'), 'org.rudix.pkg.rudix' )
        self.assertEqual( normalize('org.rudix.pkg.rudix'),
                          'org.rudix.pkg.rudix' )
        self.assertEqual( denormalize('org.rudix.pkg.rudix'), 'rudix' )
        self.assertEqual( denormalize('rudix'), 'rudix' )

if __name__ == '__main__':
    unittest.main()
