# [ WaKali Experimental Framework ]

*This repo does not include its core. I will not share any code that includes code that automates any messenger. Thats your part, if you want to use this.*

```
/wakali
|-- /lib
|   |-- /modules
|   |   |-- /dirbust
|   |   |   |-- *dirbust.py & dirbust_config.json*
|   |   |-- /nmap
|   |   |   |-- *nmap.py & nmap.json*
|   |   |-- /ripper
|   |   |   |-- *ripper.py & ripper.json*
|   |   |-- /whois
|   |   |   |-- *whois.py & whois.json*
|   |   |-- *module_config.json*
|   |   |-- *module_core.py*
|   |-- /scripts
|   |   |-- /bot *your messengerbot comes here. Or somewhere you want, idc*
|   |   |-- *edit_conf.py*
|   |   |-- *install.py*
|   |   |-- *update.py*
|   |-- /versions
|   |   |-- When you update from the main menu, updated files will be stored here. Don't worry, we do not replace any code on accident here, never happened...
|   |-- core_config.json
|-- wakali.py *Mainfile*
|
|-- README.md
|-- .gitignore
```

# [ 1 Basics ]

Using commands you will be able to edit the *module_config.json*.

For example a command could look like this: *$set module nmap*.

This will then use the *nmap_config.json* as template for the needed values. *Obviously, every module we want to use, needs other values.*

The template for a modules *.json* file could look like this:

```
{
    "module": "nmap",
    "args": {
        "mode": "basic",
        "target": "192.168.191.69"
    }
}
```

When you set up all the values for the module, you could start the module by calling the *module_core.py* which will take the name of the module,

in this example: *nmap* and runs the pythonfile executing the module in some way and either returning the complete consoleoutput, the result saved in a textfile, a screenshot or something else.

*But that part is already deep into the messengerpart*

# 2 Usage

This repo is soley for the purpose, that my friend and I can update the mainframecode, without having to worry about moving files around.

