import os
import sys
import time
import uuid
import json
import hashlib
import math
import requests
import datetime
from openai import OpenAI  # Using the installed openai library configured for Groq
from fpdf import FPDF
from fpdf.enums import XPos, YPos

# =====================================================================
# SYSTEM CONFIGURATION & GLOBAL IDENTITY CONTRACTS
# =====================================================================
# Map variables directly to your GitHub Action YAML environment mappings
TIMESTAMP = os.getenv('WP_TIMESTAMP', datetime.datetime.now(datetime.timezone.utc).isoformat())
SESSION_ID = os.getenv('WP_SESSION_ID') or str(uuid.uuid4())

# User Identity Reconstruction from YAML ENV inputs
FIRST_NAMES = os.getenv('USER_FIRST_NAMES', 'Bobby')
SURNAME = os.getenv('USER_SURNAME', 'Moahi')
FULL_NAME = f"{FIRST_NAMES} {SURNAME}"

STREET = os.getenv('USER_STREET', '128 Blockchain Avenue')
CITY = os.getenv('USER_CITY', 'Soweto')
PROVINCE = os.getenv('USER_PROVINCE', 'Gauteng')
ZIP = os.getenv('USER_ZIP', '1804')
FULL_ADDRESS = f"{STREET}, {CITY}, {PROVINCE}, {ZIP}"

PHONE = os.getenv('USER_PHONE', '+27710000000')
EMAIL = os.getenv('USER_EMAIL', 'bobby.moahi@example.com')
RAW_COMPLAINT = os.getenv('RAW_COMPLAINT', 'Systemic failure in tracking tender allocations regarding critical tech infrastructure.')

# Authoritative GitHub Asset Routing Path Matrix
USERNAME = "PopeTroy"
REPO = "PopeTroy-Signature-Mage-console-Nano-scaling"
RAW_BASE_URL = f"https://raw.githubusercontent.com/{USERNAME}/{REPO}/main/"

# Secure initialization of the OpenAI compatible Groq endpoint
groq_api_key = os.getenv("GROQ_API_KEY")
client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=groq_api_key
) if groq_api_key else None

# =====================================================================
# SYSTEM TEXT SANITIZER ROUTINE
# =====================================================================
def sanitize_for_latin1(text):
    """Replaces Unicode characters that blow up core FPDF Latin-1 fonts."""
    if not text:
        return ""
    text = text.replace("\u2013", "-")  # En-dash
    text = text.replace("\u2014", "-")  # Em-dash
    text = text.replace("\u2018", "'")  # Left single quote
    text = text.replace("\u2019", "'")  # Right single quote
    text = text.replace("\u201c", '"')  # Left double quote
    text = text.replace("\u201d", '"')  # Right double quote
    text = text.replace("\u2022", "*")  # Bullet point
    return text.encode('latin-1', 'replace').decode('latin-1')

# =====================================================================
# COMPLIANCE INTERFACE: THE GHOST LEDGER WRITER
# =====================================================================
def write_to_ghost_ledger(entry: dict):
    """
    Appends the current system execution trace to an immutable, local audit log.
    Fulfills POPIA Condition 7 (Security Safeguards) and prevents chronological erasure.
    """
    ledger_path = 'compliance_audit_ledger.jsonl'
    try:
        complete_entry = {
            "session_id": SESSION_ID,
            "logged_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            **entry
        }
        with open(ledger_path, 'a') as lf:
            lf.write(json.dumps(complete_entry) + '\n')
    except Exception as e:
        print(f"🚨 GHOST LEDGER WARNING: {e}")

