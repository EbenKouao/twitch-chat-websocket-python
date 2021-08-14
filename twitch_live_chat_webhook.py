import socket
from emoji import demojize
import time
import datetime
import auth_credentials as auth


# auth_credentials - Get OAUTH https://twitchapps.com/tmi/
twitch_server = auth.twitch_server
port = auth.port
twitch_auth_username = auth.twitch_auth_username
twitch_oauth = auth.twitch_oauth
twitch_live_channel_name = auth.twitch_live_channel_name

print(twitch_server)
print(port)
print(twitch_auth_username)
print(twitch_oauth)
print(twitch_live_channel_name)

def get_timestamp_date(timestamp):
    t = time.localtime()
    current_time = time.strftime("%Y-%m-%dT%H:%M:%S.000Z", t)
    # print(current_time)
    return current_time

def main():
    sock = socket.socket()
    sock.connect((twitch_server, int(port)))
    sock.send(f"PASS {twitch_oauth}\r\n".encode('utf-8'))
    sock.send(f"NICK {twitch_auth_username}\r\n".encode('utf-8'))
    sock.send(f"JOIN {twitch_live_channel_name}\r\n".encode('utf-8'))

    try:
        while True:

            resp = sock.recv(2048).decode('utf-8')
            if resp.startswith('PING'):
                sock.send("RECIEVED\n".encode('utf-8'))
            elif len(resp) > 0:
                
                #strip emoji from message
                resp_demoji = demojize(resp).split(":")
                # print(resp_demoji)
                
                #twitch username
                username_split = resp_demoji[1].split("!")
                twitch_username = username_split[0].replace("\r\n","")
                # print(twitch_username)

                #twitch message
                chat_message = resp_demoji[2].replace("\r\n","")
                # print(chat_message)
                # print(messages)

                print(f"Twitch Username: {twitch_username} ---> said: {chat_message}")


    except KeyboardInterrupt:
        sock.close()
        exit()

if __name__ == '__main__':
    print("********Started TWTICH_SERVER********")
    print("======================================")
    main()