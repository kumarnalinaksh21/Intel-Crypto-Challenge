Crypto Sign
===========

Crypto Sign is Kumar Nalinaksh's personal submission to the code challenge prompt found below.

Installing
----------

This is intended to be used on Unix based file systems.
However this script has been written in such a manner that it can be executed on Windows and Linux both.

To run this script you need to have Python3 installed.


Usage
-----

    crypto-sign-challenge MESSAGE

`MESSAGE` is the message you wish to sign with your private key.  

The following is an example with output included.

```
$ crypto-sign-challenge 'Welcome to the Jungle'
{
    "message": "Welcome to the Jungle",
    "signature": "MIGIAkIBHEc8FETUYOPze9YxePzBfN2OjbstTYQxfViHu6vziSfDbM5iJ8jCmH3LkScgoTNCRBAMBY407jDC/fYq88iN22cCQgCmytbObfzxtHWHpcYFvOb3PHHDKlv+rtAZJ/+AdxBvihjY/xRDi1PH8GhyEgzW7xzJ1KF7BhqmeMwH9pXUCx6JiA==",
    "pubkey": "-----BEGIN PUBLIC KEY-----\nMIGbMBAGByqGSM49AgEGBSuBBAAjA4GGAAQAxMXE/k5LOn1ZeSNgILi/fsDyHwwW\nSugmEndN786laNFUJ0Ulzit1FumnY71Op7Gwuqrv+YoqrEwpHtpnV8mLgvEBr9sX\ncNatfZzPtjOLpHzkVfLSCX94E7uNUZx13eigwugCsR87rn94CLRU3GDbLnLO6W4f\n12FkAhynQpvqaWNKpn8=\n-----END PUBLIC KEY-----\n"
}
```

Storage
-------

This project will generate a new RSA private - public key pair if it does not exist and will store
it in:

    $HOME/.local/share/signer

If the directory does not exist, it will try to create it. Incase the directory creation is unsucccessful due to access permission issues, then it will use the current working directory.

Code Challenge Prompt
---------------------

Using Python, provide an application that meets the following
requirements:

  - Given a string input of up to 250 characters, return a JSON response
    compliant to the schema defined below.
    - You are responsible for generating a public/private RSA or ECDSA keypair
      and persisting the keypair on the filesystem
      - Subsequent invocations of your application should read from the same
        files
  - Document your code, at a minimum defining parameter types and return values
    for any public methods
  - Include Unit Test(s) with instructions on how a Continuous Integration
    system can execute your test(s)
  - You may only use first order libraries, you may not use any third party
    libraries or packages.  For example, you may use the OpenSSL library, but
    you may not use any libraries built on top of OpenSSL.

JSON Schema for your application response:

```json
{
    "$schema": "http://json-schema.org/draft-04/schema#",
    "title": "Signed Identifier",
    "description": "Schema for a signed identifier",
    "type": "object",
    "required": [ "message", "signature", "pubkey" ],
    "properties": {
        "message": {
            "type": "string",
            "description": "original string provided as the input to your app"
        },
        "signature": {
            "type": "string",
            "description": "RFC 4648 compliant Base64 encoded cryptographic signature of the input, calculated using the private key and the SHA256 digest of the input"
        },
        "pubkey": {
            "type": "string",
            "description": "Base64 encoded string (PEM format) of the public key generated from the private key used to create the digital signature"
        }
    }
}
```


Documentation
=============

SAMPLE EXECUTION
---------------------

```
>python crypto_sign_challenge.py Hello World!
```

Output:

```json
{
   "message": "Hello World! ",
   "signature": "fQOnDSvDbHVOExLA/Ss9wfhVvFepNtQ59qkk9pl6ZEyixbY+6CblmAcaEblNTJcir6FEHzslph7z\nsGawOVh7/WPUF6gg3Inl+hASmlzIkCBDLAr1smbbahoVv9BMqMWiaapHS1A3/Mo45ddrx8DxIp4K\n7nOh4sa0wdjynB0teI5UnfEUFUwmdx+ENuRScc5tUhr9kUdk9+SOXn88T8M77W4sfG7UF7lVHwmT\nv5YbiDSLFq3khY9OzI/Pe2d8IP0DKBBfg6WrecWyKJVmhfUafq9OskRX/knVYhvkHntIzB81AdnS\nH3GpiddlPO8KHnq8059fCbEiPGVUIj9C2Bk5cQ==\n",
   "pubkey": "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAv2OTb1wxV62Rmlzxz70e\nEzmAWcBdixjqivrczJo9FeJpQjcV97XWFi6lJKpYkBiAOT8sYiWxNFaoDd1l5utO\ntrVEV9z3ZP4OrOOnLQjmIB6oaAKCIwUD2jdKb+1dl35f3CzQMEQoxefSsygYHLnv\nDv/wB9YzG6WHiqiqJnMeDLbPd2azgeOUrxGDnNNDf3olJVOzp5sEqauHfFXAP3JL\nhCfD44ATRH1tySSvj3TziFOyjNfDD4/6RZfnloyozVco2zOG7uiEcsg8fVIy7vBm\n1fFxNWleTfvEsS8YpLJ31WkYyiMJAcIbZhrnvhIK/Kt2cAbDcKBOUcvSaTacIUAr\nfwIDAQAB\n-----END PUBLIC KEY-----\n"
}
```

