import unittest


# Uses the discover method on the current directory ('')
def suite():
    suite = unittest.TestSuite()
    #tests = unittest.TestLoader().discover('')
    tests = unittest.TestLoader().discover('.', pattern="test_*.py")
    suite.addTests(tests)
    unittest.TextTestRunner(verbosity=2).run(suite)


suite()
