import crypto_sign_challenge
import unittest

class TestCryptoSignChallenge(unittest.TestCase):
    def test_withMoreThan256Characters(self): #this test checks if more than 250 character messages are processed or not
        IntendedFlag = False
        argument = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec."
        crypto_sign_challenge.message = argument
        crypto_sign_challenge.Check_Input() 
        ObservedOutput = crypto_sign_challenge.flag 
        self.assertEqual(IntendedFlag, ObservedOutput) #matching flags to check whether message within character limits
        
    def test_WithoutArguments(self): #this test checks if null messages are processed or not
        IntendedFlag = False
        crypto_sign_challenge.Main()
        ObservedOutput = crypto_sign_challenge.flag
        self.assertEqual(IntendedFlag, ObservedOutput) #matching flags to check whether message within character limits
        
    def test_withNormalArguments(self): #this test checks if messages within character limitations are processed or not
        argument = "Hello Zindagi"
        crypto_sign_challenge.message = argument
        crypto_sign_challenge.CheckIfdirectoryExistsAndThenConfigureKeys()
        crypto_sign_challenge.SigningTheMessage()
        self.assertTrue(crypto_sign_challenge.FormJSON()) #checking if JSON is printed by the return boolean executed after it.


if __name__ == "__main__":
    unittest.main() #executing the test cases.

