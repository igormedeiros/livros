@echo off
REM Navega para o diretório do exercício
pushd %~dp0

REM Executa o script Python
python main.py

REM Retorna ao diretório original
popd