UART_SET = 0x01
UART_GET = 0x03

UART_RESPONSE = 0x02
UART_ACK_RESPONSE = 0xFF

UART_BAD_CMD_RESPONSE = 0xFc
UART_BAD_ARG_RESPONSE = 0xFD
UART_BAD_CRC_RESPONSE = 0xFE

CRC_INIT = 0xB0CA
START_CHAR = 0x24

UART_COMP_SHIMMER = 0x01
UART_COMP_BAT = 0x02
UART_COMP_DAUGHTER_CARD = 0x03
UART_COMP_D_ACCEL = 0x04
UART_COMP_GSR = 0x05

UART_PROP_ENABLE = 0x00
UART_PROP_SAMPLE_RATE = 0x01
UART_PROP_MAC = 0x02
UART_PROP_VER = 0x03
UART_PROP_RWC_CFG_TIME = 0x04
UART_PROP_CURR_LOCAL_TIME = 0x05
UART_PROP_INFOMEM = 0x06
UART_PROP_CARD_ID = 0x02