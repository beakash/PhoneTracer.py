from .tracer import PhoneTracer
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="PhoneTracer - OSINT phone number tracing tool")
    parser.add_argument('number', nargs='?', help="Phone number to trace (in international format)")
    args = parser.parse_args()
    
    tracer = PhoneTracer()
    
    print(f"[+] PhoneTracer v{tracer.version} - OSINT")
    
    if args.number:
        number = args.number
    else:
        number = input("[*] Enter phone number to trace (e.g. +12125551234): ")
    
    print(f"[*] Target: {number}")
    print("[*] Initiating trace...")
    
    result = tracer.trace(number)
    
    if result['valid']:
        print(f"[+] Country/Region: {result['location']}")
        print("[+] Trace complete")
    else:
        print(f"[!] Error: {result['error']}")
        print("[!] Please enter a valid phone number in international format")

if __name__ == "__main__":
    main()
