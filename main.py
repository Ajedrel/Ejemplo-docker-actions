import os
import random

def set_action_output(output_name, output_value):
    with open(os.path.abspath(os.environ["GITHUB_OUTPUT"]), "a") as output:
        print(f"{output_name}={output_value}", file=output)

def run():
    valor2 = None
    numero = os.getenv('INPUT_NOMBRE', default="uno")
    numero = numero.lower()
    valor = random.randint(1, 6)
    if numero == 'dos':
        valor2 = random.randint(1, 6)
    mensaje = f"Valor: {valor}    {valor2}"
    set_action_output('valores', f'Valores, {mensaje}')

if __name__ == '__main__':
    run()