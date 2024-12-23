import socket

import dns.resolver
import dns.reversename


def check_akamai(domain):
    try:
        # Get IP and check reverse DNS
        ip = socket.gethostbyname(domain)
        print(ip)
        rev_name = dns.reversename.from_address(ip)
        print(rev_name)
        reversed_dns = dns.resolver.query(rev_name, "PTR")[0]
        if "akamai" in str(reversed_dns):
            return "Akamai detected via reverse DNS"

        return "No Akamai detected"
    except Exception as e:
        return "Error: " + str(e)


domains = [
    "www.barnesandnoble.com",
    "www.bedbathandbeyond.com",
    "www.bestbuy.com",
    "www.bloomingdales.com",
    "www.clinique.com",
    "www.costco.com",
    "www.cremedelamer.com",
    "www.dillards.com",
    "www.jared.com",
    "www.kohls.com",
    "www.macys.com",
    "www.petsmart.com",
    "www.playstation.com",
    "www.saksfifthavenue.com",
    "www.saksoff5th.com",
    "www.samsclub.com",
    "www.sephora.com",
    "www.staples.com",
    "www.tiffany.com",
    "www.tjmaxx.com",
    "www.tjmaxx.tjx.com",
    "www.vive.com",
    "www.walgreens.com",
    "www.zoro.com",
]

for domain in domains:
    print(domain + ":\t" + check_akamai(domain))
