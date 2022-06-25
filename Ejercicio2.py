total_neto_a_pagar = float(input("Ingresa el total a pagar: "))
personas_juntas = int(input("Ingresa el numero de personas a dividir la cuenta: "))
porcenta_propina = int(input("Ingresa el porcentaje de propina: "))
porcenta_impuesto = int(input("Ingresa el porcentaje de impuesto: "))

total_a_pagar = total_neto_a_pagar + ((porcenta_impuesto * total_neto_a_pagar)/100) + \
    ((porcenta_propina * total_neto_a_pagar)/100)

pago_por_persona = total_a_pagar / personas_juntas

print(f"""El total a pagar es: {total_a_pagar}.
El pago por persona es: {pago_por_persona}""")