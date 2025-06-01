"""
AI Smart Helper for Fixing IT Problems Fast

This script simulates a smart AI helper system for IT ticket management, featuring three agents: Watcher, ProblemSolver, and Learner. It demonstrates how incoming tickets are monitored, patterns are detected, urgent issues are escalated, and the system learns over time.
"""

from typing import List, Dict, Any
from collections import defaultdict, Counter
import time
import random

# Simulated ticket structure
ticket_id_counter = 1

def generate_ticket(issue_type, user, description):
    global ticket_id_counter
    ticket = {
        'id': ticket_id_counter,
        'type': issue_type,
        'user': user,
        'description': description,
        'timestamp': time.time(),
        'status': 'open'
    }
    ticket_id_counter += 1
    return ticket

# The Watcher: Monitors all tickets and spots patterns
class Watcher:
    def __init__(self):
        self.history = []
        self.patterns = defaultdict(list)

    def observe(self, ticket):
        self.history.append(ticket)
        self.patterns[ticket['type']].append(ticket)
        return self.detect_anomaly(ticket)

    def detect_anomaly(self, ticket):
        # Example: If more than 5 tickets of the same type in 1 minute, flag as anomaly
        recent = [t for t in self.patterns[ticket['type']] if time.time() - t['timestamp'] < 60]
        if len(recent) > 5:
            return True, f"Pattern detected: {len(recent)} '{ticket['type']}' tickets in 1 minute."
        return False, None

# The Problem Solver: Escalates, alerts, and auto-resolves simple issues
class ProblemSolver:
    def __init__(self):
        self.urgent_queue = []
        self.alerts = []

    def handle(self, ticket, anomaly, message):
        if anomaly:
            self.urgent_queue.append(ticket)
            self.alerts.append(f"ALERT: {message} (Ticket ID: {ticket['id']})")
            print(f"[ALERT] {message} (Ticket ID: {ticket['id']})")
        elif ticket['type'] == 'password_reset':
            ticket['status'] = 'resolved'
            print(f"[AUTO-RESOLVED] Ticket {ticket['id']} (Password reset)")
        else:
            print(f"[QUEUED] Ticket {ticket['id']} queued for IT team.")

# The Learner: Remembers what worked and improves detection
class Learner:
    def __init__(self):
        self.resolved_patterns = Counter()

    def learn(self, ticket, anomaly):
        if anomaly:
            self.resolved_patterns[ticket['type']] += 1
            print(f"[LEARNER] Learned from anomaly: {ticket['type']}")

# Simulate incoming tickets and AI helper workflow
def simulate_tickets():
    watcher = Watcher()
    solver = ProblemSolver()
    learner = Learner()

    # Simulate a stream of tickets
    issues = [
        ('login_issue', 'user1', 'Cannot log in'),
        ('login_issue', 'user2', 'Login failed'),
        ('login_issue', 'user3', 'Stuck at login'),
        ('password_reset', 'user4', 'Forgot password'),
        ('login_issue', 'user5', 'Login not working'),
        ('login_issue', 'user6', 'Login error'),
        ('website_slow', 'user7', 'Website is slow'),
        ('website_slow', 'user8', 'Page takes long to load'),
        ('website_slow', 'user9', 'Slow response'),
        ('critical_system_down', 'user10', 'System not responding'),
    ]

    for issue_type, user, desc in issues:
        ticket = generate_ticket(issue_type, user, desc)
        anomaly, message = watcher.observe(ticket)
        solver.handle(ticket, anomaly, message)
        learner.learn(ticket, anomaly)
        time.sleep(0.5)  # Simulate time between tickets

    print("\n[SUMMARY] Resolved patterns:")
    for k, v in learner.resolved_patterns.items():
        print(f"  {k}: {v} times")

if __name__ == "__main__":
    print("Starting AI Smart Helper simulation...")
    simulate_tickets()
    print("Simulation complete.")
