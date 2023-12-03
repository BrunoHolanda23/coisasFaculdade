import socket

def main():
    # Cria um soquete de rede
    sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(ETH_P_ALL))

    # Inicia a captura de pacotes
    sock.bind(('', 0))

    # Analisa os pacotes capturados
    while True:
        # Recebe um pacote
        data, _ = sock.recvfrom(65535)

        # Analisa o cabeçalho do pacote
        eth_header = data[:14]
        eth_type = eth_header[0:2]

        # Se o tipo de pacote for Ethernet II
        if eth_type == b'0800':
            # Analisa o cabeçalho do IP
            ip_header = data[14:20]
            ip_version = ip_header[0]
            ip_header_length = ip_header[1] & 0xf
            ip_source_address = ip_header[2:6]
            ip_destination_address = ip_header[6:10]

            # Se o pacote for DHCPDISCOVER
            if ip_protocol == ord(ip_header[0]):
                # Analisa o cabeçalho do DHCP
                dhcp_header = data[20:44]
                dhcp_message_type = dhcp_header[0]
                dhcp_client_mac = dhcp_header[2:10]

                # Exibe os resultados da análise
                print("IP: %s" % str(ip_source_address))
                print("MAC: %s" % dhcp_client_mac)

if __name__ == '__main__':
    main()
