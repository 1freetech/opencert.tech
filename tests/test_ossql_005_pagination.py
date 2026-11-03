"""Regression tests for OSSQL.005's published pagination training data.

Run: python -m unittest tests/test_ossql_005_pagination.py
Requires: Python standard library sqlite3, no network or database service.
Dataset is fictional, not vendor-provided miner specifications.
"""
import sqlite3
import unittest


CREATE_DATASET = """
CREATE TABLE miners (
    miner_id INTEGER PRIMARY KEY,
    model TEXT NOT NULL,
    hashrate_th INTEGER NOT NULL
);
INSERT INTO miners (miner_id, model, hashrate_th) VALUES
(101, 'Training A', 140),
(102, 'Training B', 188),
(103, 'Training C', 220),
(104, 'Training D', 100),
(105, 'Training E', 188),
(106, 'Training F', 270),
(107, 'Training G', 140),
(108, 'Training H', 335);
"""

PAGINATED_QUERY = """
SELECT miner_id, model, hashrate_th
FROM miners
ORDER BY hashrate_th DESC, miner_id ASC
LIMIT ? OFFSET ?;
"""


class SQLPaginationLessonTests(unittest.TestCase):
    def setUp(self):
        self.connection = sqlite3.connect(":memory:")
        self.connection.executescript(CREATE_DATASET)

    def tearDown(self):
        self.connection.close()

    def page(self, page_number, size=3):
        assert page_number >= 1
        assert size >= 1
        return [row[0] for row in self.connection.execute(
            PAGINATED_QUERY, (size, (page_number - 1) * size)
        ).fetchall()]

    def test_first_page(self):
        self.assertEqual(self.page(1), [108, 106, 103])

    def test_second_page_preserves_unique_tie_order(self):
        self.assertEqual(self.page(2), [102, 105, 101])

    def test_partial_last_page(self):
        self.assertEqual(self.page(3), [107, 104])

    def test_beyond_final_page_is_empty(self):
        self.assertEqual(self.page(4), [])

    def test_page_size_and_no_duplication(self):
        pages = [self.page(i) for i in (1, 2, 3)]
        flattened = [miner for page in pages for miner in page]
        self.assertEqual(len(flattened), 8)
        self.assertEqual(len(set(flattened)), 8)
        self.assertEqual(len(self.page(1, size=5)), 5)


if __name__ == "__main__":
    unittest.main()
