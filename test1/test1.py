import commands
(status, output) = commands.getstatusoutput('ls /bin')
print status, output
