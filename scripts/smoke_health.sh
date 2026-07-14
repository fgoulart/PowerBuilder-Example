#!/usr/bin/env sh
set -eu
BASE_URL="${PUBLIC_API_URL:-http://localhost:8000}"
curl -sf "${BASE_URL}/api/v1/health" | tee /tmp/pb-health.json
echo
grep -q '"status"' /tmp/pb-health.json
