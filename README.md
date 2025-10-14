# 🏦 PyUnit – Projeto de Conta Bancária com Testes e API

![Build Status](https://github.com/rubenmorais/PyUnit/actions/workflows/tests.yml/badge.svg)
![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)
![Python](https://img.shields.io/badge/python-3.12-blue)

## 📌 Descrição

Projeto implementa uma classe `ContaBancaria` em Python, com operações de depósito, levantamento e transferência, usando:
- tratamento de exceções personalizadas (`ValorInvalidoError`, `SaldoInsuficienteError`)
- testes unitários com **unittest** (PyUnit)
- API HTTP em **Flask**
- integração contínua (**CI**) via **GitHub Actions**
- cobertura de testes e métricas de tempo de execução

---

## 🚀 Tecnologias usadas

| Ferramenta / Biblioteca | Utilidade |
|--------------------------|-----------|
| Python 3.12 | Linguagem principal |
| Flask | API web para interagir com contas |
| unittest / PyUnit | Framework de testes unitários |
| coverage.py | Medição de cobertura de código |
| GitHub Actions | Execução automática de testes no push / pull request |
| logging | Registo de eventos e operações |

---

## 🧪 Executar testes

```bash
pip install -r requirements.txt
coverage run -m unittest discover
coverage report -m
