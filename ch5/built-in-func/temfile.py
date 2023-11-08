import tempfile

filename = tempfile.mktemp()
print(filename)
# filename.close()

f = tempfile.TemporaryFile()
f.close()
