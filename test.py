import crypto_sign_challenge
import unittest
import argparse
import os, sys

class TestCryptoSignChallenge(unittest.TestCase):
    def test_withMoreThan256Characters(self):
        IntendedFlag = False
        argument = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec."
        crypto_sign_challenge.message = argument
        crypto_sign_challenge.Check_Input()
        ObservedOutput = crypto_sign_challenge.flag
        self.assertEqual(IntendedFlag, ObservedOutput)
        
    def test_WithoutArguments(self):
        IntendedFlag = False
        crypto_sign_challenge.Main()
        ObservedOutput = crypto_sign_challenge.flag
        self.assertEqual(IntendedFlag, ObservedOutput)
        
    def test_withNormalArguments(self):
        argument = "Hello Zindagi"
        crypto_sign_challenge.message = argument
        crypto_sign_challenge.CheckIfdirectoryExistsAndThenConfigureKeys()
        crypto_sign_challenge.SigningTheMessage()
        self.assertTrue(crypto_sign_challenge.FormJSON())


if __name__ == "__main__":
    unittest.main()

