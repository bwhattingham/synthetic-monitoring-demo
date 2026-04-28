Synthetic Monitoring Simulation

This project is a public, safe simulation of the synthetic monitoring pipelines I’ve built using Datadog and internal monitoring tools.
It does not contain any proprietary code or configuration — only the concepts.

🧠 What This Demonstrates
How synthetic tests work
Why global latency monitoring matters
How to design a monitoring pipeline
How to think about reliability and user experience
How to document technical workflows clearly

📡 Example Use Case
This simulation mirrors the structure of a real project where I monitored latency across multiple regions using a public JSON endpoint.

📁 Project Structure
synthetic-monitoring-demo/
│
├── README.md
├── synthetic-test.json
├── fake-api/
│   ├── response.json
│   └── server.py
└── dashboards/
└── example-dashboard.json

🚀 Running the Fake API
This mock API simulates a latency endpoint.
Start the server:
python3 fake-api/server.py
Then visit:
http://localhost:5000/latency
You’ll see a JSON response with a random latency value.

📝 Notes
This repo focuses on:
Concepts
Documentation
Monitoring mindset
DevRel‑style explanation
No internal systems or data are included.


