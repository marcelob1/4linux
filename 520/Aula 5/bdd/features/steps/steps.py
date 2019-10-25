#!/usr/bin/python3

from behave import step

def soma(num1,num2):
    return num1 + num2

@when('somar "{num1}" com "{num2}"')
def test_soma(context,num1,num2):
    context.r_soma = soma(int(num1), int(num2))

@then('O resultado deve ser "{esperado}"')
    test_some_result(context, esperado):
    assert context.r_soma == int(esperado), "Erro"