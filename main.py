from flask import Flask, render_template, request, send_file
import agents.discovery_agent as discovery_agent
import agents.scraper_agent as scraper_agent
import agents.extractor_agent as extractor_agent
import agents.cleaner_agent as cleaner_agent
import agents.qa_agent as qa_agent
import pandas as pd
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    csv_ready = False

    if request.method == "POST":
        theme = "AI News"   # For hackathon demo, fixed theme
        print(f"[INFO] Running agents for theme: {theme}")

        # Run agent pipeline
        urls = discovery_agent.run(theme)
        htmls = scraper_agent.run(urls)
        extracted_data = extractor_agent.run(htmls)
        cleaned_df = cleaner_agent.run(extracted_data)
        final_df = qa_agent.run(cleaned_df)

        os.makedirs("data", exist_ok=True)
        output_filename = "data/output.csv"
        final_df.to_csv(output_filename, index=False)
        csv_ready = True

    return render_template("index.html", csv_ready=csv_ready)

@app.route("/download")
def download_csv():
    return send_file("data/output.csv", as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=81)

