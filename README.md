![alt text](https://raw.githubusercontent.com/nkoster/gpgchat/master/upload.png "gpgchat")

Simple bash script that enables a PGP (GnuPG) encrypted chat between two hosts,
when the script is used on both hosts.

You can also exchange files, encrypted, during a chat session.

## Usage
```bash
./gpgchat <pub key id> <host> <port> [remote port]
```
The remote port is only necessary when both chats are running on the same host.

When you're in a chat, you can type `>>>[file]` to send a file to the remote.
In case you did not specify a file, a file selection dialog will execute.
