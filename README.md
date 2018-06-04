# Password-Generator
Random password generator, saving in file, encryption/decryption of file using python
## Intention
  Instead of storing passwords in browser and else where
  this tool is developed to store all passwords on our own machine.
## Requirements
  python3 module pyAesCrypt
  
  ``` pip3 install pyAesCrypt ```
## Usage
```
  python3 pass.py -m <mode> -u <username> -s <website>
  python3 pass.py -m <mode> -u <username> -s <website> -l <length>	
  python3 pass.py -m <mode> -l <length>	
  python3 pass.py -c <encrypt/decrypt>

optional arguments:
  -h, --help              show this help message and exit
  -m MODE, --mode MODE    Modes: strong|weak|medium
  -u USERNAME, --username USERNAME Specify Username
  -s SITE, --site SITE    Specify Web Site
  -l LENGTH, --length     LENGTH Specify Length of Password
  -c CRYPT, --crypt CRYPT Encrypt/Dycrypt file: encrypt|decrypt
```
