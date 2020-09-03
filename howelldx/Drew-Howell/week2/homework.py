import logging
logging.basicConfig(level=logging.DEBUG)

def squared_threes():
    return_value = []
    for i in range(1,100):
      if i%3 == 0:
        value = i*i
        return_value.append(value)
    return return_value

if __name__ == "__main__":
  for x in squared_threes():
       print(x)
