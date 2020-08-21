## Exploit Title: Tailor MS v1.0 - Reflected XSS Key Logger
### Exploit Author: Bobby Cooke (boku)
+ Reflected Cross-Site Scripting (XSS) vulnerability in 'index.php' login-portal webpage of SourceCodesters Tailor Management System v1.0 allows remote attackers to harvest keys pressed via unauthenticated victim clicking malicious URL and typing.
![](tailor-xss-keylogger.gif)
+ OWASP Top Ten 2017: A7:2017-Cross-Site Scripting (XSS)
+ CWE-79: Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') - Type 1: Reflected XSS
+ CWE-523: Unprotected Transport of Credentials
+ CVSS Base Score: 6.4 
  - Impact Subscore: 4.7 
  - Exploitability Subscore: 1.6
+ CVSS v3.1 Vector: AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:L/A:L
#### Vendor Homepage: https://www.sourcecodester.com
#### Software Link: https://www.sourcecodester.com/sites/default/files/download/Warren%20Daloyan/tailor.zip
#### Tested On: Windows 10 Pro + XAMPP | Python 2.7
