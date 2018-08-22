import zmq

def initialize_mq(host='127.0.0.1', port='5678'):
  context = zmq.Context()
  sock = context.socket(zmq.REP)
  sock.bind("tcp://{host}:{port}".format(host=host, port=port))
  return sock

def receive_message(sock):
  message = sock.recv()
  sock.send("received " + message)
  return message

def process_message(message):
  nums = message.split(" ")
  result = 0
  for num in nums:
    if num:
      result = result + int(num)
  print "result of summation is ", str(result)

def main():
  sock = initialize_mq()
  while True:
    message = receive_message(sock)
    #print "received", message
    process_message(message)

if __name__ == '__main__':
  main()
