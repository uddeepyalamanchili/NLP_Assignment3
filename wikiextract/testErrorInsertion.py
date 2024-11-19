import unittest

# Import the functions from the script
# Assuming the script is named 'error_insertion.py' and functions are accessible
# If the script is in another file, adjust the import accordingly
from insert_errors import insert_errors

class TestInsertErrors(unittest.TestCase):

    def test_adjective_inflection_error(self):
        # Test inflectional errors in adjectives
        # Sentence: वह अच्छी लड़की है।
        # Expected Error: वह अच्छा लड़की है।
        sentence = [
            ('वह', 'PRP', []),
            ('अच्छी', 'JJ', []),
            ('लड़की', 'NN', []),
            ('है', 'VAUX', [])
        ]
        expected_err = 'वह अच्छे लड़की हैं'
        expected_cor = 'वह अच्छी लड़की है'
        err, cor = insert_errors(sentence)
        print('test 1', err, cor)
        print('expected', expected_err, expected_cor)
        self.assertEqual(err, expected_err, 'Test 1 - err passing')
        self.assertEqual(cor, expected_cor)

    def test_verb_inflection_error(self):
        # Test inflectional errors in verbs
        # Sentence: वे स्कूल जाते हैं।
        # Expected Error: वे स्कूल जाता हैं।
        sentence = [
            ('वे', 'PRP', []),
            ('स्कूल', 'NN', []),
            ('जाते', 'VM', []),
            ('हैं', 'VAUX', [])
        ]
        expected_err = 'वे स्कूल जाता हैं'
        expected_cor = 'वे स्कूल जाते हैं'
        err, cor = insert_errors(sentence)
        self.assertEqual(err, expected_err)
        self.assertEqual(cor, expected_cor)

    def test_pronoun_inflection_error(self):
        # Test inflectional errors in pronouns
        # Sentence: उसने अपना काम पूरा किया।
        # Expected Error: उसने अपनी काम पूरा किया।
        sentence = [
            ('उसने', 'PRP', []),
            ('अपना', 'PRP', []),
            ('काम', 'NN', []),
            ('पूरा', 'JJ', []),
            ('किया', 'VM', [])
        ]
        expected_err = 'उसने अपनी काम पूरा किया'
        expected_cor = 'उसने अपना काम पूरा किया'
        err, cor = insert_errors(sentence)
        self.assertEqual(err, expected_err)
        self.assertEqual(cor, expected_cor)

    def test_postposition_inflection_error(self):
        # Test inflectional errors in postpositions
        # Sentence: राम के पास किताब है।
        # Expected Error: राम का पास किताब है।
        sentence = [
            ('राम', 'NNP', []),
            ('के', 'PSP', []),
            ('पास', 'NN', []),
            ('किताब', 'NN', []),
            ('है', 'VAUX', [])
        ]
        expected_err = 'राम का पास किताब है'
        expected_cor = 'राम के पास किताब है'
        err, cor = insert_errors(sentence)
        self.assertEqual(err, expected_err)
        self.assertEqual(cor, expected_cor)

    def test_exception_handling(self):
        # Test handling of words in the exceptions list
        # Sentence: वह खुश है।
        # Expected: No change since 'है' is in exceptions
        sentence = [
            ('वह', 'PRP', []),
            ('खुश', 'JJ', []),
            ('है', 'VAUX', [])
        ]
        expected_err = 'वह खुश है'
        expected_cor = 'वह खुश है'
        err, cor = insert_errors(sentence)
        self.assertEqual(err, expected_err)
        self.assertEqual(cor, expected_cor)

    def test_no_error_introduced(self):
        # Test that the function doesn't introduce errors when it shouldn't
        # Sentence: मुझे खाना पसंद है।
        # Expected: No change
        sentence = [
            ('मुझे', 'PRP', []),
            ('खाना', 'NN', []),
            ('पसंद', 'JJ', []),
            ('है', 'VAUX', [])
        ]
        expected_err = 'मुझे खाना पसंद है'
        expected_cor = 'मुझे खाना पसंद है'
        err, cor = insert_errors(sentence)
        self.assertEqual(err, expected_err)
        self.assertEqual(cor, expected_cor)

if __name__ == '__main__':
    unittest.main()
