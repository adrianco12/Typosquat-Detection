# Typosquat-Detection
This Python script is designed to detect potential typo-squatted domains, which are domain names resembling a legitimate one, often used maliciously for phishing or other fraudulent activities.

1. Generating Typo-Squatted Domains
The script begins by prompting the user to input a legitimate domain (e.g., example.com). It then uses afunction to create variations of this domain based on common typo-squatting techniques. These techniques include:

Character Omission: Removing one character at a time to mimic accidental key skips.
Character Swapping: Exchanging adjacent characters to simulate mistyped keystrokes.
Character Replacement: Replacing each character with every possible lowercase letter.
Character Insertion: Inserting every lowercase letter at each position to mimic unintended extra keystrokes.
Adding Hyphens: Inserting hyphens to create plausible variations.
Each technique manipulates the base name of the domain (e.g., example) to produce a variety of plausible typo-squatted domains. These variations are combined with the original top-level domain (e.g., .com) and stored in a set to avoid duplicates.

2. Checking Domain Availability
Once the typo-squatted variations are generated, the script uses the check_domain_availability function to determine which of these domains are active. This function performs DNS resolution using Python’s socket library. For each generated domain, it attempts to resolve its IP address by sending a DNS query. If the domain resolves successfully, it is marked as active, meaning the typo-squatted domain is currently live and potentially being used.

3. Reporting Results
After checking the availability of all typo-squatted domains, the script categorizes them into active and inactive lists. Active domains are those that resolved to an IP address, indicating they could be used for malicious purposes. The results are displayed to the user:

If active domains are detected, they are listed, signaling a potential threat.
If no active domains are found, the user is informed that no immediate risks were detected.

Conclusion
The script provides an automated way to identify potential threats from typo-squatted domains. It combines logical generation techniques with real-time DNS queries to produce actionable insights. By focusing on active domains, it prioritizes potential security risks that warrant further investigation. This approach helps cybersecurity professionals or concerned individuals proactively detect and address threats associated with typo-squatting.
