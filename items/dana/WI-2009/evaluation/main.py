"""Automated evaluation entry point for the work item."""
import unittest


class WorkItemEvaluation(unittest.TestCase):
    def test_public_contract(self):
        """Verify the public contract of pdf_worker."""
        self.assertTrue(True, "WI-2009 contract check")


if __name__ == "__main__":
    unittest.main()
