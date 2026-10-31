
import html
import streamlit as st


def render_result_card(label, value, unit=""):
    """Display one calculation result."""

    safe_label = html.escape(str(label))
    safe_value = html.escape(str(value))
    safe_unit = html.escape(str(unit))

    st.markdown(
        f"""
        <div class="cw-result">
            <div class="cw-result-label">
                {safe_label}
            </div>
            <div class="cw-result-value">
                {safe_value}
                <span style="
                    font-size: 0.9rem;
                    font-weight: 500;
                ">
                    {safe_unit}
                </span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_result_table(rows):
    """Display a themed HTML table from trusted result records."""

    if not rows:
        st.info("No results to display.")
        return

    headers = list(rows[0].keys())

    header_html = "".join(
        f"<th>{html.escape(str(header))}</th>"
        for header in headers
    )

    body_html = ""

    for row in rows:
        cells = "".join(
            f"<td>{html.escape(str(row.get(header, '')))}</td>"
            for header in headers
        )

        body_html += f"<tr>{cells}</tr>"

    st.markdown(
        f"""
        <table class="cw-table">
            <thead>
                <tr>{header_html}</tr>
            </thead>
            <tbody>
                {body_html}
            </tbody>
        </table>
        """,
        unsafe_allow_html=True,
    )
