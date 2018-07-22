![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")

Super simple bash script that enables a PGP (GnuPG) encrypted chat between two hosts,
when the script is used on both hosts.

You can also upload files, encrypted, during a chat session.

## Usage
```bash
./gpgchat <pub key id> <host> <port> [remote port]
```
The remote port is only necessary when both chats are running on the same host.

When you're in a chat, you can type `>>>[file]` to send a file to the remote.
In case you did not specify a file, a file selection dialog will execute.
