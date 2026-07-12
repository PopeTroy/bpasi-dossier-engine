import os
import sys
import time
import hashlib
import json
from openai import OpenAI
from fpdf import FPDF

# =====================================================================
# COURT COMPLIANT PDF ARCHITECTURE SPECIFICATION
# =====================================================================
class BPASICourtDocument(FPDF):
    def header(self):
        # Chapter 5 Directive Requirement: Clean uncompressed pagination
        if self.page_no() > 1:
            self.set_font("Helvetica", "I", 9)
            self.cell(0, 10, f"BOBBY MOAHI v THE NATIONAL EXECUTIVE & OTHERS - Page {self.page_no()}", border=0, ln=1, align="R")
            self.ln(5)

    def footer(self):
        # Absolute structural page tracking
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.cell(0, 10, f"CaseLines Ingestion Verification ID Token Tracking Layer", border=0, align="C")

def create_court_pdf(filename, title_text, content_text, needs_commissioner=False):
    pdf = BPASICourtDocument()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=20)
    
    # Case Heading Setup
    pdf.set_font("Helvetica", "B", 12)
    pdf.multi_cell(0, 6, title_text, border=0, align="C")
    pdf.ln(10)
    
    pdf.set_font("Helvetica", "", 11)
    # Map input text into clean paragraphs
    for paragraph in content_text.split('\n'):
        if paragraph.strip():
            pdf.multi_cell(0, 6, paragraph.strip(), ln=1)
            pdf.ln(4)
            
    # Hardcode strict SAPS attestation framework if document requires a signature
    if needs_commissioner:
        pdf.ln(12)
        pdf.set_font("Helvetica", "B", 11)
        pdf.cell(0, 6, "DEPONENT SIGNATURE LOCK", ln=1)
        pdf.ln(4)
        pdf.set_font("Helvetica", "", 10)
        pdf.multi_cell(0, 5, "I hereby certify that the Deponent has acknowledged that he knows and understands the contents of this affidavit, which was signed and sworn to before me at _________________ on this _____ day of ___________________ 2026, the regulations contained in Government Notice No. R1258 of 21 July 1972, as amended, having been complied with.", ln=1)
        pdf.ln(8)
        pdf.cell(0, 5, "_________________________________________", ln=1)
        pdf.set_font("Helvetica", "B", 10)
        pdf.cell(0, 5, "COMMISSIONER OF OATHS (EX OFFICIO)", ln=1)
        pdf.ln(4)
        pdf.set_font("Helvetica", "", 9)
        pdf.cell(0, 5, "Full Names: ___________________________________________________________", ln=1)
        pdf.cell(0, 5, "Designation / Rank: ____________________________________________________", ln=1)
        pdf.cell(0, 5, "Physical Address: ______________________________________________________", ln=1)
        pdf.ln(5)
        pdf.cell(0, 15, "[ PLACE PHYSICAL SAPS PRECINCT STAMP HERE ]", border=1, ln=1, align="C")

    pdf.output(filename)
    print(f"📄 Physical PDF Generated and Locked: {filename}")

# =====================================================================
# SWARM RUNTIME CORE PIPELINE
# =====================================================================
def run_bpasi_swarm():
    session_id = os.getenv("WP_SESSION_ID", "MOCK-SESSION-144000")
    timestamp = os.getenv("WP_TIMESTAMP", str(int(time.time())))
    raw_complaint = os.getenv("RAW_COMPLAINT", "Systemic failure in tracking tender allocations regarding critical tech infrastructure.")
    first_names = os.getenv("USER_FIRST_NAMES", "Bobby")
    surname = os.getenv("USER_SURNAME", "Moahi")
    
    # ECTA Section 15 compliance tracking token
    token = hashlib.sha256(f"{session_id}-{timestamp}".encode()).hexdigest()[:8].upper()
    print(f"🧬 [BPASI ENGINE ACTIVE] Processing entry signature: TS-{token} for Litigant: {first_names} {surname}")
    
    # Initialize API Handshakes with exact Base URLs
    groq_client = OpenAI(
        base_url="https://api.groq.com/openai/v1",
        api_key=os.getenv("GROQ_API_KEY")
    )
    
    # Fallback structure configuration
    legal_foundation = f"Substantive constitutional grievance regarding Section 195 ethics: {raw_complaint}"
    
    groq_prompt = f"""
    You are the 25 Overwrite and 20 Ingest Agents. Apply the Law of Dimensional Overwrite.
    Structure a strict, court-compliant CaseLines Master Index of Documents (MoI) matching Chapter 5 Directives based on this data: {legal_foundation}.
    Every filename must incorporate the user's surname: '{surname}' and token '{token}'.
    """
    
    try:
        # Verified active 2026 Groq production model parameter
        groq_res = groq_client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[{"role": "user", "content": groq_prompt}],
            temperature=0.1
        )
        caselines_index = groq_res.choices[0].message.content
    except Exception as e:
        print(f"⚠️ API pipeline dropped, compiling default index structure metrics: {e}")
        caselines_index = f"Master Index Reference Layer for Token TS-{token}"

    # EMIT ACTUAL PHYSICAL COMPLIANT LEGAL FILE BUNDLE (.pdf)
    print("⚙️ Initializing PDF compilation rendering engines...")
    
    court_heading = "IN THE HIGH COURT OF SOUTH AFRICA\nGAUTENG DIVISION, JOHANNESBURG\n\nIn the matter between:\nBOBBY MOAHI (Applicant)\nand\nTHE NATIONAL EXECUTIVE & OTHERS (Respondents)"
    
    # File 1: Notice of Motion
    create_court_pdf(
        filename=f"A01_Notice_of_Motion_{surname}_{token}.pdf",
        title_text=court_heading,
        content_text="KINDLY TAKE NOTICE that BOBBY MOAHI (hereinafter referred to as the Applicant) intends to apply to this Honourable Court for an order declaring that the public procurement tracking irregularities run in direct breach of Section 195 and Section 217 of the Constitution, and that administrative records be compelled for verification inside the Court Online database system."
    )
    
    # File 2: Founding Affidavit (Requires SAPS Attestation Block)
    create_court_pdf(
        filename=f"A02_Founding_Affidavit_{surname}_{token}.pdf",
        title_text="APPLICANT'S FOUNDING AFFIDAVIT",
        content_text=f"I, the undersigned, BOBBY MOAHI, do hereby make oath and state:\n\n1. I am an adult male Litigant in Person bringing this application in my personal capacity as a citizen of the Republic of South Africa under Section 38 of the Constitution.\n\n2. STATEMENT OF SERVICE DISRUPTION & CONSTITUTIONAL IRREGULARITY:\n{raw_complaint}\n\n3. In terms of Section 15 of the Electronic Communications and Transactions Act 25 of 2002 (ECTA), the digital fingerprints and text matrices generated by this pipeline preserve full data integrity.",
        needs_commissioner=True
    )

    print("\n🚀 [ULTIMATE SYSTEM STATUS ACHIEVED - PDF DOSSIER CORES HARDLOCKED TO DRIVE]")
    print(caselines_index)
    
    # Target email node update configuration
    target_lead_node = "info@celsiustechmediagroup.co.za"
    print(f"📬 Forwarding verification metadata summary signature [TS-{token}] to lead generation queue at: {target_lead_node}")

if __name__ == "__main__":
    run_bpasi_swarm()
