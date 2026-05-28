#!/usr/bin/env bash
# User-local runtime for invoke-cursor-agent (no sudo).
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT}"

if ! command -v node >/dev/null 2>&1; then
  export NVM_DIR="${HOME}/.nvm"
  if [[ ! -s "${NVM_DIR}/nvm.sh" ]]; then
    echo "Installing nvm to ${NVM_DIR}..."
    curl -fsSL https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash
  fi
  # shellcheck disable=SC1091
  source "${NVM_DIR}/nvm.sh"
  nvm install 20
  nvm alias default 20
  ln -sfn "$(nvm version default | tr -d v | xargs -I{} echo "v{}")" "${NVM_DIR}/versions/node/default" 2>/dev/null \
    || ln -sfn "$(ls -1 "${NVM_DIR}/versions/node" | tail -1)" "${NVM_DIR}/versions/node/default"
fi

echo "Node: $(node --version)"
npm install

if [[ ! -d "${ROOT}/.venv" ]]; then
  python3 -m venv "${ROOT}/.venv"
fi
"${ROOT}/.venv/bin/pip" install -r requirements.txt
echo "Python venv ready: ${ROOT}/.venv"
