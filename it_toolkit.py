print("==============================")
def port_lookup():
     print ()
     print ("------ PORT LOOKUP ------")
     
     port = input("Enter a port number: ")
               
     if   port == "80":
          print("Service: HTTP")
          print("Purpose: Standard web traffic")

     elif port == "443":
          print("Service: HTTPS")

          print("Purpose: Secure encrypted web traffic")

     elif port == "22":
          print("Service: SSH")
          print("Purpose: Secure remote access") 

     elif port == "21":
          print ("Service: FTP")
          print ("purpose: File transfer")

     elif port == "25":
          print ("service: SMTP")
          print ("purpose: sending email") 

     elif port == "53": 
          print ("service: DNS")
          print ("purpose: Resolves domain names to IP addresses")

     elif port == "110":
          print ("srvice: pop3")
          print ("porpose: receiving email")    

     elif port == "143":
          print ("service: IMAP")   
          print ("purpose: Accessing and managing email")
     else:
          print("port not found in my database")


def dns_helper():
    print()
    print("------ DNS RECORD HELPER ------")
    print()
    print("A     - IPv4 address")
    print("AAAA  - IPv6 address")
    print("CNAME - Alias / another name")
    print("MX    - Mail server")
    print()

    record = input("Enter a DNS record type: ").strip().upper()

    if record == "A":
        print("A record maps a domain name to an IPv4 address.")

    elif record == "AAAA":
        print("AAAA record maps a domain name to an IPv6 address.")

    elif record == "CNAME":
        print("CNAME creates an alias for another domain name.")

    elif record == "MX":
        print("MX tells DNS which mail server handles email.")

    else:
        print("DNS record not found.")          

def converter():
    print()
    print("------ BITS & BYTES CONVERTER ------")
    print()
    print("1. Bits -> Bytes")
    print("2. Bytes -> Bits")
    print("3. KB -> MB")
    print("4. MB -> GB")
    print("5. GB -> MB")
    print()

    conversion = input("Choose a conversion: ").strip()

    if conversion == "1":
        bits = float(input("Enter number of bits: "))
        bytes_result = bytes / 8
        print("Result:", bytes_result, "bytes")

    elif conversion == "2":
        bytes_amount = float(input("Enter number of bytes: "))
        bits_result = bytes_amount * 8
        print("Result:", bits_result, "bits")

    elif conversion == "3":
        kb = float(input("Enter number of KB: "))
        mb_result = kb / 1024
        print("Result:", mb_result, "MB")

    elif conversion == "4":
        mb = float(input("Enter number of MB: "))
        gb_result = mb / 1024
        print("Result:", gb_result, "GB")

    elif conversion == "5":
        gb = float(input("Enter number of GB: "))
        mb_result = gb * 1024
        print("Result:", mb_result, "MB")

    else:
        print("Invalid conversion.")

def troubleshooting():
    print()
    print("------ TROUBLESHOOTING HELPER ------")
    print()
    print("1. No Internet")
    print("2. Slow Computer")
    print("3. No Display")
    print("4. Wi-Fi Network Not Showing")
    print()

    problem = input("Choose a problem: ").strip()

    if problem == "1":
        print()
        print("NO INTERNET - CHECKLIST")
        print("1. Check Wi-Fi or Ethernet connection.")
        print("2. Restart the router.")
        print("3. Restart the computer.")
        print("4. Check the IP configuration.")
        print("5. Test DNS or try another website.")

    elif problem == "2":
        print()
        print("SLOW COMPUTER - CHECKLIST")
        print("1. Check which programs are running.")
        print("2. Close unnecessary applications.")
        print("3. Check CPU and memory usage.")
        print("4. Check available storage space.")
        print("5. Restart the computer if necessary.")

    elif problem == "3":
        print()
        print("NO DISPLAY - CHECKLIST")
        print("1. Check that the monitor is powered on.")
        print("2. Check the display cable.")
        print("3. Make sure the correct input source is selected.")
        print("4. Try another cable or monitor if available.")
        print("5. Check the computer's display output.")

    elif problem == "4":
        print()
        print("WI-FI NOT SHOWING - CHECKLIST")
        print("1. Make sure Wi-Fi is enabled.")
        print("2. Check that Airplane Mode is off.")
        print("3. Check whether other Wi-Fi networks appear.")
        print("4. Restart the Wi-Fi adapter or computer.")
        print("5. Check the network adapter if the issue continues.")

    else:
        print("Problem not found.")

