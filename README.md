# domain_info_grabber
A small OSINT tool for domain lookups. Provide a domain and get back IP, server location, WHOIS and DNS records in one report.

## How to run

    pip install python-whois dnspython requests
    python grabber.py example.com

## What you get back

* IP address
* Server location
* WHOIS info (registrar, dates, name servers)
* DNS records (A, MX, NS)

## Heads up

Built for learning and testing against domains you own or have permission to poke. Don't point it at stuff that ain't yours.
