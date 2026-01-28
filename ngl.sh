#!/bin/bash

##############################################
#               HELP
##############################################
show_help() {
    cat << EOF
Usage: $0 [OPTIONS] [ARGUMENTS]

Options:
    -h, --help                   Display this help message.
EOF
}

##############################################
#         OPTION PROCESSING
##############################################
case "$1" in
    -h|--help)
        show_help
        ;;
    -r|--run)
        python src/main.py "$@"
        ;;
    *)
        echo "❌ Unknown option: $1"
        echo ""
        show_help
        exit 1
        ;;
esac