def networking_reference():
    print()
    print("------ NETWORKING QUICK REFERENCE ------")
    print()
    print("1. LAN vs WAN")
    print("2. TCP vs UDP")
    print("3. IPv4 vs IPv6")
    print("4. DNS vs DHCP")
    print("5. Wi-Fi Standards")
    print()

    topic = input("Choose a topic: ").strip()

    if topic == "1":
        print()
        print("------ LAN vs WAN ------")
        print("LAN = Local Area Network")
        print("Connects devices in a small area, like a home or office.")
        print("Example: Your laptop, phone, and printer connected to your home router.")
        print()
        print("WAN = Wide Area Network")
        print("Connects networks across large geographical areas.")
        print("Example: The Internet is the largest WAN.")

    elif topic == "2":
        print()
        print("------ TCP vs UDP ------")
        print("TCP = Transmission Control Protocol")
        print("Reliable and connection-oriented.")
        print("Checks that data arrives correctly and in order.")
        print("Example: Websites, email, and file downloads.")
        print()
        print("UDP = User Datagram Protocol")
        print("Faster but does not guarantee delivery.")
        print("Sends data without waiting for confirmation.")
        print("Example: Gaming, streaming, and VoIP calls.")

    elif topic == "3":
        print()
        print("------ IPv4 vs IPv6 ------")
        print("IPv4 = Internet Protocol version 4")
        print("Uses 32-bit addresses.")
        print("Example: 192.168.1.10")
        print()
        print("IPv6 = Internet Protocol version 6")
        print("Uses 128-bit addresses.")
        print("Example: 2001:db8::1")

    elif topic == "4":
        print()
        print("------ DNS vs DHCP ------")
        print("DNS = Domain Name System")
        print("Translates domain names into IP addresses.")
        print("Example: google.com -> IP address")
        print()
        print("DHCP = Dynamic Host Configuration Protocol")
        print("Automatically gives devices network settings.")
        print("Example: IP address, subnet mask, gateway, and DNS server.")

    elif topic == "5":
        print()
        print("------ WI-FI STANDARDS ------")
        print("802.11a  - 5 GHz")
        print("802.11b  - 2.4 GHz")
        print("802.11g  - 2.4 GHz")
        print("802.11n  - 2.4 GHz and 5 GHz (Wi-Fi 4)")
        print("802.11ac - 5 GHz (Wi-Fi 5)")
        print("802.11ax - 2.4 GHz and 5 GHz (Wi-Fi 6)")

    else:
        print("Topic not found.")
while True: 
          print("      SADIA'S IT TOOLKIT")
          print("    Python • IT • Networking")
          print("==============================")

          print()
          print("1. Port Lookup")
          print("2. DNS Record Helper")
          print("3. Bits & Bytes Converter")
          print("4. Troubleshooting Helper")
          print("5. Networking Quick Reference")
          print("0. Exit")

          print()

          choice = input("Choose a tool: ")

          if choice == "0":
               print ("thanks for using sadia's IT toolkit")
               break

          if choice == "1":
                port_lookup()
          
          
          elif choice == "2":
                dns_helper()
          

          elif choice == "3":  
                converter()    


          elif choice == "4":
               troubleshooting ()


          elif choice == "5":
              networking_reference()

          elif choice =="0":
              print ("thanks for using sadia's IT toolkit")
              break 
          else:
              print("Invalid choice")    