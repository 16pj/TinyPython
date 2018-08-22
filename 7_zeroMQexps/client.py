import zmq
import sys

def initialize_mq(host='127.0.0.1', port='5678'):
  context = zmq.Context()
  sock = context.socket(zmq.REQ)
  sock.connect("tcp://127.0.0.1:5678")
  return sock

def send_message(sock, message):
  sock.send(message)
  print sock.recv()

def create_message():
  message = ' '.join(sys.argv[1:])
  return message

if __name__ == '__main__':
  sock = initialize_mq()
  message = create_message()
  send_message(sock, message)
