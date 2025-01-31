# ~/.bashrc: executed by bash(1) for non-login shells.
# See /usr/share/doc/bash/examples/startup-files for examples.
# To customize this file, edit it and run `source ~/.bashrc` to apply changes.

alias ll='ls -la --color=auto'
alias grep='grep --color=auto'
alias ip='ip -c'
alias cls='clear'
alias cls='reset'

PS1='[\u@\h \W]\$ '

echo "Welcome back, Samy!"

export PATH=$PATH:$HOME/bin:$HOME/tools:$HOME/scripts

export LS_COLORS='di=1;34:ln=1;36:so=1;35:pi=1;33:ex=1;32'

HISTSIZE=10000
HISTFILESIZE=20000
shopt -s histappend

bind 'set completion-ignore-case on'

search_tool() {
    if command -v $1 &> /dev/null
    then
        echo "$1 is installed in $(which $1)"
    else
        echo "$1 is not found"
    fi
}

update_system() {
    sudo apt update && sudo apt upgrade -y
}

if [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
fi


# Display the current Kali version
alias kali_version='cat /etc/os-release | grep VERSION'

# Enable command history search with arrow keys
bind '"\e[A": history-search-backward'
bind '"\e[B": history-search-forward'
