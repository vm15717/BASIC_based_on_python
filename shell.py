import excalibur

while True:
    text = input("excalibur>")
    print(f'The input is {text}')
    result, error = excalibur.run_excalibur(text)
    if error:
        print(str(error.as_string))
    else:
        print(result)
