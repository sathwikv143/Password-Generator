# Password-Generator
Random password generator, saving in file, encryption/decryption of file using python3
## Intention
  Instead of storing passwords in browser and else where
  this tool is developed to store all passwords on our own machine 
  with encryption and decryption option.
## Requirements
  python3 module pyAesCrypt
  
  ``` pip3 install pyAesCrypt ```
## Usage
```
python pass.py -m <mode> -u <username> -s <website>	
python pass.py -m <mode> -u <username> -s <website> -l <length>	
python pass.py -m <mode> -l <length>	
python pass.py -c <encrypt/decrypt>

Modes used : `strong`, `weak`, `medium`
Options to crypt file are : `encrypt`, `decrypt`

Random Password Generator

optional arguments:
  -h, --help                        Show this help message and exit
  -m MODE, --mode MODE              Modes to generate password
  -u USERNAME, --username USERNAME  Specify Username
  -s SITE, --site SITE              Specify Web Site
  -l LENGTH, --length LENGTH        Specify Length of Password
  -c CRYPT, --crypt CRYPT           Encrypt/Dycrypt file
```
