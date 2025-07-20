#!/bin/bash  
# Substitua o email pelo seu email do GitHub  
ssh-keygen -t rsa -b 4096 -C "igor@igormedeiros.com.br"

# Inicia o ssh-agent em background  
eval "$(ssh-agent -s)"

# Adiciona sua chave SSH privada ao ssh-agent  
ssh-add ~/.ssh/id_rsa

# Exibe a chave pública para que você possa copiá-la  
echo "Copie a chave pública abaixo e cole nas configurações do seu GitHub:"  
cat ~/.ssh/id_rsa.pub