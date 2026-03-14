#!/bin/bash
# AgentStack monitoring loop
while true; do
  python3 /root/.openclaw/workspace/AgentStack/scripts/monitor.py >> /root/.openclaw/workspace/AgentStack/logs.txt 2>&1
  sleep 600
done
