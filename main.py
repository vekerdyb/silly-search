from random import randint
import requests
import re
import urlparse

links_regular_expression = re.compile("(http[s]?://[^\s\"><]+)")


def download(url):
    try:
        response = requests.get(url)
    except:
        return ""
    return response.text


def get_links(text):
    return links_regular_expression.findall(text)


hosts = ["http://index.hu"]
visited_links = []
emails = []

while len(hosts) < 100:
    current_host = hosts[randint(0, len(hosts) - 1)]
    hosts.remove(current_host)
    if current_host not in visited_links:
        print "attempting to download %s" % current_host
        html_content = download(current_host)
        if html_content:
            raw_links = get_links(html_content)
            new_hosts = []
            for l in set(raw_links):
                parsed = urlparse.urlparse(l)
                new_hosts.append("%s://%s" % (parsed.scheme, parsed.netloc))
            hosts = list(set(hosts))
            visited_links.append(current_host)
            print "number of hosts retrieved: %d" % len(hosts)
    else:
        pass

for host in hosts:
    print host

for v in visited_links:
    print "visited: %s" % v