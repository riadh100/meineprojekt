"""
Erstellt Handels- und Systemberichte
für Yasin AI.
"""

from datetime import datetime
from pathlib import Path

import markdown
from jinja2 import Template
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
)
from reportlab.lib.styles import (
    getSampleStyleSheet,
)

from app.database.session import SessionLocal
from app.models.statistics import Statistics


REPORT_DIR = Path("reports")


def load_statistics():

    db = SessionLocal()

    try:

        return db.query(
            Statistics
        ).all()

    finally:

        db.close()


def generate_markdown(data):

    REPORT_DIR.mkdir(
        exist_ok=True
    )

    file = REPORT_DIR / (
        f"report_{datetime.utcnow():%Y%m%d}.md"
    )

    lines = [
        "# Yasin AI Report",
        "",
        f"Erstellt: {datetime.utcnow()}",
        "",
        "| Markt | Trades | Winrate | Profit Factor |",
        "|-------|--------|---------|---------------|",
    ]

    for item in data:

        lines.append(
            f"| {item.market} | "
            f"{item.total_trades} | "
            f"{item.win_rate}% | "
            f"{item.profit_factor} |"
        )

    file.write_text(
        "\n".join(lines),
        encoding="utf-8",
    )

    return file


def generate_html(markdown_file):

    REPORT_DIR.mkdir(
        exist_ok=True
    )

    html = markdown.markdown(
        markdown_file.read_text(
            encoding="utf-8"
        )
    )

    template = Template("""
    <html>
      <head>
        <title>Yasin AI Report</title>
      </head>
      <body>
        {{ content }}
      </body>
    </html>
    """)

    output = REPORT_DIR / "report.html"

    output.write_text(
        template.render(
            content=html
        ),
        encoding="utf-8",
    )

    return output


def generate_pdf(data):

    REPORT_DIR.mkdir(
        exist_ok=True
    )

    file = REPORT_DIR / "report.pdf"

    styles = getSampleStyleSheet()

    document = SimpleDocTemplate(
        str(file)
    )

    elements = [
        Paragraph(
            "Yasin AI Report",
            styles["Heading1"],
        )
    ]

    for item in data:

        elements.append(
            Paragraph(
                (
                    f"{item.market}: "
                    f"{item.total_trades} Trades | "
                    f"Winrate {item.win_rate}%"
                ),
                styles["BodyText"],
            )
        )

    document.build(elements)

    return file


def main():

    print("=" * 60)
    print("YASIN AI REPORT GENERATOR")
    print("=" * 60)

    statistics = load_statistics()

    md = generate_markdown(
        statistics
    )

    html = generate_html(md)

    pdf = generate_pdf(
        statistics
    )

    print(f"Markdown: {md}")
    print(f"HTML: {html}")
    print(f"PDF: {pdf}")

    print()

    print(
        "Berichte erfolgreich erstellt."
    )


if __name__ == "__main__":

    main()
