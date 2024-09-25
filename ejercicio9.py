from scapy.all import *

def analyze_packet(packets):
    cadena = []
    
    for pkt in packets:
        try:
            if pkt.haslayer(ICMP) and pkt[ICMP].type == 8:
                # Extraer la carga útil (Raw data)
                if pkt.haslayer(Raw):
                    data = pkt[Raw].load
                    # Obtener el primer byte
                    first_byte = data[0]
                    cadena.append(chr(first_byte)) 
                    
        except (IndexError, AttributeError) as e:
            pass

    return ''.join(cadena)

pcap_file = r"icmprequest.pcapng"
packets = rdpcap(pcap_file)


result_cadena = analyze_packet(packets)
print(f"Bytes: {result_cadena}")
