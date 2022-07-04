# EncryptUtils
 *A small encrypting/decrypting toolkit which includes support for text and files.*

### Table of contents
[Back to top](#encryptutils)

 [Table of contents](#table-of-contents)

[Installation](#installation)
  * [Using pip](#using-pip)
    * [Unix/mac/linux](#unixmaclinux)
	* [Windows](#windows)
  * [Using git clone](#using-git-clone)
    * [Unix/mac/linux](#unixmaclinux-1)
	* [Windows](#windows-1)

[Usage](#usage)
  * [Encrypting text](#encrypting-text)
  * [Decrypting text](#decrypting-text)
  * [Encrypting a file](#encrypting-a-file)
  * [Decrypting a file](#decrypting-a-file)
  * [Encrypting multiple files](#encrypting-multiple-files)
  * [Decrypting multiple files](#decrypting-multiple-files)


## Installation
You can install EncryptUtils in two methods:

### Using `pip`
To install this package using pip, simply run the following command:

#### Unix/mac/linux:
```bash
pip3 install encryptutils
```

#### Windows:
```cmd
pip install encryptutils
```

### Using `git clone`
***WARNING: THIS SECTION IS A WORK IN PROGRESS***
You can also install EncryptUtils by running `git clone`.

#### Unix/mac/linux:
```bash
git clone https://github.com/tinkering-townsperson/encryptutils

cd encryptutils
chown install.sh 755
./install
```

#### Windows:
```cmd
git clone https://github.com/tinkering-townsperson/encryptutils
cd encryptutils
.\install
```

## Usage

### Encrypting text
To encrypt text in the form of a string or byte-like object, you can use the `encrypt()` method.

`encryptingMyPyPIToken.py`
```py
from encryptutils import *
from pathlib import Path
from cryptography.fernet import Fernet

myKey = Fernet.generate_key()
myPyPIToken = "pypi-~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

encrypt(myPyPIToken, myKey)
```

### Decrypting text
To decrypt text, use the `decrypt()` method

`decryptingMyPyPITokenBecauseINeedItNow.py`
```py
from encryptutils import *
from pathlib import Path
from cryptography.fernet import Fernet

myEncryptedPyPIToken = "niQaqhetJzLHW56cFaDQuG6kcLizYicrdth4xeiruyg=\n\ngAAAAABiw2yHQkEclSVxSyqLuw1EKoAKErh_pLCMKsC2y-udbPm6T5Q96YwONikdPrE6WTf--XS-_qvs3vx95OdbTnATtfNPma0XBesR9O9ftZdnx3leSYhmK2Nq3oP2nB_u3xACfK09y0QmTiHAbA2BlXo-2vnbm-bb5JHZzzMm72jCHw19uuWWQANTbIi38b3VTpt3UHcf1rEu_I-GRA7LXwxQ9Djk4Ueq3mHykTXqs8duM9hK461ZLNr6AoskbCK0On9LDa6ZDoOULjnDmKvC35Ai8e3-zcVM4YHEoxgaRmZbTHhtUM0="

decrypt(myPyPIToken)
```
You may have noticed that you do not need to provide `decrypt()` with a key. This is because when you encrypt files with `encrypt()` the method concatenates(adds) the key to the encrypted data. `decrypt()` splits the key and data apart, and uses the key to decrypt the encrypted data!

### Encrypting a file
To encrypt a file, simply import it in a python file *or* the interactive prompt. Here is an example:

`encryptMyPasswords.py`
```py
from encryptutils import *
from pathlib import Path
from cryptography.fernet import Fernet

myKey = Fernet.generate_key()
myPasswordsPath = Path("C:\\Users\\AfterNoonPM\\myPasswords.csv")

encrypt_file(myPasswordsPath, myKey)
```

### Decrypting a file
Decrypting a file is more of the same story:

`decryptMyPasswordsBecauseIForgotThemOops.py`
```py
from encryptutils import *
from pathlib import Path

myForgottenPasswordsPath = Path("C:\\Users\\AfterNoonPM\\myPasswords.csv")

decrypt_file(myPasswordsPath)
```
You may have noticed that you do not need to provide `decrypt_file()` with a key. The reason for this is almost the same as mentioned [here](#decrypting-text).

### Encrypting multiple files
Encrypting multiple files is almost the same as encrypting one, with a few minor differences.

`encryptingMyPictures.py`
```py
from encryptutils import *
from pathlib import Path
from cryptography.fernet import Fernet

myKey = Fernet.generate_key()
myPicture1 = Path("C:\\Users\\AfterNoonPM\\Pictures\\myPicture1.png")
myPicture2 = Path("C:\\Users\\AfterNoonPM\\Pictures\\myPicture2.png")
myPicture3 = Path("C:\\Users\\AfterNoonPM\\Pictures\\myPicture3.png")
myPicture4 = Path("C:\\Users\\AfterNoonPM\\Pictures\\myPicture4.png")

encrypt_files((myPicture1, myPicture2, myPicture3, myPicture4), myKey)
```
### Decrypting multiple files
Decrypting multiple files is almost the same.

`decryptingMyPreciousPictures.py`
```py
from encryptutils import *
from pathlib import Path
from cryptography.fernet import Fernet

myKey = Fernet.generate_key()
myEncryptedPicture1 = Path("C:\\Users\\AfterNoonPM\\Pictures\\myPicture1.png")
myEncryptedPicture2 = Path("C:\\Users\\AfterNoonPM\\Pictures\\myPicture2.png")
myEncryptedPicture3 = Path("C:\\Users\\AfterNoonPM\\Pictures\\myPicture3.png")
myEncryptedPicture4 = Path("C:\\Users\\AfterNoonPM\\Pictures\\myPicture4.png")

decrypt_files((myPicture1, myPicture2, myPicture3, myPicture4))
```
And not including the key still has the same reason as [here](#decrypting-text)

