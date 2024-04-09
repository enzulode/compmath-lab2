def is_float(data: str):
  try:
    float(data)
    return True
  except ValueError:
    return False

def check_input_is_float(text, action):
  return action != '1' or is_float(text) or text == '-'
