import os, subprocess

for exs in os.listdir('.'):
  if os.path.isfile(exs) and exs.endswith('.exs'):
    print 'converting', exs
    sfz = exs[:-4] + '.sfz'
    subprocess.call(['/usr/local/bin/python3', '/Users/rick/exs2sfz.py', exs, sfz, '../Audio'])
    #os.remove(exs)
