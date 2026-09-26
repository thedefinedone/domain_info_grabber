import sys
import socket
import requests
import whois
import dns.resolver


def get_ip(domian):
    try:
        return socket.gethostbyname(domian)
    except:
        return None


def get_location(ip):
    if not ip:
        return "unknown"
    try:
        r = requests.get(f"http://ip-api.com/json/{ip}", timeout=5).json()
        if r.get("status") == "success":
            return f"{r['city']}, {r['country']}"
        return "unknown"
    except:
        return "lookup failed"


def get_whois(domain):
    try:
        w = whois.whois(domain)
        return {
            "Registrar": w.registrar,
            "Created": w.creation_date,
            "Expires": w.expiration_date,
            "Name Servers": w.name_servers,
        }
    except:
        return {"Error": "WHOIS blocked or invalid domain"}


def get_dns(domain):
    records = {}
    for q in ['A', 'MX', 'NS']:
        try:
            answers = dns.resolver.resolve(domain, q)
            if q == 'MX':
                records[q] = [f"{a.preference} {a.exchange}" for a in answers]
            else:
                records[q] = [str(a) for a in answers]
        except:
            records[q] = []
    return records


def main():
    if len(sys.argv) < 2:
        print("Usage: py grabber.py example.com")
        return

    domain = sys.argv[1]
    print(f"\n--- scanning: {domain} ---\n")

    ip = get_ip(domain)
    print(f"[+] IP Address: {ip}")

    if ip:
        print(f"[+] Server Location: {get_location(ip)}")

    print(f"\n[+] WHOIS Registry:")
    for key, value in get_whois(domain).items():
        print(f"    {key}: {value}")

    print(f"\n[+] DNS Records:")
    for record_type, values in get_dns(domain).items():
        print(f"    {record_type}: {', '.join(values) if values else 'No records found'}")


if __name__ == "__main__":
    main()