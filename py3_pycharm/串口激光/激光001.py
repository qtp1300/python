import serial
import time
import serial.tools.list_ports

port_list = serial.tools.list_ports.comports(include_links=True)

if     (len(port_list)) <= 0:
    print("没有找到串口")
else:
    port_num = str(len(port_list))
    print("找到" + port_num + "个串口");
    i = 0;
    while (i < len(port_list)):
        # print(port_list[i]);
        port_name = port_list[i][0];
        print(port_name);
        i = i + 1
# serial()
    com = serial.Serial(port_name, 115200);

# com = serial.Serial("COM6",115200);
    date_src = "$00022123&";
    data_encodeing = date_src.encode('utf-8')
    # print(data_encodeing);
    write_status = com.write(data_encodeing);
    # print(write_status);
    data_return = "";
    data_return = data_return.__add__(str(com.read_all())[3:][:-2])
    time.sleep(3);
    data_return = data_return.__add__(str(com.read_all())[3:][:-2])
    # print(data_return)
    data_return = data_return[19:]
    # print(data_return)
    print(data_return[0:2]+"."+data_return[3:]+"米")








com.close();



# serial.serialwin32(port_name,115200);

# print(serial.__version__)
# print(port_list[0]);