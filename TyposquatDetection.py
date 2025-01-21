import itertools
import string
import dns.resolver

def generate_typosquatted_domains(domain):
    """
    Generates potential typo-squatted domains based on common techniques.
    """
    base_name, tld = domain.split('.')
    variations = set()

    # 1. Character omission
    for i in range(len(base_name)):
        variations.add(base_name[:i] + base_name[i + 1:])

    # 2. Character swapping
    for i in range(len(base_name) - 1):
        swapped = list(base_name)
        swapped[i], swapped[i + 1] = swapped[i + 1], swapped[i]
        variations.add(''.join(swapped))

    # 3. Character replacement
    for i in range(len(base_name)):
        for c in string.ascii_lowercase:
            variations.add(base_name[:i] + c + base_name[i + 1:])

    # 4. Character insertion
    for i in range(len(base_name) + 1):
        for c in string.ascii_lowercase:
            variations.add(base_name[:i] + c + base_name[i:])

    # 5. Adding a hyphen
    for i in range(1, len(base_name)):
        variations.add(base_name[:i] + '-' + base_name[i:])

    # Combine with the TLD
    return [f"{var}.{tld}" for var in variations if var != base_name]


def check_domain_availability(domains):
    """
    Checks the DNS resolution of a list of domains to identify active ones.
    """
    active_domains = []
    for domain in domains:
        try:
            # Attempt to resolve the domain's A record
            dns.resolver.resolve(domain, 'A')
            active_domains.append(domain)
        except dns.resolver.NXDOMAIN:
            # Domain does not exist
            pass
        except Exception as e:
            print(f"Error resolving {domain}: {e}")
    return active_domains


def main():
    legitimate_domain = input("Enter the legitimate domain (e.g., example.com): ").strip()
    print("\nGenerating potential typo-squatted domains...")
    typosquatted_domains = generate_typosquatted_domains(legitimate_domain)

    print(f"\nGenerated {len(typosquatted_domains)} potential typo-squatted domains.")
    print("Checking for active domains...")
    active_domains = check_domain_availability(typosquatted_domains)

    if active_domains:
        print("\nActive domains detected:")
        for domain in active_domains:
            print(f"- {domain}")
    else:
        print("\nNo active typo-squatted domains detected.")


if __name__ == "__main__":
    main()