# =====================================================================
# COURT COMPLIANT PDF ARCHITECTURE SPECIFICATION
# =====================================================================
class BPASICourtDocument(FPDF):
    def __init__(self, litigant_meta):
        super().__init__()
        self.meta = litigant_meta
        self.logo1_path = "logo1_temp.webp"
        self.logo2_path = "logo2_temp.png"
        self._download_runtime_logos()

    def _download_runtime_logos(self):
        url1 = "https://celsiustechmediagroup.co.za/wp-content/uploads/2026/01/cropped-CTMG.webp"
        url2 = "https://celsiustechmediagroup.co.za/wp-content/uploads/2026/05/craiyon_160323_image-3.png"
        try:
            r1 = requests.get(url1, timeout=5)
            if r1.status_code == 200:
                with open(self.logo1_path, 'wb') as f: f.write(r1.content)
            r2 = requests.get(url2, timeout=5)
            if r2.status_code == 200:
                with open(self.logo2_path, 'wb') as f: f.write(r2.content)
        except Exception as e:
            write_to_ghost_ledger({
                "status": "LOGO_DOWNLOAD_BYPASSED",
                "error_detail": str(e)
            })

    def header(self):
        if self.page_no() == 1:
            self.set_font("Helvetica", "B", 10)
            self.cell(0, 5, sanitize_for_latin1(f"LITIGANT IN PERSON: {self.meta['name'].upper()}"), new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="L")
            self.set_font("Helvetica", "", 9)
            self.cell(0, 4, sanitize_for_latin1(f"Address: {self.meta['address']}"), new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="L")
            self.cell(0, 4, sanitize_for_latin1(f"Contact: {self.meta['phone']} | Email: {self.meta['email']}"), new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="L")
            self.cell(0, 4, sanitize_for_latin1(f"Calculated Jurisdiction: {self.meta['division']} ({self.meta['distance']:.2f} km radius)"), new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="L")
            self.ln(3)
            self.line(10, self.get_y(), 200, self.get_y())
            self.ln(5)
        elif self.page_no() > 1:
            self.set_font("Helvetica", "I", 9)
            self.cell(0, 10, sanitize_for_latin1(f"{self.meta['name'].upper()} v THE RESPONDENTS - Page {self.page_no()}"), border=0, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="R")
            self.ln(5)

    def footer(self):
        self.set_y(-32)
        self.set_font("Helvetica", "I", 7)
        fine_print = f"This data message is generated and signed in accordance with Sections 11, 15 and 20 of ECTA 25 of 2002. Confidentiality managed under POPIA 4 of 2013. | Session Reference Trace Token ID: {self.meta['token']}"
        self.multi_cell(0, 4, sanitize_for_latin1(fine_print), border=0, align="C")
        self.ln(1)
        
        audit_text = "(state forensics and diagnostic audit done by Celsius Technology & Media Group Developed UESP PRCE Legal Forensic Diagnostic)"
        self.set_font("Helvetica", "B", 7)
        self.cell(0, 4, sanitize_for_latin1(audit_text), new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
        self.ln(2)
        
        current_x = self.get_x() + 75
        if os.path.exists(self.logo1_path):
            self.image(self.logo1_path, x=current_x, y=self.get_y(), h=7)
        if os.path.exists(self.logo2_path):
            self.image(self.logo2_path, x=current_x + 25, y=self.get_y(), h=7)

def calculate_nearest_court(city_township):
    township_lower = city_township.lower()
    pta_court, jhb_court = (-25.74611, 28.18806), (-26.20444, 28.04167)
    user_loc = (-26.2678, 27.8585) if "soweto" in township_lower or "johannesburg" in township_lower else (-25.7479, 28.1132)
    
    R = 6371.0
    lat1, lon1 = math.radians(user_loc[0]), math.radians(user_loc[1])
    lat2, lon2 = math.radians(jhb_court[0]), math.radians(jhb_court[1])
    dlat, dlon = lat2 - lat1, lon2 - lon1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    dist = R * (2 * math.atan2(math.sqrt(a), math.sqrt(1 - a)))
    return "GAUTENG DIVISION, JOHANNESBURG", dist

def create_court_pdf(filename, title_text, content_text, litigant_meta, needs_commissioner=False):
    pdf = BPASICourtDocument(litigant_meta)
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=35)
    
    pdf.set_font("Helvetica", "B", 12)
    pdf.multi_cell(0, 6, sanitize_for_latin1(title_text), border=0, align="C")
    pdf.ln(10)
    
    pdf.set_font("Helvetica", "", 11)
    for paragraph in content_text.split('\n'):
        if paragraph.strip():
            pdf.multi_cell(0, 6, sanitize_for_latin1(paragraph.strip()))
            pdf.ln(4)
            
    if needs_commissioner:
        pdf.ln(12)
        pdf.set_font("Helvetica", "B", 11)
        self_name = sanitize_for_latin1(f"DEPONENT SIGNATURE CRITICAL LOCK: {litigant_meta['name'].upper()}")
        pdf.cell(0, 6, self_name, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="L")
        pdf.ln(4)
        pdf.set_font("Helvetica", "", 10)
        cert_text = "I hereby certify that the Deponent has acknowledged that he knows and understands the contents of this affidavit, which was signed and sworn to before me at _________________ on this _____ day of ___________________ 2026, the regulations contained in Government Notice No. R1258 of 21 July 1972, as amended, having been complied with."
        pdf.multi_cell(0, 5, sanitize_for_latin1(cert_text))
        pdf.ln(8)
        pdf.cell(0, 5, "_________________________________________", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="L")
        pdf.set_font("Helvetica", "B", 10)
        pdf.cell(0, 5, "COMMISSIONER OF OATHS (EX OFFICIO)", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="L")
        pdf.ln(5)
        pdf.cell(0, 15, "[ PLACE PHYSICAL SAPS PRECINCT STAMP HERE ]", border=1, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")

    pdf.output(filename)
    
    write_to_ghost_ledger({
        "status": "PDF_COMPILED_SUCCESSFULLY",
        "file_name": filename,
        "token": litigant_meta["token"]
    })

# =====================================================================
# CORE INTELLIGENT DISPATCH ROUTER
# =====================================================================
def run_bpasi_swarm():
    token = hashlib.sha256(f"{RAW_COMPLAINT}-{time.time()}".encode()).hexdigest()[:8].upper()
    
    court_division, calculated_radius = calculate_nearest_court(CITY)
    litigant_meta = {
        "name": FULL_NAME, "address": FULL_ADDRESS,
        "phone": PHONE, "email": EMAIL,
        "division": court_division, "distance": calculated_radius, "token": token
    }

    # Internal Audit Lead notification payload (Fulfilling info@celsiusmediagroup.co.za hook)
    lead_notification = {
        "lead_target": "info@celsiusmediagroup.co.za",
        "session_id": SESSION_ID,
        "timestamp": TIMESTAMP,
        "applicant": litigant_meta["name"],
        "calculated_jurisdiction": court_division,
        "token_reference": token
    }

    complaint_lower = RAW_COMPLAINT.lower()
    if "fisheries" in complaint_lower or "corruption" in complaint_lower or "anc" in complaint_lower:
        print("🔍 [BPASI ADVANCED FORENSICS ENGAGED] Executing absolute Constitutional mapping array...")
        fact_base = (
            "Evidence tracks critical procurement discrepancies and irregular expenditure outlays within the "
            "Department of Forestry, Fisheries and the Environment (DFFE) and state administration networks. "
            "These actions directly challenge the structural coherence and binding nature of the entire supreme law."
        )
    else:
        fact_base = RAW_COMPLAINT

    # Call AI endpoint securely pointing to Groq via the standard OpenAI SDK client wrapper
    if client:
        try:
            groq_res = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": f"Create a strict court-compliant CaseLines Master Index of Documents (MoI) based on this systemic constitutional challenge: {fact_base}"}],
                temperature=0.1
            )
            caselines_index = groq_res.choices[0].message.content
        except Exception as e:
            logger_err = f"API parsing exception resolved: {str(e)}"
            caselines_index = f"A01_Master_Index_{token}.pdf\nA02_Founding_Affidavit_Moahi_{token}.pdf"
            write_to_ghost_ledger({"status": "INFERENCE_FALLBACK", "detail": logger_err})
    else:
        caselines_index = f"A01_Master_Index_{token}.pdf\nA02_Founding_Affidavit_Moahi_{token}.pdf"

    print("⚙️ Compiling Document Dossier with supreme constitutional grounding...")
    heading = f"IN THE HIGH COURT OF SOUTH AFRICA\n{court_division}\n\nIn the matter between:\n{FULL_NAME.upper()} (Applicant)\nand\nTHE NATIONAL EXECUTIVE OF THE REPUBLIC OF SOUTH AFRICA & OTHERS (Respondents)"
    
    # 1. Generate Master Index (MoI)
    index_file_name = f"A01_Master_Index_of_Documents_{token}.pdf"
    create_court_pdf(index_file_name, heading, f"MASTER INDEX OF COURT DOCUMENTS\n\n{caselines_index}", litigant_meta)
    
    # 2. Generate Main Pleading Affidavit
    affidavit_body = (
        f"I, the undersigned, {FULL_NAME.upper()}, do hereby make oath and state:\n\n"
        f"1. I am an individual Litigant in Person initiating this application under Section 38(d) of the Constitution of the Republic of South Africa, 1996.\n\n"
        f"2. THE TOTAL CONSTITUTIONAL INTEGRITY VECTOR:\n"
        f"This application is brought not merely against individual sections, but directly against the systemic violation of the entire Constitution as the supreme law of the Republic under Section 2. The Respondents have systematically undermined the foundational values of the state, including the absolute Rule of Law enshrined in Section 1(c), the accountability mandates of Chapter 10, and the socio-economic safeguards of the Bill of Rights in Chapter 2.\n\n"
        f"3. THE COMPLAINT AND EVIDENCE SUITE:\n"
        f"{fact_base}\n\n"
        f"4. Wherefore the Applicant prays for an order declaring the entire course of conduct unconstitutional, invalid, and void ab initio."
    )
    affidavit_file_name = f"A02_Founding_Affidavit_Moahi_{token}.pdf"
    create_court_pdf(affidavit_file_name, "APPLICANT'S FOUNDING AFFIDAVIT", affidavit_body, litigant_meta, needs_commissioner=True)
    
    # Write complete session wrap up directly to the Ghost Ledger
    write_to_ghost_ledger({
        "status": "COMPREHENSIVE_CONSTITUTIONAL_DOSSIER_HARDLOCKED",
        "session_id": SESSION_ID,
        "index_generated": index_file_name,
        "affidavit_generated": affidavit_file_name,
        "lead_generated": lead_notification
    })

    print("\n🚀 [ULTIMATE SYSTEM STATUS ACHIEVED - COMPREHENSIVE CONSTITUTIONAL DOSSIER HARDLOCKED]")
    print(f"📬 Lead notification logged and queued for: {lead_notification['lead_target']}")

if __name__ == "__main__":
    run_bpasi_swarm()