Logs generated (crypto_sign_challenge.log) as follows:

```log
2021-10-05 07:11:53,137 - root - Script has been invoked!
2021-10-05 07:11:53,189 - root - Constructing the message from parsed arguments.
2021-10-05 07:11:53,189 - root - The message is within acceptable parameters
2021-10-05 07:11:53,226 - root - Default directory does not esist.
2021-10-05 07:11:53,226 - root - Attempting to creating the directory
2021-10-05 07:11:53,228 - root - Default directory could not be created due to access permission issue.
2021-10-05 07:11:53,228 - root - Instead of default directory program will now use current working directory.
2021-10-05 07:11:53,228 - root - Private and Public keys does not exist.
2021-10-05 07:11:53,435 - root - Key pair has been generated
2021-10-05 07:11:53,435 - root - Private key has been written to the PEM file.
2021-10-05 07:11:53,437 - root - Private key has been configured in the form of pkey() object.
2021-10-05 07:11:53,437 - root - Public key has been written to the PEM file.
2021-10-05 07:11:53,438 - root - Public key has been loaded from the PEM file and decoded to Base64.
2021-10-05 07:11:53,443 - root - Signature has been formed and decoded to Base64
2021-10-05 07:11:53,443 - root - {'message': 'Hello World! ', 'signature': 'fQOnDSvDbHVOExLA/Ss9wfhVvFepNtQ59qkk9pl6ZEyixbY+6CblmAcaEblNTJcir6FEHzslph7z\nsGawOVh7/WPUF6gg3Inl+hASmlzIkCBDLAr1smbbahoVv9BMqMWiaapHS1A3/Mo45ddrx8DxIp4K\n7nOh4sa0wdjynB0teI5UnfEUFUwmdx+ENuRScc5tUhr9kUdk9+SOXn88T8M77W4sfG7UF7lVHwmT\nv5YbiDSLFq3khY9OzI/Pe2d8IP0DKBBfg6WrecWyKJVmhfUafq9OskRX/knVYhvkHntIzB81AdnS\nH3GpiddlPO8KHnq8059fCbEiPGVUIj9C2Bk5cQ==\n', 'pubkey': '-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAv2OTb1wxV62Rmlzxz70e\nEzmAWcBdixjqivrczJo9FeJpQjcV97XWFi6lJKpYkBiAOT8sYiWxNFaoDd1l5utO\ntrVEV9z3ZP4OrOOnLQjmIB6oaAKCIwUD2jdKb+1dl35f3CzQMEQoxefSsygYHLnv\nDv/wB9YzG6WHiqiqJnMeDLbPd2azgeOUrxGDnNNDf3olJVOzp5sEqauHfFXAP3JL\nhCfD44ATRH1tySSvj3TziFOyjNfDD4/6RZfnloyozVco2zOG7uiEcsg8fVIy7vBm\n1fFxNWleTfvEsS8YpLJ31WkYyiMJAcIbZhrnvhIK/Kt2cAbDcKBOUcvSaTacIUAr\nfwIDAQAB\n-----END PUBLIC KEY-----\n'}
2021-10-05 07:11:53,444 - root - JSON has been formed and decoded to Base64
2021-10-05 07:11:53,444 - root - Script execution has completed successfully!
```


EXECUTING UNIT TESTING
---------------------

There are three test cases:
1. Testing with 0 characters as message.
2. Testing with message within character limitations of 1-250.
3. Testing with message of more than 250 characters.

```
>python test.py
```

Output:

