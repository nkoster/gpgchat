![alt text](https://raw.githubusercontent.com/nkoster/gpgchat/master/upload.png "gpgchat")

Simple bash script that enables a PGP (GnuPG) encrypted chat between two hosts,
and two single public keys, when the script is used on both hosts.

You can also transfer a file, PGP encrypted, during a chat session.

Plus, you can execute a local command, or run a shell, within a chat session.

### Usage
```
./gpgchat <pub key id> <host> <port> [remote port]
```
The remote port is only necessary when both chats are running on the same host.

### Send a file
When you're in a chat, you can type **`>>>[file]`** to send a file to the remote.
In case you did not specify a file, a file selection dialog will execute.
On the remote host, the file goes to **`/tmp/gpgchat/`**.

### Execute a command
You can type **`!!![command]`** to run a command within a chat session.
If you omit the command, the default OS shell will be executed.

### Dependencies
The script is depending on **`gpg`** and **`ncat`** (part of the **`nmap`**
package), and **`python`** for the Gtk+ file selection dialog. 
