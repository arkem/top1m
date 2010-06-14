#!/usr/bin/python3
import sys
import urllib.parse

maxsites = 5000
failurl = 'http://arkem.org/failurl.html'
sites = {l.split(',')[1].strip() for l in open('/home/arkem/top-1m.csv') if int(l.split(',')[0]) <= maxsites}
sites.add(urllib.parse.urlparse(failurl).netloc)

for l in sys.stdin:
    try:
        fqdn = urllib.parse.urlparse(l.split()[0]).netloc
        if fqdn not in sites and \
            ".".join(fqdn.split('.')[1:]) not in sites:
            sys.stdout.write('%s?fqdn=%s\n' % (failurl, fqdn))
        else:
            sys.stdout.write('\n')
        sys.stdout.flush()
    except Exception as e:
        pass