```
..{
   "message": "Hello Zindagi",
   "signature": "UOsiKZkmxG0b0/lSgsCaEIamiJBoFThnN1exNnuwX7n8cxVsHwInzKNOWLjb1XXh0GYY/za88uPR\nSUngZVeYmM7x5N092BdPZkj9+BXnm1idzDM92E9xk2KCGzHsyhPnsjeK4tq574GJgV22xm9+duY+\nKNuEbs6VdH2LikhDfJL1FYCOeOfRGbpBCo27f+A8ELPK7EWiJNvN3IJ2vO8mTHqdyvAlAKxK3krY\nITDnYJm+31kv+bClipJqEWWV1TEnpNgXiQ480XvKsMWFSwIrTrRKfx5eVJ5k+dw00yn74eLrDzRq\nxYp8VJDISwLfl72sQsLXrXKOryUIb6dUcTR7kw==\n",
   "pubkey": "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAryemBvEqu/738BPsJbDJ\nIzWLIWKvthlDadk7UZfBHisTW/SCrdBa9oMsXhg0WhCLOYE+s2lPvNJ1oTX3BeLp\nxs2f9VrscVBLiK7yO+remGn0ZSgdRtm1zTHIoQphYHEBhZjduWbvDMWpgF9dEfM1\nBXay2ENb9SDFMmGKr64kGeod/h6nxvBXGohEpyEmwyx4U049kPW9kSzcR/H6+Ys/\nkS8Y6aHLoh3fVYFOplibtOOCtcYxMmT9vuA2vr7cSO3i5KkeYJXOkllCK4IC5HVC\nZkhp7jdXL/Q5IMzdhwZNpjadEshO9/HsD7IvAnGc1M06QadEgHM5BTKHt9nPibDt\nEQIDAQAB\n-----END PUBLIC KEY-----\n"
}
.
----------------------------------------------------------------------
Ran 3 tests in 0.018s

OK
```

Logs generated (crypto_sign_challenge.log) as follows:

```log
2021-10-05 07:19:10,297 - root - Script has been invoked!
2021-10-05 07:19:10,297 - root - Constructing the message from parsed arguments.
2021-10-05 07:19:10,298 - root - The message must be more than 1 character and less than 250 characters.
2021-10-05 07:19:10,298 - root - Script execution is unsuccessfull!
2021-10-05 07:19:10,298 - root - The message must be more than 1 character and less than 250 characters.
2021-10-05 07:19:10,298 - root - Script execution is unsuccessfull!
2021-10-05 07:19:10,299 - root - Default directory does not esist.
2021-10-05 07:19:10,299 - root - Attempting to creating the directory
2021-10-05 07:19:10,301 - root - Default directory could not be created due to access permission issue.
2021-10-05 07:19:10,301 - root - Instead of default directory program will now use current working directory.
2021-10-05 07:19:10,301 - root - Private and Public keys does not exist.
2021-10-05 07:19:10,416 - root - Key pair has been generated
2021-10-05 07:19:10,416 - root - Private key has been written to the PEM file.
2021-10-05 07:19:10,417 - root - Private key has been configured in the form of pkey() object.
2021-10-05 07:19:10,417 - root - Public key has been written to the PEM file.
2021-10-05 07:19:10,418 - root - Public key has been loaded from the PEM file and decoded to Base64.
2021-10-05 07:19:10,420 - root - Signature has been formed and decoded to Base64
2021-10-05 07:19:10,420 - root - {'message': 'Hello Zindagi', 'signature': 'UOsiKZkmxG0b0/lSgsCaEIamiJBoFThnN1exNnuwX7n8cxVsHwInzKNOWLjb1XXh0GYY/za88uPR\nSUngZVeYmM7x5N092BdPZkj9+BXnm1idzDM92E9xk2KCGzHsyhPnsjeK4tq574GJgV22xm9+duY+\nKNuEbs6VdH2LikhDfJL1FYCOeOfRGbpBCo27f+A8ELPK7EWiJNvN3IJ2vO8mTHqdyvAlAKxK3krY\nITDnYJm+31kv+bClipJqEWWV1TEnpNgXiQ480XvKsMWFSwIrTrRKfx5eVJ5k+dw00yn74eLrDzRq\nxYp8VJDISwLfl72sQsLXrXKOryUIb6dUcTR7kw==\n', 'pubkey': '-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAryemBvEqu/738BPsJbDJ\nIzWLIWKvthlDadk7UZfBHisTW/SCrdBa9oMsXhg0WhCLOYE+s2lPvNJ1oTX3BeLp\nxs2f9VrscVBLiK7yO+remGn0ZSgdRtm1zTHIoQphYHEBhZjduWbvDMWpgF9dEfM1\nBXay2ENb9SDFMmGKr64kGeod/h6nxvBXGohEpyEmwyx4U049kPW9kSzcR/H6+Ys/\nkS8Y6aHLoh3fVYFOplibtOOCtcYxMmT9vuA2vr7cSO3i5KkeYJXOkllCK4IC5HVC\nZkhp7jdXL/Q5IMzdhwZNpjadEshO9/HsD7IvAnGc1M06QadEgHM5BTKHt9nPibDt\nEQIDAQAB\n-----END PUBLIC KEY-----\n'}
2021-10-05 07:19:10,427 - root - JSON has been formed and decoded to Base64
```



Installing
----------