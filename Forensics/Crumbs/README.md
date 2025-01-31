# Forensics: Crumbs

**Author**: [greed](https://github.com/greedoftheendless)<br>
**Points**: 120<br>
**Hint(s)**: None<br>
**Flag**: `xploit{Macros_Unleashed_4N4lyz3d}`<br>

**Challenge description:**
```
The Incident Response team at Microhard Inc. has been up all night, only to come across this one document left behind. Did VisuallyBoring syndicate, the notorious hacktivist group strike again?
```

## Solve

This challenge involves analysing the macros in a word .docm file. The provided docm has the file extension .docm which means there is macros in the file.
Macros are snippets of code usually written in VisualBasic to do certain task, when the file is opened. Macros are used by attackers to run malicious code. 

### See macro code in word:
Open the Word document, press `Alt + F11` to open the VBA Editor, then check the Modules under "Microsoft Word Objects" for macro code. Alternatively, enable the **Developer** tab, click **Macros**, select one, and click **Edit** to view the code.

### See macro in libreoffice:
Open the document in LibreOffice Writer, then press `Alt + F11` to open the **Macro Editor** and browse under "LibreOffice Macros" to find the code. Alternatively, go to **Tools** > **Macros** > **Edit Macros** to view or modify them.

### Command line:
use the olevba tool to list macros in a document file!

```bash

└──╼ $olevba message_for_microhard.docm
olevba 0.60.1 on Python 3.11.2 - http://decalage.info/python/oletools
===============================================================================
FILE: message_for_microhard.docm
Type: OpenXML
WARNING  For now, VBA stomping cannot be detected for files in memory
-------------------------------------------------------------------------------
VBA MACRO ThisDocument.cls
in file: word/vbaProject.bin - OLE stream: 'VBA/ThisDocument'
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
(empty macro)
-------------------------------------------------------------------------------
VBA MACRO Module1.bas
in file: word/vbaProject.bin - OLE stream: 'VBA/Module1'
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Sub GetFlag()
    Dim Flag As String
    Flag = "xploit{Macros_Unleashed_4N4lyz3d}"
    MsgBox "The hidden flag is: " & Flag
End Sub

No suspicious keyword or IOC found.

```
