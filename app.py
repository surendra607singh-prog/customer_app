import streamlit as st
import pandas as pd

st.set_page_config(page_title="Complaint Search", layout="centered")

st.title("📞 Complaint Search App")

uploaded_file = st.file_uploader("📂 Upload Complaint Sheet", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file, header=None)
    df = df.astype(str).apply(lambda x: x.str.strip())
    df = df[~df.eq("nan").all(axis=1)]

    contact = st.text_input("🔍 Enter Contact Number")

    if contact:
        mask = df.apply(lambda row: row.str.contains(contact, na=False).any(), axis=1)
        result = df[mask]

        if result.empty:
            st.error("❌ No customer found")
        else:
            customer = result.iloc[0]
            st.success("✅ CUSTOMER DETAILS")

            fields = {
                "📄 Doc No": customer[2],
                "👤 Name": customer[3],
                "📞 Contact": customer[4],
                "🏠 Address": customer[5],
                "📮 Pin Code": customer[7],
                "🔧 Product": customer[8],
                "🏷 Make": customer[9],
                "👨‍🔧 Technician": customer[12],
                "💰 Bill Amount": customer[11],
            }

            for k, v in fields.items():
                if v and v.lower() != "nan":
                    st.write(f"**{k}:** {v}")
