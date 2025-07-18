#!/bin/bash

# Atualiza os pacotes e instala o Zsh
sudo apt update
sudo apt install -y zsh

# Define o Zsh como o shell padrão para o usuário atual
# Pode ser necessário inserir a senha aqui, dependendo das permissões do sudo
sudo usermod -s /usr/bin/zsh $(whoami)

# Instala o Oh My Zsh sem iniciar um novo shell
export RUNZSH=no
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended

# Clona os plugins do zsh-syntax-highlighting e zsh-autosuggestions
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions

# Edita a linha de plugins no ~/.zshrc usando sed
sed -i 's/^plugins=(.*/plugins=(git zsh-syntax-highlighting zsh-autosuggestions)/' ~/.zshrc

source ~/.zshrc

echo "Instalação e configuração do Zsh e Oh My Zsh concluídas!"
echo "Por favor, reinicie seu terminal ou faça logout e login para que as alterações entrem em vigor."

# Inicia uma nova sessão Zsh para aplicar as alterações (opcional)
exec zsh
