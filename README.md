# pyNtdllOverwrite

Overwrite ntdll.dll's ".text" section using a clean version of the DLL.  

It can help to evade security measures that install API hooks such as EDRs. 

The unhooked version of the DLL can be obtained from:

- A DLL file already on disk - For example "C:\Windows\System32\ntdll.dll".
- The KnownDlls folder ("\KnownDlls\ntdll.dll").
- A process created in debug mode - Processes created in suspended or debug mode have a clean ntdll.dll.


---------------------------------

### From disk

Get the clean ntdll.dll from disk. You can specify a file path or use the default value "C:\Windows\System32\ntdll.dll":

```
python pyNtdllOverwrite.py -o disk [-p PATH]
```

![img1](https://raw.githubusercontent.com/ricardojoserf/ricardojoserf.github.io/master/images/pyNtdllOverwrite/Screenshot_1.png)


### From KnownDlls folder

Get the clean ntdll.dll from the KnownDlls folder:

```
python pyNtdllOverwrite.py -o knowndlls
```

![img2](https://raw.githubusercontent.com/ricardojoserf/ricardojoserf.github.io/master/images/pyNtdllOverwrite/Screenshot_2.png)


### From a debug process

Get the clean ntdll.dll from a new process created with the DEBUG_PROCESS flag. You can specify a binary to create the process or use the default value "C:\Windows\System32\calc.exe":

```
python pyNtdllOverwrite.py -o debugproc [-p PATH]
```

![img3](https://raw.githubusercontent.com/ricardojoserf/ricardojoserf.github.io/master/images/pyNtdllOverwrite/Screenshot_3.png)

-------------------------------

### Links

- .NET implementation: [SharpNtdllOverwrite](https://github.com/ricardojoserf/SharpNtdllOverwrite)

- Golang implementation: [goNtdllOverwrite](https://github.com/ricardojoserf/goNtdllOverwrite)
