import excalibur

while True:
    text = input("excalibur>")
    result, error = excalibur.run_excalibur('<stdin>', text)
    if error:
        print(str(error.as_string()))
    else:
        print(result)
