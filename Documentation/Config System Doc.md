# PicoOS Global Configuration System

The Folder `/picoos/config` Contains A Hierachry Style Configuration System. 
Each Config "key" Is a String but can be used as any data type. "keys" Are `*.cfg` Files with names following this standard : `A_VERY_IMPORTANT_KEY.cfg`.
in the config folder, There is a important Tree structure which is to organize The diffrent Config Keys.

To create a key, Simply Create a `.cfg` file and name it with your key name. Then open it, and set the value inside  the file **without any formatting** EX : 
```
very important string
```
Or
```
69420
```

Technically, all keys are strings. But, they can be converted to `int` or `bool` using special functions

---

## Registry Tree Structure :
```
Registry Root
┣ SYSTEM : For system Files
┃ ┣ boot : Bootloader Related Config
┃ ┣ setup : setup related config
┃ ┗ software : System software related config
┣ SOFTWARE : Software Related Config
┃ ┗ [softwareNameHere] : Config For Specific Program
┣ DEVICE : External Devices Related Config
┣ CLASSES : Classes Related Config
┗ PROGRAMS : Program List, Installers And Uninstallers
```
