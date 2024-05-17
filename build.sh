#!/usr/bin/env bash

sudo apt update; sudo apt install pipx; pipx ensurepath; pipx install poetry && poetry install